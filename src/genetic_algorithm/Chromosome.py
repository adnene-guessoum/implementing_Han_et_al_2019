"""
	Necessary classes and functions for GA
"""

import math

class Gene:
	def __init__(self, start_time, machine):
		self.stage = machine.stage_affectation
		self.start_time = start_time
		self.processing_time = machine.machining_time
		self.end_time = start_time + machine.processing_time


# one chr = one solution ie. the complete
# sequential path of a workpiece through the
# machines (chosen amongst machines of a stage)
class Chromosome:
	def __init__(self, solution: list[object]):
		self.chromosome = solution

	def compute_fitness():
		return

	def compute_cmax():
		return


