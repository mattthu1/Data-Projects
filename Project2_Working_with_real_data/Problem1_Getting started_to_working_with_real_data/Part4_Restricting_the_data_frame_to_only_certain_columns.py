""""Because data frames can contain so much information, and you may only want to work with a
subset of that data, it's useful to be able to restrict a data frame to certain columns or rows.
In the bronx_pop_density data frame, output only the columns "Zipcode," "Total Population
2010," and "Pop. Under 18"""


import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl

data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

display(bronx_pop_density[["Zipcode", "Total Population 2010", "Pop. Under 18"]])