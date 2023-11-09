#Find the sample and population standard deviation.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
fave_numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5]

print(np.std(fave_numbers,ddof=0))
print(np.std(fave_numbers, ddof=1))