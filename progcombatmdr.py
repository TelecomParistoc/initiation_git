from AX12 import AX12
from time import sleep
g=AX12(176)
d=AX12(175)
m=AX12(173)

def avancer(k=50):
  g.turn(k)
  d.turn(-k)
def reculer(k=50):
  avancer(-k)

def turnleft(k=50):
  g.turn(k)
  d.turn(k)
  sleep(3)
  g.turn(0)
  d.turn(0)

def turnright(k=50):
  g.turn(-k)
  d.turn(-k)
  sleep(3)
  g.turn(0)
  d.turn(0)

def moulin(k=70):
    m.turn(k)

def arrete():
    g.turn(0)
    d.turn(0)
