# ecologicalmodelling

## SYSTEM REQUIREMENTS:

1. Python 3.5 or later
2. Numpy v1.12.0
3. Matplotlib v2.0.0

### Recommendations:
1. Download with Anaconda for best results.
2. Installation for Anaconda: https://www.continuum.io/downloads
3. Download Pycharm for best performance. Known to not work on Spyder.


## BACKGROUND: 
Successional patterns and dynamics of tropical forests are extensively studied using chronosequences and, more recently, longitudinal studies. These empirical studies generally focus on local factors and processes, even though landscape-scale processes may play an equally important role. Most theoretical models of succession are largely verbal and hypotheses derived from these models often are not very specific. 

*As a consequence, it is not always clear what patterns to expect under a given hypothesis*. Here we describe a basic simulation model with simple assumptions and rules that operationalize specific hypotheses and explore how this model can generate predictions on how successional patterns differ within and across different landscapes. 

**METHODS:** We developed a simple rule-based simulation model in which fixed numbers of trees are added and removed from a plot at each time step. Trees are randomly selected from a local species pool (recruitment) and from the plot (mortality), based on their species identity and the age-dependent recruitment and mortality probabilities per species (group). Simulations are run for 35 years and for 50 plots at the time, and a range of alpha and beta diversity indices are calculated for each time step based on the generated data. 

*Refer to METHODS.md for more details on our methodology*

**RESULTS:** We show how different (combinations of) assumptions and rules related to 

1. size of and similarity among local species pools; and 
2. variation in the age-dependent recruitment and mortality rates of species affect the 
	+ sign, direction and shape of successional patterns in alpha and beta diversities as well as 
	+ how and how fast the species composition of local communities and the metacommunity changes over time. 

*Refer to RESULTS.md for more details on the results you can obtain and a way to interpret them*

**DISCUSSION:** A crucial element of most models of succession is the variation in how species are adapted to the changing conditions along a successional gradient and how that drives successional species turnover. Dispersal limited is a key driver of succession but not always explicitly included in succession models. Our simple modelling exercise provides insight in how both can affect successional patterns, and highlights *the need to study successional patterns on both local and landscape scale*. To test prediction from the model – and explore the role and relative importance of different ecological processes along major environmental and land-use gradients – we need studies with replicated plots per age class, replicated along land use gradient.

**TODO:**

1. Resampling: Incorporate relative recruitment and mortality rates for 3 groups of species into sampling function.
    + Each species has a certain proportion in the global species pool - Affects sampling from global to local
    + Group recruitment and mortality rates - Affects sampling from local to plot
2. Result: Want 3 separate groups for d0, d1 and d2 diversities as well as pairwise diversities
