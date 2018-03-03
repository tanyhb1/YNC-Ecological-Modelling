from simulation import *
import math
import numpy as np
from itertools import combinations
from setup import *

plot_year_species = plot_year_species(plots, years,
                                      species_global_pool, global_pool, local_pool_size, temporary_pool_size,
                                      recruit_rate, species_recruit_rate, species_mort_rate, death_rate, sim_results_filename)

def d0_div ():
    d0_alpha_diversity = np.zeros(years)
    d0_beta_diversity = np.zeros(years)
    d0_gamma_diversity = np.zeros(years)
    # Calculating D0_diversities
    for y in range(years):
        # Calculating alpha diversity
        average_alpha_diversity = 0
        for p in range(plots):
            alpha_diversity = 0
            for s in range(species_global_pool):
                if plot_year_species[p][y][s] > 0:
                    alpha_diversity += 1
            average_alpha_diversity = average_alpha_diversity + alpha_diversity
        d0_alpha_diversity[y] = average_alpha_diversity / plots

        # Calculating gamma_diversity
        gamma_diversity = 0
        for s in range(species_global_pool):
            sp_boolean = False
            for p in range(plots):
                if plot_year_species[p][y][s] > 0:
                    sp_boolean = True
            if sp_boolean:
                gamma_diversity += 1
        d0_gamma_diversity[y] = gamma_diversity

        # Calculating beta diversity
        d0_beta_diversity[y] = d0_gamma_diversity[y] / d0_alpha_diversity[y]
    print("Calculated D0 Diversities")
    return (d0_alpha_diversity, d0_beta_diversity, d0_gamma_diversity)

def d1_div():
    across_plots = np.sum(plot_year_species, axis=0).transpose()
    # Summing over all species, so you get the total number of species across all plots each year
    total_species = np.sum(across_plots, axis=0)

    # Calculate Gamma diversity
    d1_gamma_diversity = np.zeros(years)
    for y in range(years):
        gamma_diversity = 0
        for s in range(species_global_pool):
            p = across_plots[s][y] / total_species[y]
            if (p != 0):
                gamma_diversity += -((p) * math.log(p, math.e))
        gamma_diversity = math.exp(gamma_diversity)
        d1_gamma_diversity[y] = gamma_diversity

    # Calculate Alpha Diversity
    d1_alpha_diversity = np.zeros(years)
    for y in range(years):
        alpha_diversity_by_plot = []
        for p in range(plots):
            alpha_diversity = 0
            div_probabilities = []
            # sum over all species
            diversity_abundance = np.sum(plot_year_species[p][y])
            # for each species
            for s in range(len(plot_year_species[p][y])):
                probability_s = (plot_year_species[p][y][s] / diversity_abundance)
                # Calculate alpha diversity per plot, summing across species
                if (probability_s != 0):
                    alpha_diversity += -((probability_s) * (math.log(probability_s, math.e)))
            alpha_diversity = math.exp(alpha_diversity)
            alpha_diversity_by_plot.append(alpha_diversity)
            # Get total alpha diversity
            total_alpha_diversity = np.sum(alpha_diversity_by_plot)
            # Get the average
        average_alpha_diversity = total_alpha_diversity / plots
        d1_alpha_diversity[y] = average_alpha_diversity

    # Calculate Beta Diversity
    d1_beta_diversity = np.divide(d1_gamma_diversity, d1_alpha_diversity)
    print("Calculated d1 diversities")
    return(d1_alpha_diversity, d1_beta_diversity, d1_gamma_diversity)

def d2_div():
    # Calculate Gamma diversity
    d2_gamma_diversity = np.zeros(years)
    for y in range(years):
        div_probabilities = []
        species_across_plots = []
        # for each species
        for s in range(species_global_pool):
            total = 0
            # summing across the landscapes
            for p in range(plots):
                total += plot_year_species[p][y][s]
            species_across_plots.append(total)
        overall_abundance = np.sum(species_across_plots)

        p = 0
        for i in range(len(species_across_plots)):
            p += (species_across_plots[i] / overall_abundance) ** 2.0
        d2_gamma_diversity[y] = 1 / p

    # Calculate Alpha Diversity
    d2_alpha_diversity = np.zeros(years)
    for y in range(years):
        alpha_diversity_by_plot = []
        for p in range(plots):
            alpha_diversity = 0
            div_probabilities = []
            # sum over all species
            diversity_abundance = np.sum(plot_year_species[p][y])
            # for each species
            for s in range(len(plot_year_species[p][y])):
                probability_s = (plot_year_species[p][y][s] / diversity_abundance)
                # Calculate alpha diversity per plot, summing across species
                if (probability_s != 0):
                    alpha_diversity += probability_s ** 2
            alpha_diversity_by_plot.append(1 / alpha_diversity)
            # Get total alpha diversity
            total_alpha_diversity = np.sum(alpha_diversity_by_plot)
            # Get the average
        average_alpha_diversity = total_alpha_diversity / plots
        d2_alpha_diversity[y] = average_alpha_diversity
    # Calculate Beta Diversity
    d2_beta_diversity = np.divide(d2_gamma_diversity, d2_alpha_diversity)
    print("Calculated d2 diversities")
    return (d2_alpha_diversity, d2_beta_diversity, d2_gamma_diversity)


