import numpy as np
import matplotlib.pyplot
import constants as c

resultA = np.load("resultA.npy")
resultB = np.load("resultB.npy")
maxofA = np.max(resultA, axis = 1)
maxofB = np.max(resultB, axis = 1)
matplotlib.pyplot.plot(maxofA, label="5 hidden neurons", linewidth=3)
matplotlib.pyplot.plot(maxofB, label="10 hidden neurons")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()