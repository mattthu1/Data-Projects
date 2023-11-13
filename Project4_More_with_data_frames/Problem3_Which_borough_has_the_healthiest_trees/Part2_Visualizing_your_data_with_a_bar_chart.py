

import numpy as np # the "as np" command allows us to use the abbreviation "np"
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


data_URL = "~/shared/2015_Street_Tree_Census_-_Tree_Data.csv"
tree_df = pd.read_csv(data_URL)


manhattan_num_trees = len(tree_df[tree_df['borocode'] == 1]) # tree_df[tree_df[
staten_island_num_trees = len(tree_df[tree_df['borocode'] == 5])
brooklyn_num_trees = len(tree_df[tree_df['borocode'] == 3])
queens_num_trees = len(tree_df[tree_df['borocode'] == 4])
bronx_num_trees = len(tree_df[tree_df['borocode'] == 2])
total_trees = bronx_num_trees + queens_num_trees +brooklyn_num_trees +staten_island_num_trees + manhattan_num_trees


print(f"There are {manhattan_num_trees} trees in Manahattan.")
print(f"There are {bronx_num_trees} trees in The Bronx.")
print(f"There are {brooklyn_num_trees} trees in Brooklyn.")
print(f"There are {queens_num_trees} trees in Queens.")
print(f"There are {staten_island_num_trees} trees in Staten Island.")
print(f"There are a total of {total_trees} in all of NYC in 2015")


manhattan_good_health = len(tree_df[(tree_df['borocode'] == 1) & (tree_df['health'] == 'Good')])
bronx_good_health = len(tree_df[(tree_df['borocode'] == 2) & (tree_df['health'] == 'Good')])
brooklyn_good_health = len(tree_df[(tree_df['borocode'] == 3) & (tree_df['health'] == 'Good')])
queens_good_health = len(tree_df[(tree_df['borocode'] == 4) & (tree_df['health'] == 'Good')])
staten_island_good_health = len(tree_df[(tree_df['borocode'] == 5) & (tree_df['health'] == 'Good')])

data = {'Manhattan':manhattan_good_health,
 'The Bronx':bronx_good_health,
 'Brooklyn':brooklyn_good_health,
 'Queens':queens_good_health,
 'Staten Island':staten_island_good_health}
boroughs = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(boroughs, values, color ='maroon', width = 0.4)
plt.xlabel("Borough")
plt.ylabel("Percent of Trees that are Healthy")
plt.title("Tree Health by NYC Borough")
plt.show()