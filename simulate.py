from simulation import SIMULATION
import sys

simulation = SIMULATION(sys.argv[1], sys.argv[2])
simulation.Run()
simulation.Get_Fitness()


