import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self) :
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices :
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self) :
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices :
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t) :
        for i in self.sensors :
            self.sensors[i].Get_Value(t)

    def Act(self, t) :
        for i in self.motors :
            self.motors[i].Set_Value(self.robotId, t)
