"""
	Simple Genetic Algorithm for comparison purposes
"""

import numpy as np
import pandas as pd
import math
import time
import random

import Chromosome as ch

def generate_random_solution(machines_per_stage: list[list]): # or more simply dataset as pandas Dataframe
	"""
	Randomize machine selection for initial population generation
	"""

	temp_solution = []

	for stage in machines_per_stage:
		selected = random.choice(stage)
		temp_solution.append(selected)

	return temp_solution


def initialize(data, population_size: int):
	"""
	Generate initial Population of solutions
	"""
	initial_pop = [];

	# one chromosome = one solution, as many solution as pop_size
	for i in range(population_size):
		new_chromosome = ch.Chromosome(generate_random_solution(data))
		initial_pop.append(new_chromosome)

	return initial_population

def select_parents(population):
	"""
		Fitness Proportionate Selection
		Or
		Tournament Selection...
	"""
	
