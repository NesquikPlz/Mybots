import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(5) :
#     os.system("python generate.py")
#     os.system("python simulate.py")

os.system("chcp 65001")
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.save_resultMatrix()