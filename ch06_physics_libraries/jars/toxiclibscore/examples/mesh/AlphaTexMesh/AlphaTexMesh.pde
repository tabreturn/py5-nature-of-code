import toxi.geom.*;
import toxi.geom.mesh.*;
import toxi.processing.*;
import java.util.*;
import java.io.*;

PImage img, tex;
WETriangleMesh mesh;

ToxiclibsSupport gfx;

void setup() {
  size(640, 480, P3D);
  img = loadImage("mask_frame235.png");
  // find region of interest
  Rect bounds = findRegion(img);
  // crop & save region as texture for file
  tex = img.get((int)bounds.x, (int)bounds.y, (int)bounds.width, (int)bounds.height);
  String texName = "tex01.png";
  tex.save(sketchPath("obj/"+texName));
  // create height mesh of region
  mesh = parseImageRegion(img, bounds);
  // center mesh
  mesh.center(null);
  // smooth
  new LaplacianSmooth().filter(mesh, 2);
  mesh.computeFaceNormals();
  mesh.computeVertexNormals();
  createMaterialFile(sketchPath("obj/tex.mtl"), texName);
  // export mesh as OBJ with normals, uv's & flipped V coordinates
  saveAsObj(mesh, sketchPath("obj/wave.obj"), true, true, true);
  textureMode(NORMAL);
  gfx = new ToxiclibsSupport(this);
}

void draw() {
  background(100);
  translate(width/2, height/2, 0);
  rotateX(mouseY*0.01);
  rotateY(mouseX*0.01);
  noStroke();
  gfx.texturedMesh(mesh, tex, false);
}

/**
 * Returns region of interest in supplied image
 */
Rect findRegion(PImage img) {
  Vec2D min = Vec2D.MAX_VALUE.copy();
  Vec2D max = Vec2D.MIN_VALUE.copy();
  for (int y = 0; y < img.height; y++) {
    for (int x = 0; x < img.width; x++) {
      int idx = x + y * img.width;
      int col = img.pixels[idx];
      if (alpha(col) == 255 && brightness(col) > 50) {
        Vec2D p = new Vec2D(x, y);
        min.minSelf(p);
        max.maxSelf(p);
      }
    }
  }
  return new Rect(min, max);
}

/**
 * Returns an elevation value for the given color
 */
float mapElevation(int col) {
  return map(brightness(col), 0, 255, -30, 30);
}

/**
 * Generates a height mesh in XY plane from given image region
 */
WETriangleMesh parseImageRegion(PImage img, Rect bounds) {
  int[] pix = img.pixels;
  int w = img.width, h = img.height;
  Vec2D uvScale = bounds.getDimensions().sub(1, 1).reciprocal();
  WETriangleMesh mesh = new WETriangleMesh("mesh");
  // create index of valid points in image
  HashSet<Integer> pointIndex = new HashSet<Integer>((int)bounds.getArea());
  for (int y = (int)bounds.y,
       bx = (int)bounds.getRight(),
       by = (int)bounds.getBottom(),
       v = 0;
       y < by; y++, v++) {
      for (int x = (int)bounds.x, u = 0; x < bx; x++, u++) {
      int idx = x + y * w;
      int col = pix[idx];
      // valid point?
      if (alpha(col) == 255 && brightness(col) > 50) {
        pointIndex.add(idx);
        // only generate mesh faces if neighbors are valid too
        if (pointIndex.contains(idx - w - 1) &&
          pointIndex.contains(idx - w) &&
          pointIndex.contains(idx - 1)) {
          Vec3D a = new Vec3D(x - 1, y - 1, mapElevation(pix[idx - w - 1]));
          Vec3D b = new Vec3D(x, y - 1, mapElevation(pix[idx - w]));
          Vec3D c = new Vec3D(x - 1, y, mapElevation(pix[idx - 1]));
          Vec3D d = new Vec3D(x, y, mapElevation(col));
          Vec2D uvA = new Vec2D(u - 1, v - 1).scaleSelf(uvScale);
          Vec2D uvB = new Vec2D(u, v - 1).scaleSelf(uvScale);
          Vec2D uvC = new Vec2D(u - 1, v).scaleSelf(uvScale);
          Vec2D uvD = new Vec2D(u, v).scaleSelf(uvScale);
          mesh.addFace(a, b, c, uvA, uvB, uvC);
          mesh.addFace(c, b, d, uvC, uvB, uvD);
        }
      }
    }
  }
  return mesh;
}

