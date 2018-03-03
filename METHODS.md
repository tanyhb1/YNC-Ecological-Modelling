# METHODS

## Ver 1.0.0 29 March 2017
1. Read data given by the user, which contains the following
	+ Mortality and Recruitments of groups, given by variations in logistic curves
	+ List of species, their recruitment and mortality groups, and their proportion in the global species pool

2. Run simulation: 
	1. Create a temporary pool based on the global pool.
	2. Create a local pool from the temporary pool
	3. For each year, kill off trees and recruit trees.

3. Calculate species diversities: Species diversities are grouped according to three diversity indices, D0, D1 and D2. For each diversity indices our focus is on beta diversity, which is the dissimilarity of species over the landscape.
	1. D0 - Species Richness: Number of species in a sample unit (McCune, 2002)
	2. D1 - Shannon-Weiner Index: Quantifies the information content of a sample unit
	3. D2 - Simpson's Index: Measure of dominance of a species
There are also 3 types of beta diversities
	1. Turnover - This is the turnover rate per sample
	2. Local - Effective average proportion of species *within a unit* that are not ubiquitous
	3. Regional - Effective average proportion of species that are not ubiquitous
What does 'effective' mean then?


### Ways to think about diversity indices
D0, D1 and D2 all talk about how diverse plots of land are. The higher the index, the more diverse they are. The difference is the degree to which they factor in the abundance of species in a plot. D0 is only the species count. This means that even if you have 10 trees from species 1 and 4 trees from species 2, they are considered the same in the context of D0. This is taken more into account with D1, and D2.

### Sampling Methods
1. Global to temporary pool to local pool -> We are sampling based on the relative abundances of species in the global pool without replacement. This gives just the list of species that are in the pool. Then from the temporary pool, we sample one more time, taking into account the relative abundance in the temporary pool, into the local pool.
2. Local pool to plot
	1. Recruitment & Mortality - We sample a list of species from the local pool with replacement, taking into account the current abundance of species in the plot, as well as the species specific abundances according to which group they belong to. 
