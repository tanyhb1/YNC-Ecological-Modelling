# Number of successional years to examine: Note this has to align with "mortality-recruitment.csv"
year_num = 35

# Number of plots to be examined
plots = 40

# Maximum number of species a local pool can have
local_pool_size = 80

# If you use this, make sure that the temporary pool size is the same as the global species pool
effective_pool_size = 200

# Distributes species more to create variation
temporary_pool_size = 354

# Number of simulations to run
sim_num = 1

# Type of data for graphing
graph_typ = "OriginalData"

# Fixed recruitment and mortality rate for all plots
overall_density_curves = "mortality-recruitment.csv"

# Recruitment and Mortality groups that each species is under
species_groups = "sg0.csv"

# Species specific mortality and recruitment weights
group_recr_mortalities = "sc0.csv"

# for simulation results, please keep the "sim_results/" section so that it is saved in the right folder
sim_results_filename = "sim_results/LSP80"

# True -> Graphs calculating the diversities will be produced
produce_graphs = False

