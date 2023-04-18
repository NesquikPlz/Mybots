import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) +".nndf")
        os.system("del brain" + str(self.solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self) :
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices :
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self) :
        self.motors = {}
        # print(pyrosim.jointNamesToIndices)
        # exit()
        for jointName in pyrosim.jointNamesToIndices :
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t) :
        for i in self.sensors :
            self.sensors[i].Get_Value(t)

    def Act(self, t) :
        for neuronName in self.nn.Get_Neuron_Names() :
            if self.nn.Is_Motor_Neuron(neuronName) :
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # print(neuronName, jointName, desiredAngle)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

        # for i in self.motors :
        #     self.motors[i].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        tmpFileName = "tmp"+str(self.solutionID)+".txt"
        fitnessFileName = "fitness"+str(self.solutionID)+".txt"
        f = open(tmpFileName, "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system(f"rename {tmpFileName} {fitnessFileName}")