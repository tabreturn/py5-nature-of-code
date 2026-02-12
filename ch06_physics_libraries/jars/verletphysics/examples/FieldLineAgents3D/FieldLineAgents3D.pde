/**
 * FieldLineAgents is a simulation of agents tracing field lines within
 * a cluster of randomly charged dipoles. Agents are spawned in uniform
 * directions from each pole and collect their trajectory in a list.
 * Agents stop evaluating the field once they reach another pole or leave
 * the bounding rect of the simulation.
 *
 * The agent behavior can be modified using the SELF_AVOIDANCE flag, which
 * when true ensures that agents *always* travel away from their parent pole.
 *
 * Usage:
 *
 * click on poles to toggle their charge (positive/negative)
 * r: reset & randomize simulation
 * a: toggle agent self avoidance
 *
 * (c) 2012 Karsten Schmidt // LGPL licensed
 */
import processing.opengl.*;

import toxi.geom.*;
import toxi.geom.mesh.*;
import toxi.color.*;
import toxi.math.*;
import toxi.util.*;
import toxi.processing.*;
import java.util.*;

int SPEED = 5;
int NUM_POLES = 5;
int NUM_AGENTS = 20;
boolean SELF_AVOIDANCE = false;

List<Pole> poles=new ArrayList<Pole>();
List<Agent> agents = new ArrayList<Agent>();

AABB bounds;

ToxiclibsSupport gfx;
boolean doSave;

void setup() {
  size(1280, 720, OPENGL);
  initSimulation();
  bounds=new AABB(new Vec3D(),new Vec3D(600,600,600));
  gfx=new ToxiclibsSupport(this);
}

void draw() {
  background(255);
  translate(width/2, height/2, 0);
  rotateX(mouseY*0.01);
  rotateY(mouseX*0.01);
  noFill();
  stroke(0);
  for (Agent a : agents) {
    a.update(poles);
    // ignore agents which do not manage to leave parent pole
    if (a.path.size()>3) {
      gfx.stroke(a.isAlive ? TColor.RED : TColor.BLUE.copy().setAlpha(0.5));
      gfx.lineStrip3D(a.path);
    }
  }
  if (doSave) {
    saveFrame("agents-"+DateUtils.timeStamp()+".png");
    doSave=false;
  }
}

void keyPressed() {
  if (key=='r') initSimulation();
  if (key=='a') {
    SELF_AVOIDANCE=!SELF_AVOIDANCE;
    resetAgents();
  }
  if (key==' ') {
    doSave=true;
  }
}

void initSimulation() {
  poles.clear();
  for (int i=0; i<NUM_POLES; i++) {
    poles.add(new Pole(Vec3D.randomVector().scaleSelf(random(300)), makeCharge(5)));
  }
  resetAgents();
}

void resetAgents() {
  agents.clear();
  // distribute agents uniformly on sphere
  SphereFunction sf=new SphereFunction(SPEED);
  for (Pole p : poles) {
    for (int i=0; i<NUM_AGENTS; i++) {
      for (int j=0; j<NUM_AGENTS; j++) {
        Vec3D dir = sf.computeVertexFor(new Vec3D(), j*PI/NUM_AGENTS, i*TWO_PI/NUM_AGENTS);
        agents.add(new Agent(p, dir, SPEED));
      }
    }
  }
}

float makeCharge(float c) {
  if (MathUtils.flipCoin()) c=-c;
  return c;
}

class Pole extends Vec3D {
  float charge;

  Pole(Vec3D p, float c) {
    super(p);
    charge=c;
  }
}

class Agent {
  Pole parent;
  Vec3D pos;
  float targetDist;
  float speed;
  boolean isAlive=true;

  List<Vec3D> path=new LinkedList<Vec3D>();

  Agent(Pole p, Vec3D dir, float speed) {
    path.add(p.copy());
    this.pos=p.add(dir);
    this.targetDist=sq(speed*0.9);
    this.speed=speed;
    this.parent=p;
  }

  void update(List<Pole> poles) {
    if (isAlive) {
      Vec3D dir=new Vec3D();
      Vec3D target=null;
      for (Pole p : poles) {
        Vec3D d=pos.sub(p);
        float mag=d.magSquared();
        if (mag<targetDist) {
          isAlive=false;
          target=p;
          break;
        }
        if (p!=parent || !SELF_AVOIDANCE) {
          dir.addSelf(d.scaleSelf(p.charge/mag));
        } 
        else {
          dir.addSelf(d.scaleSelf(abs(p.charge)/mag));
        }
      }
      dir.normalize();
      if (isAlive) {
        path.add(pos.copy());
        pos.addSelf(dir.scale(speed));
        isAlive=pos.isInAABB(bounds);
      } 
      else {
        if (target!=null) path.add(target.copy());
      }
    }
  }
}

