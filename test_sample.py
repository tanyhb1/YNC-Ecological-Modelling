"""
Remember to run py.test in terminal to test code
"""

import simulation_init
import numpy as np

""" Check whether the matrix gives the right shape """
def test_create_species_matrix():
    assert (simulation_init.create_species_matrix(30, 50, 100).shape == (30, 50, 100))

""" Check whether probabilities are between 0 and 1 """
def test_sampling_function():
    species_list = ([1, 2, 3, 4, 5], [10, 5, 3, 8, 4])
    required_num = 3
    replacement = False
    result = simulation_init.sampling_func(species_list, required_num, replacement)
    assert (len(result) == required_num) # make sure that we get the number of species we need

""" After sampling, all the abundances should be greater than 0"""
def test_create_temporary_pool():
    species_global_pool = 10
    size_of_temp_pool = 5
    s = np.arange(0, species_global_pool, 1)
    p = [3] * species_global_pool
    global_pool = (s, p)
    (temp_pool, abundances) = simulation_init.create_temporary_pool(size_of_temp_pool, global_pool)
    assert (np.count_nonzero(abundances) != 0) # make sure that the abundances are not all 0

test_create_species_matrix()
test_sampling_function()
test_create_temporary_pool()