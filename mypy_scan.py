#!/usr/bin/env python3

"""
Checks all sketches for type errors and common Python mistakes.

Scans each lesson folder (chXX/NN.NN) and reports problems like:
- missing return values
- wrong argument types
- untyped lists (e.g. emitters = [])
- unsafe None usage

RUN:
python mypy_scan.py &> mypy_log.out
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

MYPY_ARGS: list[str] = [
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


@dataclass(frozen=True)
class LessonResult:
    lesson: Path
    checked_files: int
    mypy_exit_code: int


def repo_root() -> Path:
    return Path.cwd()


def relpath_str(p: Path, root: Path) -> str:
    try:
        return p.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return p.as_posix()


def is_lesson_dir(p: Path) -> bool:
    return p.is_dir() and LESSON_DIR_RE.match(p.name) is not None


def chapter_has_lessons(chapter: Path) -> bool:
    return chapter.is_dir() and any(is_lesson_dir(p) for p in chapter.iterdir())


def iter_lessons(root: Path) -> Iterable[Path]:
    for chapter in sorted(root.glob(CHAPTER_GLOB)):
        if not chapter.is_dir():
            continue
        for lesson in sorted(chapter.iterdir()):
            if is_lesson_dir(lesson):
                yield lesson


def collect_py_files(lesson: Path) -> list[Path]:
    return sorted(lesson.rglob('*.py'))


def run_mypy(files: list[Path], lesson: Path) -> int:
    if not files:
        return 0
    cmd = [sys.executable, '-m', 'mypy', *MYPY_ARGS, *map(str, files)]
    env = dict(os.environ)
    env['MYPYPATH'] = str(lesson)
    p = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if p.returncode != 0:
        if p.stdout:
            print(p.stdout, end='')
        if p.stderr:
            print(p.stderr, end='')
    return p.returncode


def main() -> None:
    root = repo_root()

    for chapter in sorted(root.glob(CHAPTER_GLOB)):
        if chapter.is_dir() and not chapter_has_lessons(chapter):
            print(f'Skipping {relpath_str(chapter, root)} -- no NN.NN lesson folders found')

    lessons = list(iter_lessons(root))
    if not lessons:
        print('No lesson folders found (expected chXX_name/NN.NN).', file=sys.stderr)
        sys.exit(2)

    results: list[LessonResult] = []
    any_fail = False

    for lesson in lessons:
        print('=' * 72)
        print(f'Checking {relpath_str(lesson, root)}')
        print('=' * 72)

        files = collect_py_files(lesson)

        if not files:
            print('(no .py files in this lesson)')
            results.append(LessonResult(lesson, 0, 0))
            continue

        code = run_mypy(files, lesson)
        any_fail |= code != 0
        results.append(LessonResult(lesson, len(files), code))

    failed = [r for r in results if r.mypy_exit_code != 0]
    passed = [r for r in results if r.mypy_exit_code == 0 and r.checked_files > 0]
    skipped_only = [r for r in results if r.checked_files == 0]

    print('\n' + '=' * 72)
    print('Summary')
    print('=' * 72)
    print(f'Lessons scanned: {len(results)}')
    print(f'Passed: {len(passed)}')
    print(f'Failed: {len(failed)}')
    print(f'Skipped (no files): {len(skipped_only)}')

    if failed:
        print('\nFailed lessons:')
        for r in failed:
            print(f'  - {relpath_str(r.lesson, root)} (checked {r.checked_files})')

    sys.exit(1 if any_fail else 0)


if __name__ == '__main__':
    main()
