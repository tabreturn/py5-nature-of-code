#!/usr/bin/env python3

"""
Checks all sketches for type errors and common Python mistakes.

Scans each lesson folder (chXX/NN.NN) and reports problems like:
- missing return values
- wrong argument types
- untyped lists (e.g. emitters = [])
- unsafe None usage

REQUIRES:
Install mypy

RUN:
python mypy_scan.py &> mypy_log.out
"""

import ast
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

MYPY_ARGS = [
  '--python-version', '3.10',
  '--ignore-missing-imports',
  '--disallow-any-generics',
  '--disable-error-code', 'name-defined',
  '--disable-error-code', 'used-before-def',
  '--disable-error-code', 'has-type',
  '--disable-error-code', 'union-attr',
  '--explicit-package-bases',
  '--namespace-packages',
]

CHAPTER_GLOB = 'ch*'
LESSON_DIR_RE = re.compile(r'^\d+\.\d+$')

SKIP_DIRS = {
  '.git', '__pycache__', '.mypy_cache', '.pytest_cache',
  'venv', '.venv', 'build', 'dist'
}


def repo_root():
    return Path.cwd()


def relpath_str(p, root):
    try:
        return p.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return p.as_posix()


def is_lesson_dir(p):
    return p.is_dir() and LESSON_DIR_RE.match(p.name) is not None


def chapter_has_lessons(chapter):
    return chapter.is_dir() and any(is_lesson_dir(p) for p in chapter.iterdir())


def iter_lessons(root):
    for chapter in sorted(root.glob(CHAPTER_GLOB)):
        if not chapter.is_dir():
            continue
        for lesson in sorted(chapter.iterdir()):
            if is_lesson_dir(lesson):
                yield lesson


def collect_py_files(lesson):
    return sorted(lesson.rglob('*.py'))


def run_mypy(files, lesson):
    if not files:
        return 0

    cmd = [sys.executable, '-m', 'mypy', *MYPY_ARGS, *map(str, files)]
    env = dict(os.environ)
    env['MYPYPATH'] = str(lesson)

    p = subprocess.run(cmd, env=env, capture_output=True, text=True)

    if p.stdout:
        print(p.stdout, end='')
    if p.stderr:
        print(p.stderr, end='')

    return p.returncode


def scan_lessons(lessons, root):
    results = []
    any_fail = False
    warnings = 0

    for lesson in lessons:
        print('=' * 80)
        print(f'Checking {relpath_str(lesson, root)}')
        print('=' * 80)

        files = collect_py_files(lesson)

        if not files:
            print('WARNING: no .py files in this lesson')
            warnings += 1
            results.append((lesson, 0, 0))
            continue

        code = run_mypy(files, lesson)
        any_fail |= code != 0
        results.append((lesson, len(files), code))

    return results, any_fail, warnings


def summarize(results, root, warnings):
    failed = [r for r in results if r[2] != 0]
    passed = [r for r in results if r[2] == 0 and r[1] > 0]
    skipped_only = [r for r in results if r[1] == 0]

    print('\n' + '*' * 80)
    print('SUMMARY')
    print('*' * 80)
    print(f'Lessons scanned: {len(results)}')
    print(f'Passed: {len(passed)}')
    print(f'Failed: {len(failed)}')
    print(f'Skipped (no files): {len(skipped_only)}')
    print(f'Warnings: {warnings}')

    if failed:
        print('\nFailed lessons:')
        for lesson, checked_files, code in failed:
            _ = code
            print(f'  - {relpath_str(lesson, root)} (checked {checked_files})')


@dataclass(frozen=True)
class UntypedMethod:
    path: Path
    lineno: int
    class_name: str
    method_name: str
    missing: tuple


def iter_project_py_files(root):
    for p in root.rglob('*.py'):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def _missing_hints_for_method(fn):
    missing = []

    params = []
    params.extend(getattr(fn.args, 'posonlyargs', []))
    params.extend(fn.args.args)
    params.extend(fn.args.kwonlyargs)

    for a in params:
        if a.arg in ('self', 'cls'):
            continue
        if a.annotation is None:
            missing.append(a.arg)

    if fn.args.vararg is not None and fn.args.vararg.annotation is None:
        missing.append(f'*{fn.args.vararg.arg}')
    if fn.args.kwarg is not None and fn.args.kwarg.annotation is None:
        missing.append(f'**{fn.args.kwarg.arg}')

    if fn.returns is None:
        missing.append('return')

    return tuple(missing)


def scan_untyped_methods(root):
    findings = []

    for path in iter_project_py_files(root):
        try:
            src = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue

        try:
            tree = ast.parse(src, filename=str(path))
        except SyntaxError:
            continue

        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue

            for item in node.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if item.name == '__init__':
                    continue

                missing = _missing_hints_for_method(item)
                if missing:
                    findings.append(UntypedMethod(
                        path,
                        getattr(item, 'lineno', 1),
                        node.name,
                        item.name,
                        missing,
                    ))

    return findings


def report_untyped_methods(findings, root):
    if not findings:
        return 0

    print('\n' + '=' * 80)
    print('UNTYPED CLASS METHODS')
    print('=' * 80)

    for f in sorted(findings, key=lambda x: (str(x.path), x.lineno)):
        rel = relpath_str(f.path, root)
        print(f'{rel}:{f.lineno}  {f.class_name}.{f.method_name}  missing: {", ".join(f.missing)}')

    print(f'\nTotal: {len(findings)}')
    return 1


def main():
    root = repo_root()
    warnings = 0

    for chapter in sorted(root.glob(CHAPTER_GLOB)):
        if chapter.is_dir() and not chapter_has_lessons(chapter):
            print(f'WARNING: Skipping {relpath_str(chapter, root)} -- no NN.NN lesson folders found')
            warnings += 1

    lessons = list(iter_lessons(root))
    if not lessons:
        print('WARNING: No lesson folders found (expected chXX_name/NN.NN)')
        sys.exit(2)

    print()

    results, any_fail, lesson_warnings = scan_lessons(lessons, root)
    warnings += lesson_warnings

    summarize(results, root, warnings)

    findings = scan_untyped_methods(root)
    untyped_code = report_untyped_methods(findings, root)

    sys.exit(1 if (any_fail or untyped_code != 0) else 0)


if __name__ == '__main__':
    main()
