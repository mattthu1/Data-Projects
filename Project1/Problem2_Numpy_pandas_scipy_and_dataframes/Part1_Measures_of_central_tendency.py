#Find the mean, median, and mode of fave_numbers using built-in functions.

fave_numbers = [1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats




fave_numbers = [1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
print(np.mean(fave_numbers))
print(np.median(fave_numbers))
print(stats.mode(fave_numbers))