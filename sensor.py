import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(1000)

    def Get_Value(self, t) :
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values[t]

    def Save_Values(self) :
            numpy.save("data/" + self.linkName + "SensorValues.npy", self.values)