""""Lehman College (part of the City University of New York system) hosts a portal for a variety of
datasets about the Bronx: https://bronx.lehman.cuny.edu.
One of these is a dataset containing information on population density. Navigate to the Bronx
Population Density page, click “Export”, right click on “CSV”, and choose “Copy link address”.
Save this URL into the data_URL string. Then, use the pd.read_csv() function to download this CSV file and save it into a data frame
called bronx_pop_density"""


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)