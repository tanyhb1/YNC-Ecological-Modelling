age, recr, mort, density = np.genfromtxt('data/mortality-recruitment.csv', delimiter=',', usecols=(1,2, 3,4), unpack=True, dtype=int)
age = age[1:]
recr_by_year = recr[1:]
mort_by_year = mort[1:]
density = density[1:]

""" Gets groups of data for mortality and recruitment """
# Store the mortality of species by group
groups = 3                                              # to be changed by user
grp_col = tuple((i) for i in range(0, groups+1))        # to be used when getting data from the table

# stores the mortality of species by groups into a dictionary
def get_data(filename, grp_col):
    group = {}
    for i in range(1, groups+1):
        group["group %s" % i] = np.genfromtxt(filename, delimiter=',', usecols=grp_col, unpack=True)
        group["group %s" % i] = group["group %s" % i][i]
    return group

group_mort = get_data('data/year-group-mort.csv', grp_col)
group_mort = OrderedDict(sorted(group_mort.items()))

group_recr = get_data('data/year-group-recr.csv', grp_col)
group_recr = OrderedDict(sorted(group_recr.items()))

species_grp_file = input("Input species group filename: ")
species_grp_file = "data/" + species_grp_file