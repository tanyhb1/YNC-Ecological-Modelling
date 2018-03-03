""" GLOBAL PARAMETERS """
import numpy as np
import math
from matplotlib import pyplot as plt
from parameters import *
np.set_printoptions(threshold=np.nan)

cols = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
""" Reads logistic curves data from file """
rT, rB, rb, rxmid, rs, rxshift, mT, mB, mb, mxmid, ms, mxshift = np.genfromtxt("data/%s" % group_recr_mortalities, delimiter = ",", usecols = cols, unpack=True)

""" Getting data from read columns
    Anything that starts with r, refers to recruitment
    Anything that starts with m, refers to mortality
    T = maximum value
    B = minimum value
    b = how step-like the logistic curve is. high values give a step-like pattern
    xmid = mid-point of the logistic curve
    s = slope of the curve
    xshift = shifting the logistic curve left / right
"""
rT = rT [1:]
rB = rB [1:]
rb = rb [1:]
rxmid = rxmid [1:]
rs = rs [1:]
rxshift = rxshift [1:]

mT = mT [1:]
mB = mB [1:]
mb = mb [1:]
mxmid = mxmid [1:]
ms = ms [1:]
mxshift = mxshift [1:]

yr_recr = np.arange(year_num)
yr_mort = np.arange(year_num)
num_recr = np.zeros((len(rT), year_num))
num_mort = np.zeros((len(mT), year_num))

""" Reading data for overall density curves """
age, recr, mort, density = np.genfromtxt('data/%s' % overall_density_curves, delimiter=',', usecols=(1,2, 3,4), unpack=True, dtype=int)
age = age[1:]
recr_by_year = recr[1:]
mort_by_year = mort[1:]
density = density[1:]

""" Plotting overall density curves """
fig = plt.figure()
fig.suptitle("Recruitment and Mortality Rates for Landscape across 35 years", fontweight='bold')
ax = fig.add_subplot(111)
plt.plot(age, recr_by_year, color='r', linewidth=3.0, label='Recruitment')
plt.plot(age, mort_by_year, color='b', linewidth=3.0, label='Mortality')
ax.set_xlabel("Age", fontweight='bold', fontsize=12)
ax.set_ylabel("Recruitment and Mortality Rates", fontweight='bold', fontsize=12)
plt.legend()
plt.savefig("results/OriginalData/recr_mort_rates.png")


""" Calculation of Relative Recruitment and Mortality Rates from Parameters """
for gp in range(len(rT)):
    for i in range(len(yr_recr)):
        b = math.pow(10, rb[gp] * (rxmid[gp] - (yr_recr[i] -  rxshift[gp])))
        # print("index: %s" % i)
        # print(b)
        bf = math.pow((1 + b), rs[gp])
        num_recr[gp][i] = rB[gp] + ((rT[gp] - rB[gp]) / bf)
        m = mb[gp]
        b = math.pow(10, mb[gp] * (mxmid[gp] - (yr_mort[i] - mxshift[gp])))
        bf = math.pow((1 + b), ms[gp])
        num_mort[gp][i] = mB[gp] + ((mT[gp] - mB[gp]) / bf)
# print("Recruitment Rate of Tree Groups")
# print(num_recr)
# print("Mortality Rate of Tree Groups")
# print(num_mort)

""" Plotting to see recruitment and mortality curves"""
x = [k for k in range(year_num)]
grp1_recr = num_recr[6]
grp2_recr = num_recr[7]
grp3_recr = num_recr[3]
grp4_recr = num_recr[31]
grp5_recr = num_recr[120]
grp6_recr = num_recr[210]
grp7_recr = num_recr[300]
grp8_recr = num_recr[352]


# grp1_mort = num_mort[0]
# grp2_mort = num_mort[1]
# grp3_mort = num_mort[2]
# grp4_mort = num_mort[3]

