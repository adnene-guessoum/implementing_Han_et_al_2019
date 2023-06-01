"""
    Simple Genetic Algorithm for comparison purposes
"""

import numpy as np
import pandas as pd
import math
import time
import random

def read_data(path: str) -> list[pd.DataFrame]:
    """
        Read data from file
    """
    data_stage1 = pd.read_csv(path)
    data_stage2 = pd.read_csv(path)
    data_stage3 = pd.read_csv(path)

    stagewise_data_list = [data_stage1, data_stage2, data_stage3]
    return stagewise_data_list

def initialize_parameters(data: list[pd.DataFrame]) -> dict:
    """
        Initialize parameters
    """
    number_of_stages = 3

    number_of_machines = 0
    number_of_machines_per_stage = []
    for i in range(len(data)):
        number_of_machines += len(data[i].columns)
        number_of_machines_per_stage.append(len(data[i].columns))

    number_of_jobs = 12 # workpieces (n) in the paper

    population_size = 30
    crossover_probability = 0.8
    mutation_probability = 0.2
    number_of_iterations = 100

    parameters = {
        "number_of_stages": number_of_stages,
        "population_size": population_size,
        "generations": generations,
        "crossover_probability": crossover_probability,
        "number_of_jobs": number_of_jobs,
        "mutation_probability": mutation_probability,
        "number_of_iterations": number_of_iterations,
        "number_of_machines": number_of_machines,
        "number_of_machines_per_stage": number_of_machines_per_stage
        }

    return parameters

def generate_initial_solutions(parameters: dict, data: list[pd.DataFrame]):
    """
    Randomize machine selection for initial population generation
    """

    initial_solution = {}
    key = 0

    for chromosome in range(parameters["population_size"]):
        chromosome = []

        for stage in range(parameters["number_of_stages"]):
            for job in range(parameters["number_of_jobs"]):
                selected = random.choice(data[stage].iloc[job, :].values)
                machine = data[stage].columns.get_loc(selected)
                solution_dict = {
                    "stage": stage,
                    "job": job,
                    "machine": machine
                    "operation_time": selected
                    }
                chromosome.append(solution_dict)
                key += 1
                initial_solution["chromosome_" + key] = chromosome

    return initial_solution


def select_parents(initial_solution: list[list[int]], parameters: dict):
    """
        Fitness Proportionate Selection
        Or
        Tournament Selection...
    """
    pass

def crossover(parents):
    """
        One point crossover
        Or
        Two point crossover
        Or
        Uniform crossover
    """
    pass

def mutate(child):
    """
        Random mutation
    """
    pass

def evaluate(population):
    """
        Evaluate fitness of each chromosome
    """
    pass


def genetic_algorithm(data, population_size: int, generations: int):    
    """
        Main Genetic Algorithm
    """
    pass














