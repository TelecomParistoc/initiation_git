from AX12 import AX12
from time import sleep
g=AX12(176)
d=AX12(175)
m=AX12(173)

def av(k=50):   #avancer
  g.turn(k)
  d.turn(-k)
def reculer(k=50):
  avancer(-k)

def l(k=70):   #tourner a gauche
  g.turn(-k)
  d.turn(-k)
  sleep(0.5)
  g.turn(0)
  d.turn(0)

def r(k=70):  #tourner a droite
  g.turn(k)
  d.turn(k)
  sleep(0.5)
  g.turn(0)
  d.turn(0)

def mol(k=70):  #moulin
    m.turn(k)
def smol(k=70): #stop moulin
    m.turn(0)

def stop():  #stop la voiture
    g.turn(0)
    d.turn(0)
