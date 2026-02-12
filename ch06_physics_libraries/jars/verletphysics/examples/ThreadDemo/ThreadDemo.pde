import toxi.physics2d.constraints.*;
import toxi.physics2d.*;
import toxi.geom.*;
import toxi.math.*;
import toxi.color.*;
import toxi.util.*;
import java.util.*;

int NUM_PARTICLES = 200;

VerletPhysics2D physics;
VerletParticle2D head, tail;

void setup() {
  size(1024, 768, P3D);
  smooth();
  physics=new VerletPhysics2D();
  physics.setDrag(0.025);
  Vec2D stepDir=new Vec2D(1, 0).normalizeTo((float)width/NUM_PARTICLES);
  ParticleString2D s=new ParticleString2D(physics, new Vec2D(0, height/2), stepDir, NUM_PARTICLES+1, 1, 0.1);
  head=s.getHead();
  head.lock();
  tail=s.getTail();
  tail.addConstraint(new AxisConstraint(Vec2D.Axis.X, width));
  background(0);
}

void draw() {
  if ((frameCount % 100) == 0) {
    fill(0);
  } else {
    fill(0, 10);
  }
  //rect(0, 0, width, height);
  // additive blending
  PGL pgl = ((PGraphicsOpenGL)g).pgl;
  //pgl.blendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE);
  stroke(255, 50, 0, 10);
  noFill();
  head.set(0, mouseY);
  physics.update();
  beginShape();
  float hue = 0.8 + sin(frameCount * 0.001) * 0.15;

  for (VerletParticle2D p : physics.particles) {
    TColor c = TColor.newHSV(hue, 0.8, 0.75);
    float theta = p.getVelocity().magnitude();
    c.rotateRYB(theta*0.2);
    c.lighten(theta*0.1);
    c.desaturate(theta*0.05);
    stroke(c.toARGB());
    //ellipse(p.x, p.y, 5, 5);
    vertex(p.x, p.y);
  }
  endShape();
  //saveFrame("#####.png");
}

void keyPressed() {
  if (key == ' ') {
    saveFrame(DateUtils.timeStamp()+".png");
  }
}