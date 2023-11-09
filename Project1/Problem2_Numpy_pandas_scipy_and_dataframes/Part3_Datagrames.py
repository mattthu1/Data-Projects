"""A pandas dataframe is, in short, very similar to a spreadsheet. Dataframes are 2D arrays that can
have titles and headers for rows and columns. We will have a slow introduction to dataframes over
the next few problem sets. Introduce a new variable called fave_numbers_df that is the dataframe
version of the fave_numbers list. Print both so you can see how similar and different they are
when we view it."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


fave_numbers = [1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
fave_numbers_df = pd.DataFrame(fave_numbers) 

print(f"This is the simple list: \n {fave_numbers} \n")
print(f"This is the dataframe (notice it shows the column/row like a spreadsheet: \n {fave_numbers_df} ")