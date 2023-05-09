import pybullet_data
import pybullet as p
from time import sleep
from world import WORLD
from robot import ROBOT
import numpy as np
import constants as c
import os

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if self.directOrGUI == "DIRECT" :
            self.physicsClient = p.connect(p.DIRECT)
        else :
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self) :
        for t in range(1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            if self.directOrGUI == "GUI" :
                sleep(0.005)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()

    def Get_Footprint(self):
        self.robot.Get_footprint()