import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self) :
        targetAngles = numpy.linspace(0, 2 * numpy.pi, 1000)
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        if b"Front" in self.jointName :
            self.frequency = self.frequency/2
        self.motorValues = self.amplitude*numpy.sin(self.frequency*targetAngles+self.offset)

    def Set_Value(self, robotId, desiredAngle) :
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 100
        )

    def Save_Values(self):
        numpy.save("data/" + self.jointName + "JointValues.npy", self.motorValues)