import numpy as np
import matplotlib.pyplot
import constants as c

resultA = np.load("ResultB_evolvedFootprints.npy")
resultA = resultA.reshape(5,-1)
resultA = resultA[1:, :]
print(resultA.shape)
# matplotlib.pyplot.plot(resultA, label="5 hidden neurons")
matplotlib.pyplot.rcParams["figure.figsize"]=(12,1)
matplotlib.pyplot.pcolormesh(resultA)
matplotlib.pyplot.show()