import diversities
import simulation
import graphing
import time
from setup import *
from parameters import *

d0_alpha_overall = []
d0_beta_overall = []
d0_gamma_overall = []
d1_alpha_overall = []
d1_beta_overall = []
d1_gamma_overall = []
d2_alpha_overall = []
d2_beta_overall = []
d2_gamma_overall = []

start_time = time.time()
for i in range(sim_num):
    print("Simulation %s" % i)
    start_run = time.time()
    """ Run the Simulation """
    plot_year_species = simulation.plot_year_species(plots, years,
                                          species_global_pool, global_pool, local_pool_size, temporary_pool_size,
                                          recruit_rate, species_recruit_rate, species_mort_rate, death_rate, sim_results_filename)

    if produce_graphs==True:
        """ Calculate & Plot the Diversities """

        (d0_alpha_diversity, d0_beta_diversity, d0_gamma_diversity) = diversities.d0_div()
        # (d1_alpha_diversity, d1_beta_diversity, d1_gamma_diversity) = diversities.d1_div()
        # (d2_alpha_diversity, d2_beta_diversity, d2_gamma_diversity) = diversities.d2_div()

        """ Stores each alpha, beta and gamma diversity for d0, d1 and d2 for overall simulation """
        d0_alpha_overall.append(d0_alpha_diversity)
        # d1_alpha_overall.append(d1_alpha_diversity)
        # d2_alpha_overall.append(d2_alpha_diversity)

        d0_beta_overall.append(d0_beta_diversity)
        # d1_beta_overall.append(d1_beta_diversity)
        # d2_beta_overall.append(d2_beta_diversity)

        d0_gamma_overall.append(d0_gamma_diversity)
        # d1_gamma_overall.append(d1_gamma_diversity)
        # d2_gamma_overall.append(d2_gamma_diversity)

        """ Saves the plots for the graphs """
        x = [k for k in range(years)]

        abundances = plot_year_species[plots-1].T
        graphing.plot_abundance_by_year(x, abundances, "Years", "Species Abundance")

        graphing.plot_diversities(x, d0_alpha_diversity, 'r', 0, "Mean Alpha Diversity", i)
        graphing.plot_diversities(x, d0_gamma_diversity, 'g', 0, "Gamma Diversity", i)
        graphing.plot_diversities(x, d0_beta_diversity, 'b', 0, "Beta Diversity", i)
        # graphing.plot_diversities(x, d1_alpha_diversity, 'r', 1, "Mean Alpha Diversity", i)
        # graphing.plot_diversities(x, d1_gamma_diversity, 'g', 1, "Gamma Diversity", i)
        # graphing.plot_diversities(x, d1_beta_diversity, 'b', 1, "Beta Diversity", i)
        # graphing.plot_diversities(x, d2_alpha_diversity, 'r', 2, "Mean Alpha Diversity", i)
        # graphing.plot_diversities(x, d2_gamma_diversity, 'g', 2, "Gamma Diversity", i)
        # graphing.plot_diversities(x, d2_beta_diversity, 'b', 2, "Beta Diversity", i)

        # for m in range(3):
        #     (beta_turnover, beta_sorensen, beta_jaccard) = diversities.pairwise_beta(plot_year_species, m)
        #     t = np.mean(beta_turnover, axis=0)
        #     s = np.mean(beta_sorensen, axis=0)
        #     j = np.mean(beta_jaccard, axis=0)
        #     graphing.plot_pairwise_diversities(x, t, s, j, 'b', 'g', 'r', m)
        end_run = time.time()
        print("Simulation %s took % seconds" % (i, end_run - start_run))

if produce_graphs==True:
    """ Calculating Averages with Standard Error """
    d0_alpha_avg = np.mean(np.array(d0_alpha_overall), axis=0)
    d0_beta_avg = np.mean(np.array(d0_beta_overall), axis=0)
    d0_gamma_avg = np.mean(np.array(d0_gamma_overall), axis=0)

    d0_alpha_err = np.std(np.array(d0_alpha_overall), axis=0)
    d0_beta_err = np.std(np.array(d0_beta_overall), axis=0)
    d0_gamma_err = np.std(np.array(d0_gamma_overall), axis=0)

    # d1_alpha_avg = np.mean(np.array(d0_alpha_overall), axis=0)
    # d1_beta_avg = np.mean(np.array(d0_beta_overall), axis=0)
    # d1_gamma_avg = np.mean(np.array(d0_gamma_overall), axis=0)
    #
    # d1_alpha_err = np.std(np.array(d1_alpha_overall), axis=0)
    # d1_beta_err = np.std(np.array(d1_beta_overall), axis=0)
    # d1_gamma_err = np.std(np.array(d1_gamma_overall), axis=0)
    #
    # d2_alpha_avg = np.mean(np.array(d0_alpha_overall), axis=0)
    # d2_beta_avg = np.mean(np.array(d0_beta_overall), axis=0)
    # d2_gamma_avg = np.mean(np.array(d0_gamma_overall), axis=0)
    #
    # d2_alpha_err = np.std(np.array(d2_alpha_overall), axis=0)
    # d2_beta_err = np.std(np.array(d2_beta_overall), axis=0)
    # d2_gamma_err = np.std(np.array(d2_gamma_overall), axis=0)
    #
    """ Plotting Averages with Standard Error """
    # graphing.plot_simulations(x, d0_alpha_avg, d0_alpha_err, 'b', 0, sim_num, "alpha")
    # graphing.plot_simulations(x, d1_alpha_avg, d1_alpha_err, 'g', 0, sim_num, "alpha")
    # graphing.plot_simulations(x, d2_alpha_avg, d2_alpha_err, 'r', 0, sim_num, "alpha")
    #
    # graphing.plot_simulations(x, d0_beta_avg, d0_beta_err, 'b', 1, sim_num, "beta")
    # graphing.plot_simulations(x, d1_beta_avg, d1_beta_err, 'g', 1, sim_num, "beta")
    # graphing.plot_simulations(x, d2_beta_avg, d2_beta_err, 'r', 1, sim_num, "beta")
    #
    # graphing.plot_simulations(x, d0_gamma_avg, d0_gamma_err, 'b', 2, sim_num, "gamma")
    # graphing.plot_simulations(x, d1_gamma_avg, d1_gamma_err, 'g', 2, sim_num, "gamma")
    # graphing.plot_simulations(x, d2_gamma_avg, d2_gamma_err, 'r', 2, sim_num, "gamma")

end_time = time.time()
print("Simulation took %s seconds" % (end_time - start_time))