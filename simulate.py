import math
import random
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import numpy
from time import sleep

b_amplitude = numpy.pi/4
b_frequency = 10
b_phaseOffset = 0
f_amplitude = numpy.pi/4
f_frequency = 20
f_phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
targetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
# targetAngles = numpy.sin(targetAngles) * numpy.pi / 4
b_targetAngles = b_amplitude*numpy.sin(b_frequency*targetAngles+b_phaseOffset)
f_targetAngles = f_amplitude*numpy.sin(f_frequency*targetAngles+f_phaseOffset)
# numpy.save("data/b_targetAngles.npy", b_targetAngles)
# numpy.save("data/f_targetAngles.npy", f_targetAngles)
# print(targetAngles)
# numpy.save("data/targetAngles.npy", targetAngles)
# exit()
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # print(i)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = b_targetAngles[i],
        maxForce = 30
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = f_targetAngles[i],
        maxForce = 30
    )
    sleep(0.01)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()
# print(backLegSensorValues)

