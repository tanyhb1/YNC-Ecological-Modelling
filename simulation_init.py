""" This initializes all the functions required for simulation"""

import numpy as np

def create_species_matrix(plots, years, species):
    # initializes the matrix for the number of plots and years
    # for output
    species_matrix = np.zeros((plots, years, species))
    return species_matrix

# For sampling a certain number of species from a species list
def sampling_func(species_list, required_num, replacement):
    """
    Species List: A tuple containing (list of species, weights)
    Required num: The number of species you want to draw
    Replacement: A boolean, whether you want to draw with replacement or without
    """
    list_of_species = species_list[0]
    weights = species_list[1]
    probabilities = []
    total_weights = np.sum(weights)
    total_weights = total_weights.astype(float)

    for i in range(len(weights)):
        p = weights[i] / total_weights
        probabilities.append(p)

    result = np.random.choice(list_of_species, required_num, replace=replacement, p=probabilities)

    return result

def create_temporary_pool(size_of_temp_pool, global_pool):
    """
    Returns the temporary pool, where each element is the species type
    """
    temp_pool = sampling_func(global_pool, size_of_temp_pool, False)
    abundances = np.take(global_pool[1], temp_pool)
    return (temp_pool, abundances)

def create_local_species_pool(plots, local_pool_size, temp_pool):
    local_species_pools = sampling_func(temp_pool, local_pool_size, False)
    return local_species_pools