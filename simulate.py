from simulation import SIMULATION
import sys

simulation = SIMULATION(sys.argv[1])
simulation.Run()
simulation.Get_Fitness()


