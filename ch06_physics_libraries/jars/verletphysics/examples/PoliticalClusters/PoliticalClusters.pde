/**
 * PoliticalClusters demo is based on Attraction2D demo bundled with
 * toxiclibs-0020.
 *
 * Copyright (c) 2012 Karsten Schmidt // LGPL 2.1 licensed 
 */
 
import toxi.geom.*;
import toxi.math.*;
import toxi.color.*;
import toxi.util.datatypes.*;
import toxi.physics2d.*;
import toxi.physics2d.behaviors.*;

import processing.opengl.*;

int NUM_PARTICLES = 200;
 
VerletPhysics2D physics;
// attractors for forming clusters
AttractionBehavior2D leftWing, rightWing;
// size range for particles (with bias @ 20, 33% standard deviation)
BiasedFloatRange sizeRange = new BiasedFloatRange(5, 50, 20, 0.33);

void setup() {
  size(1280, 720, OPENGL);
  // setup physics with 10% drag
  physics = new VerletPhysics2D();
  physics.setDrag(0.1f);
  physics.setWorldBounds(new Rect(0, 0, width, height));

  leftWing = new AttractionBehavior2D(new Vec2D(width*0.25, height/2), width, 0.1f);
  rightWing = new AttractionBehavior2D(new Vec2D(width*0.75, height/2), width, 0.1f);
}
 
void addParticle() {
  boolean isLeftWing = MathUtils.flipCoin();
  Vec2D pos = new Vec2D(width, 0).scaleSelf(isLeftWing ? 0.4 : 0.6);
  PoliticalParticle p = new PoliticalParticle(pos, sizeRange.pickRandom(), isLeftWing);
  physics.addParticle(p);
  // add to either political attractor
  p.addBehavior(p.isLeftWing ? leftWing : rightWing);
  // add a negative attraction force field around the new particle
  // make force radius slightly larger than needed to create gaps between particles
  physics.addBehavior(new AttractionBehavior2D(p, p.size*2.2, -2f, 0.01f));
}
 
void draw() {
  ellipseMode(RADIUS);
  background(255);
  noStroke();
  fill(255);
  if (physics.particles.size() < NUM_PARTICLES) {
    addParticle();
  }
  physics.update();
  for (VerletParticle2D p : physics.particles) {
    PoliticalParticle pp = (PoliticalParticle)p;
    fill((pp.isLeftWing ? TColor.RED : TColor.BLUE).toARGB()); 
    ellipse(p.x, p.y, pp.size, pp.size);
  }
}

class PoliticalParticle extends VerletParticle2D {
  float size;
  boolean isLeftWing;
  
  PoliticalParticle(Vec2D p, float r, boolean isLeftWing) {
    super(p);
    this.size = r;
    this.isLeftWing = isLeftWing;
  }
}
