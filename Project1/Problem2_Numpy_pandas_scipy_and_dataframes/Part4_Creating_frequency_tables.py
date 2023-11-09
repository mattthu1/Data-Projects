""""Create a frequency table with 5 groups/bins for fave_numbers_df . It does not need to be
formatted in any specific way - we simply need to see the frequency of each data value."""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
fave_numbers = [1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
fave_numbers_df = pd.DataFrame(fave_numbers, columns=['Number'])



bins = [0, 1, 2, 3, 4, 5]
frequency_table = pd.cut(fave_numbers_df['Number'], bins=bins).value_counts().sort_index()

print("Frequency Table:")
print(frequency_table)