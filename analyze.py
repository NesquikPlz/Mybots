import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# targetAnglesValues = numpy.load("data/targetAngles.npy")
b_targetAnglesValues = numpy.load("data/b_targetAngles.npy")
f_targetAnglesValues = numpy.load("data/f_targetAngles.npy")
# print(backLegSensorValues)
# matplotlib.pyplot.plot(backLegSensorValues, label="BackLeg", linewidth=3)
# matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg")
matplotlib.pyplot.plot(b_targetAnglesValues, label="backLeg Target Angles", linewidth=3)
matplotlib.pyplot.plot(f_targetAnglesValues, label="frontLeg Target Angles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()