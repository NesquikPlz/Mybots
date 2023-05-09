import numpy as np
import matplotlib.pyplot
import constants as c

resultA = np.load("resultA.npy")
resultB = np.load("resultB.npy")
maxofA = np.max(resultA, axis = 1)
maxofB = np.max(resultB, axis = 1)

resultA = resultA.T
resultB = resultB.T

# matplotlib.pyplot.plot(maxofA, label='no hidden neuron', color='blue')
# matplotlib.pyplot.plot(maxofB, label='10 hidden neurons', color='red')
for i in range(10) :
    matplotlib.pyplot.plot(resultA[i], color='blue')
    matplotlib.pyplot.plot(resultB[i], color='red')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()