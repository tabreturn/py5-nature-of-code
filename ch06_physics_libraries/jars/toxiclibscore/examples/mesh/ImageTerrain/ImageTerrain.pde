import toxi.geom.*;
import toxi.geom.mesh.*;

String IMG_PATH="2237.png";
float HEIGHT_SCALE = 0.04;
float BASE_Z = -1;

void setup() {
  PImage img = loadImage(IMG_PATH);
  Terrain terrain = new Terrain(img.width, img.height, 1);
  float[] el = new float[img.width * img.height];
  for (int i = 0; i < el.length; i++) {
      el[i] = (img.pixels[i] & 0xff) * HEIGHT_SCALE;
  }
  terrain.setElevation(el);
  WETriangleMesh mesh = new WETriangleMesh();
  terrain.toMesh(mesh, BASE_Z);
  new LaplacianSmooth().filter(mesh,1);
  mesh.saveAsSTL(sketchPath(IMG_PATH+".stl"));
  exit();
}