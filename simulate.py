import pybullet as p
from time import sleep

physicsClient = p.connect(p.GUI)
for i in range(1000):
    p.stepSimulation()
    print(i)
    sleep(0.015)
p.disconnect()