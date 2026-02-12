/**
 * FieldLineCluster is a simple physics based simulation of dipoles with
 * time-varying charges and a visualization of field lines of their
 * surrounding electro-magnetic field. The poles themselves are connected
 * into a non-physically correct cluster using VerletSprings with one
 * particle/pole being linked to the mouse position. Field lines are
 * coloured based on the sign of the charge potential of the parent pole.
 *
 * (c) 2009 Karsten Schmidt // LGPL licensed
 */
import processing.opengl.*;

import toxi.physics2d.constraints.*;
import toxi.physics2d.*;
import toxi.geom.*;

import java.util.*;

int STEP_SIZE = 5;
int MAX_ITER = 200;
int DENSITY = 16;

VerletPhysics2D physics;

Pole[] poles=new Pole[20];

void setup() {
  size(1280, 720, OPENGL);
  physics=new VerletPhysics2D();
  physics.setWorldBounds(new Rect(1, 1, width-2, height-2));
  for (int i=0; i<poles.length; i++) {
    poles[i]=new Pole(random(width), random(height), random(-1, 1)*10);
    for (int j=0; j<i; j++) {
      physics.addSpring(new VerletSpring2D(poles[j], poles[i], 300, 0.001));
    }
  }
  poles[0].lock();
}

void draw() {
  background(255);
  noFill();
  physics.update();
  poles[0].set(mouseX, mouseY);
  poles[0].charge=10*sin(frameCount*0.01);
  for (int i=0; i<poles.length; i++) {
    for (float t=0; t<TWO_PI; t+=PI/DENSITY) {
      poles[i].draw(poles, t, STEP_SIZE);
    }
  }
}

class Pole extends VerletParticle2D {
  float charge;
  float radius=10;

  Pole(float x, float y, float c) {
    super(x, y);
    charge=c;
  }

  void draw(Pole[] poles, float theta, float step) {
    Vec2D dir=new Vec2D(radius, theta).toCartesian();
    Vec2D pos=add(dir);
    float sign=Math.signum(charge);
    int iter=0;
    float eventHorizon=sq(radius*0.9);
    boolean isTracing=true;
    beginShape();
    if (sign<0) {
      stroke(0, 0, 255);
    } 
    else {
      stroke(255, 0, 0);
    }
    vertex(x, y);
    step*=sign;
    Pole target=null;
    while (isTracing && ++iter<MAX_ITER) {
      dir.clear();
      for (int i=0; i<poles.length; i++) {
        Vec2D d=pos.sub(poles[i]);
        float mag=d.magSquared();
        if (mag<eventHorizon) {
          isTracing=false;
          target=poles[i];
          break;
        }
        dir.addSelf(d.scaleSelf(poles[i].charge/mag));
      }
      dir.normalize();
      if (isTracing) {
        vertex(pos.x, pos.y);
        pos.addSelf(dir.scaleSelf(step));
        isTracing=pos.isInRectangle(physics.getWorldBounds());
      } 
      else {
        if (target!=null) vertex(target.x, target.y);
      }
    }
    endShape();
  }
}