""" Calculating Pairwise Diversities """

""" Calculating the beta diversities for plot, local and regional scale """
def calculate_turnover(beta):
    t = np.subtract(beta, 1)
    return t

def calculate_sorensen(beta, q):
    if (q==0):
        s = np.subtract(beta, 1)
        return s
    elif(q==1):
        s = np.divide(np.log(beta), math.log(2))
        return s
    else:
        s = np.subtract(2, np.divide(2, beta))
        return s

def calculate_jaccard(beta, q):
    if (q==0):
        j = np.subtract(2, np.divide(2, beta))
        return j
    elif (q==1):
        j = np.divide(np.log(beta), math.log(2))
        return j
    else:
        j = np.subtract(beta, 1)
        return j

""" Actual calculation of pairwise beta diversities """

def pairwise_beta(plot_year_species, q):
    plot_arr = [i for i in range(plots)]
    plot_comb = list(combinations(plot_arr, 2))

    beta_turnover = []
    beta_sorensen = []
    beta_jaccard = []
    for comb in plot_comb:
        # separate the pairings
        p1 = comb[0]
        p2 = comb[1]
        gamma_diversity = []
        alpha_diversity = []
        for y in range(years):
            # create the plot_species_matrix to calculate diversities
            p1_spec = plot_year_species[p1][y]
            p2_spec = plot_year_species[p2][y]
            plot_species_matrix = np.vstack((p1_spec, p2_spec)).transpose()

            # calculate gamma diversity
            sum_across_plots = np.sum(plot_species_matrix, axis=1)  # gets the sum of each species across plots
            if (q==0):
                gamma = np.count_nonzero(sum_across_plots)
                gamma_diversity.append(gamma)

                # calculate alpha diversity
                alpha = np.zeros(2)
                alpha[0] = np.count_nonzero(p1_spec)
                alpha[1] = np.count_nonzero(p2_spec)

                alpha_mean = np.mean(alpha)
                alpha_diversity.append(alpha_mean)
            elif (q==1):
                total_abundance = np.sum(sum_across_plots)
                p = np.divide(np.take(sum_across_plots, np.nonzero(sum_across_plots)), total_abundance)

                log_p = np.log(p)
                p_log_p = np.multiply(p, log_p)
                gamma = math.exp(-np.sum(p_log_p))
                gamma_diversity.append(gamma)

                # calculate alpha_diversity
                d1_alpha = np.zeros(2)
                total_p1 = np.sum(p1_spec)
                total_p2 = np.sum(p2_spec)

                prob1 = np.divide(np.take(p1_spec, np.nonzero(p1_spec)), total_p1)
                log_p1 = np.log(prob1)
                p1_log_p1 = np.multiply(prob1, log_p1)
                d1_alpha_p1 = math.exp(-np.sum(p1_log_p1))

                prob2 = np.divide(np.take(p2_spec, np.nonzero(p2_spec)), total_p2)
                log_p2 = np.log(prob2)
                p2_log_p2 = np.multiply(prob2, log_p2)
                d1_alpha_p2 = math.exp(-np.sum(p2_log_p2))

                d1_alpha_avg = (d1_alpha_p2 + d1_alpha_p1) / 2
                alpha_diversity.append(d1_alpha_avg)
            elif (q==2):
                total_abundance = np.sum(sum_across_plots)
                p = np.divide(np.take(sum_across_plots, np.nonzero(sum_across_plots)), total_abundance)

                p = np.power(p, 2)
                gamma = np.divide(1, np.sum(p))
                gamma_diversity.append(gamma)

                # calculate alpha_diversity
                total_p1 = np.sum(p1_spec)
                total_p2 = np.sum(p2_spec)

                prob1 = np.divide(np.take(p1_spec, np.nonzero(p1_spec)), total_p1)
                prob1 = np.power(prob1, 2)
                d2_alpha_p1 = np.divide(1, np.sum(prob1))

                prob2 = np.divide(np.take(p2_spec, np.nonzero(p2_spec)), total_p2)
                prob2 = np.power(prob2, 2)
                d2_alpha_p2 = np.divide(1, np.sum(prob2))

                d2_alpha_avg = (d2_alpha_p2 + d2_alpha_p1) / 2
                alpha_diversity.append(d2_alpha_avg)

        # calculate beta diversities
        beta_diversity = np.divide(gamma_diversity, alpha_diversity)
        beta_turnover.append(calculate_turnover(beta_diversity))
        beta_sorensen.append(calculate_sorensen(beta_diversity, 0))
        beta_jaccard.append(calculate_jaccard(beta_diversity, 0))

    print("Finished calculating pairwise beta diversities for q=%s" % q)
    return (beta_turnover, beta_sorensen, beta_jaccard)