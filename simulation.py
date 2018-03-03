from simulation_init import create_species_matrix, create_temporary_pool, create_local_species_pool, sampling_func
import numpy as np

def plot_year_species(plots, years,
                      species_global_pool, global_pool, local_pool_size, temporary_pool_size,
                      recruit_rate, species_recruit_rate, species_mort_rate, death_rate, filename):

    species_matrix = create_species_matrix(plots, years, species_global_pool)
    # TODO: Think of how to include the effective pool -
    # TODO: Have a pre-code python file that shrinks the sub-sample of the global species pool
    # effective_pool = create_temporary_pool(effective_pool_size, global_pool)
    for p in range(plots):
        temp_pool = create_temporary_pool(temporary_pool_size, global_pool)
        # print("Plot %s" % p)
        # print(temp_pool)
        # # Local species pool for 1 plot
        local_pool = create_local_species_pool(plots, local_pool_size, temp_pool)
        current_species_abundance = np.zeros(species_global_pool)

        for y in range(years):
            # Create mortality probabilities per year
            # Send the trees to a better life
            if (y != 0):
                """after each species is removed, we need to recalculate the probabilities.
                   Question: Shouldn't we be sampling with replacement? To account for the dominant species dying out faster?
                """
                weights = current_species_abundance + species_mort_rate[:,y]
                # weights = species_mort_rate[:,y]
                deaths = sampling_func((global_pool[0], weights), death_rate[y], True)
                for d in deaths:
                    if (current_species_abundance[d] == 0):
                        break
                    else:
                        current_species_abundance[d] -= 1

            # TODO: Update the abundance in current_species_abundance (DONE)
            # Recruitment rate: Not affected by abundance of species in plot, but by species type and by year
            # recruit_year -> for that particular year, what are the rates of recruitment
            # print(species_recruit_rate.shape)
            recruit_year = species_recruit_rate[:, y]
            local_recruitment_rate = np.take(recruit_year, local_pool)
            recruits = sampling_func((local_pool, local_recruitment_rate), recruit_rate[y], True)
            # print("Year %s" % y)
            # print(recruits)
            for r in recruits:
                current_species_abundance[r] += 1

            for s in range(species_global_pool):
                species_matrix[p][y][s] = current_species_abundance[s]

    print("Saving species matrix to file...")
    save_simulation_results(species_matrix, filename+".csv")
    print(species_matrix.shape)
    print("Finished simulation")
    return species_matrix


def save_simulation_results(data, filename):
    with open(filename, 'wb') as outfile:
        # I'm writing a header here just for the sake of readability
        # Any line starting with "#" will be ignored by numpy.loadtxt
        # outfile.write('# Array shape: {0}\n'.format(data.shape))

        # Iterating through a ndimensional array produces slices along
        # the last axis. This is equivalent to data[i,:,:] in this case
        for data_slice in data:
            # The formatting string indicates that I'm writing out
            # the values in left-justified columns 7 characters in width
            # with 2 decimal places.
            np.savetxt(outfile, data_slice, fmt='%-7.2f')

            # Writing out a break to indicate different slices...
            # outfile.write('# New slice\n')
