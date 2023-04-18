import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for i in range(5) :
#     os.system("python generate.py")
#     os.system("python simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()