import numpy as np # the "as np" command allows us to use the abbreviation "np"
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


data_URL = "~/shared/2015_Street_Tree_Census_-_Tree_Data.csv"
tree_df = pd.read_csv(data_URL)
display(tree_df.head(5))