/**
 * Exports mesh as OBJ
 * Supports flags for exporting normals, UV coords and flipping of V coordinates
 * Builds index of unique tex coords to reduce filesize
 */
void saveAsObj(TriangleMesh m, String path, boolean saveNormals, boolean saveUVs, boolean flipV) {
  println("saving OBJ: "+path);
  OBJWriter obj = new OBJWriter();
  obj.beginSave(path);

  int vOffset = obj.getCurrVertexOffset() + 1;
  int nOffset = obj.getCurrNormalOffset() + 1;
  int uvOffset = obj.getCurrUVOffset() + 1;

  obj.newObject(m.name);
  obj.addMaterialFile("tex.mtl");
  // vertices
  for (Vertex v : m.vertices.values()) {
    obj.vertex(v);
  }
  println(m.vertices.size()+" vertices");

  HashMap<Vec2D, Integer> uvIndex = new HashMap<Vec2D, Integer>();
  if (saveUVs) {
    int uvID = uvOffset;
    for (Face f : m.faces) {
      if (!uvIndex.containsKey(f.uvA)) {
        uvIndex.put(f.uvA, uvID);
        obj.uv(f.uvA, flipV);
        uvID++;
      }
      if (!uvIndex.containsKey(f.uvB)) {
        uvIndex.put(f.uvB, uvID);
        obj.uv(f.uvB, flipV);
        uvID++;
      }
      if (!uvIndex.containsKey(f.uvC)) {
        uvIndex.put(f.uvC, uvID);
        obj.uv(f.uvC, flipV);
        uvID++;
      }
    }
    println(uvIndex.size()+" texcoords");
  }

  // normals
  if (saveNormals) {
    for (Vertex v : m.vertices.values()) {
      obj.normal(v.normal);
    }
    println(m.vertices.size()+" normals");
  }

  // handle all 4 variations of normals/uvs
  if (saveNormals) {
    if (saveUVs) {
      for (Face f : m.faces) {
        obj.faceWithNormalsAndUVs(
        f.a.id + vOffset, f.b.id + vOffset, f.c.id + vOffset, 
        f.a.id + nOffset, f.b.id + nOffset, f.c.id + nOffset, 
        uvIndex.get(f.uvA), uvIndex.get(f.uvB), uvIndex.get(f.uvC));
      }
    }
    else {
      for (Face f : m.faces) {
        obj.faceWithNormals(
        f.b.id + vOffset, f.a.id + vOffset, f.c.id + vOffset, 
        f.a.id + nOffset, f.b.id + nOffset, f.c.id + nOffset);
      }
    }
  } 
  else {
    if (saveUVs) {
      for (Face f : m.faces) {
        obj.faceWithUVs(
        f.a.id + vOffset, f.b.id + vOffset, f.c.id + vOffset, 
        uvIndex.get(f.uvA), uvIndex.get(f.uvB), uvIndex.get(f.uvC));
      }
    } 
    else {
      for (Face f : m.faces) {
        obj.face(f.b.id + vOffset, f.a.id + vOffset, f.c.id + vOffset);
      }
    }
  }
  println(m.faces.size()+" faces written");
  obj.endSave();
}

void createMaterialFile(String path, String texFileName) {
  PrintWriter out = createWriter(path);
  out.println("newmtl Texture_0");
  out.println("map_Kd " + texFileName);
  out.close();
  println("wrote MTL file: "+path);
}