fig = plt.figure()
fig.suptitle('Recruitment against Age', fontsize=14, fontweight='bold')
ax = fig.add_subplot(111)
plt.plot(x, grp1_recr, color='r', linewidth=3.0, label='Pioneer Species')
plt.plot(x, grp2_recr, color='r', linewidth=3.0)
plt.plot(x, grp3_recr, color='r', linewidth=3.0)
plt.plot(x, grp4_recr, color='r', linewidth=3.0)
plt.plot(x, grp5_recr, color='b', linewidth=3.0)
plt.plot(x, grp6_recr, color='b', linewidth=3.0)
plt.plot(x, grp7_recr, color='b', linewidth=3.0)
plt.plot(x, grp8_recr, color='b', linewidth=3.0, label='Non-Pioneer Species')
ax.set_xlabel("Successional Age (Years)", fontweight='bold', fontsize=12)
ax.set_ylabel("Recruitment Rate", fontweight='bold', fontsize=12)
ax.legend()
fig.savefig('results/OriginalData/Recruitment_Rates.png')

# fig = plt.figure()
# fig.suptitle('Mortality against Age', fontsize=14, fontweight='bold')
# ax = fig.add_subplot(111)
# plt.plot(x, grp1_mort, color='r', linewidth=3.0, label='Group 1')
# plt.plot(x, grp2_mort, color='g', linewidth=3.0, label='Group 2')
# plt.plot(x, grp3_mort, color='b', linewidth=2.0, label='Group 3')
# plt.plot(x, grp4_mort, color='y', linewidth=2.0, label='Group 4')
# ax.set_xlabel("Years", fontweight='bold', fontsize=12)
# ax.set_ylabel("Mortality Rates", fontweight='bold', fontsize=12)
# fig.savefig('results/OriginalData/Mortality_Rates.png')

species_num, mort_grp, recr_grp, rel_abundance = np.genfromtxt('data/%s' % species_groups, delimiter=',', usecols = (0, 1, 2, 3), skip_header=True, unpack=True, dtype=int)
# Stacks the three arrays together to form a matrix
species_mort_recr = np.vstack((species_num, mort_grp, recr_grp)).transpose()
# To make sure that I can put a sublist within a list to store the recruitment and mortalities over years
species_mort_recr = np.array(species_mort_recr, dtype=object)

sp = [i for i in range(len(species_num))]
fig = plt.figure()
ax = fig.add_subplot(111)
fig.suptitle('Relative abundance of Species in Landscape', fontsize=17, fontweight='bold')
plt.scatter(sp, rel_abundance, c='b', s=2.0)
ax.set_xlabel("Species", fontsize=15, fontweight='bold')
ax.set_ylabel("Relative Abundance", fontsize=15, fontweight='bold')
fig.savefig('results/OriginalData/Species_Relative_Abundance.png')

####### Binds the three tables together #######
# print(species_mort_recr.shape)
for s in range(len(species_num)):
    # Get which group that particular species comes from
    mort_group = species_mort_recr[s][1]
    recr_group = species_mort_recr[s][2]
    #print("mortality groups: %s" % mort_group)
    # Getting the mortalities and recruitments from the dictionary we read from file
    mortalities = num_mort[mort_group - 1]
    #print("mortalities %s" % mortalities)
    recruitments = num_recr[recr_group - 1]
    #print("recruitments %s" % recruitments)
    # Update the matrix appropriately, recruitment in index 2, and mortality in index 1 for each species
    species_mort_recr[s][1] = mortalities.reshape((1, year_num))
    species_mort_recr[s][2] = recruitments.reshape((1, year_num))

# End result: a 500 x 3 matrix of 500 species, their mortality rates over year, and recruitment rates over year

year_species_recr = np.zeros((year_num, len(species_num)))
year_species_mort = np.zeros((year_num, len(species_num)))
for y in range(year_num):
    for s in range(len(species_num)):
        # print("Recruitment")
        # print(species_mort_recr[s][1])
        year_species_recr[y][s] = species_mort_recr[s][2][0][y]
        year_species_mort[y][s] = species_mort_recr[s][1][0][y]

# print(year_species_mort[0])
# print("Matrix of 500 species, their mortality and recruitment rates over year")
# print(species_mort_recr)

""" Variables for Simulation """

""" Obtained From Data """
years = year_num
species_global_pool = len(species_num)

s = np.arange(0, species_global_pool, 1)
#p = np.arange(0, species_global_pool, 1)
p = rel_abundance
# print(p)
global_pool = (s, p)

# number tells you the number of recruits / deaths for each year
recruit_rate = recr_by_year
species_recruit_rate = year_species_recr.T
# print("SPECIES RECRUIT RATE")
# print(species_recruit_rate)
species_mort_rate = year_species_mort.T
# print("SPECIES MORTALITY RATE")
# print(species_mort_rate)
death_rate = mort_by_year
