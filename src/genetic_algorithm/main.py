"""
	runner for our implamentation of GA in HFSP context
"""

import Chromosome
import GeneticAlgorithm

def main(
		data,
		population_size: int,
		crossover_probability: float,
		mutation_probability: float,
		generations_number: int):
	"""
		main function
	"""

	initial_population = initialize(data, population_size)

