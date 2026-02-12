import geomerative.*;
import toxi.geom.*;
import toxi.physics2d.*;
import toxi.physics2d.behaviors.*;
import toxi.physics2d.constraints.*;
import java.util.*;

int NUM_PARTICLES = 50;

VerletPhysics2D physics = new VerletPhysics2D();
Vec2D particleOrigin;
Circle c;
CircularConstraint myConstraint;
List<RShape> shapeList = new ArrayList<RShape>(NUM_PARTICLES);

RShape fluidShape;
void setup() {
    size(640, 360);
    smooth();
    RG.init(this);
    physics.setDrag(0.05f);
    physics.setWorldBounds(new Rect(0, 0, width, 300));
    physics.addBehavior(new GravityBehavior2D(new Vec2D(0, 0.15f)));
    c = new Circle(new Vec2D(width/2, height/2), 75);
    myConstraint = new CircularConstraint(c);
    particleOrigin = new Vec2D(width/2, 0);
    addParticle();
    fluidShape = shapeList.get(0);
}
void addParticle() {
    RShape s = RG.getEllipse(0, 0, height);
    s.scale(0.05);
    s.translate(particleOrigin.x, particleOrigin.y);  
    shapeList.add(s);
    VerletParticle2D p = new VerletParticle2D(Vec2D.randomVector().scale(5).addSelf(particleOrigin));
    p.addConstraint(myConstraint);
    physics.addParticle(p);
    physics.addBehavior(new AttractionBehavior2D(p, 5, -1.2f, 0.01f));
}
void draw() {
    background(255, 0, 0);
    if (physics.particles.size() < NUM_PARTICLES) {
        addParticle();
    }
    physics.update();
    float r = c.getRadius() * 2;
    fill(255, 125);
    ellipse(c.x, c.y, r, r);
    fill(255);
    // Uncomment this to get a different effect!
    // fluidShape = shapeList.get(0);
    int i = 0;
    for (VerletParticle2D p : physics.particles) {
        Vec2D v = p.getVelocity();
        RShape s = shapeList.get(i++);
        s.translate(v.x, v.y);
        fluidShape = RG.union(fluidShape, s);
    }
    fluidShape.draw();
}

