import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 


data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

display(bronx_pop_density)