import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
from time import sleep
import numpy
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self) :
        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Act(t)
            sleep(0.03)

    def __del__(self):
        p.disconnect()