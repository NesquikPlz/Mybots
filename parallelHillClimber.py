from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER :
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize) :
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self) :
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            print("---------\nGeneration : ", currentGeneration)
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        for i in solutions.keys() :
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions.keys():
            solutions[i].Wait_For_Simulation_To_End()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        for i in self.parents.keys() :
            print(f"Agent {i+1} : {self.parents[i].fitness} {self.children[i].fitness}")
        print("---------\n")
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness :
                self.parents[i] = self.children[i]

    def Show_Best(self):
        results = [x.fitness for x in self.parents.values()]
        bestSolution = results.index(min(results))
        # print(self.parents[bestSolution].fitness)
        self.parents[bestSolution].Start_Simulation("GUI")