"""It's often useful to add a column to a data frame. The code block below is a
Create a new column in the bronx_pop_density data frame called "Pop. prop. under 18",
which stands for population proportion of residents under 18, and set all the initial values to
None , which means the column does not contain any data (yet)"""


import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl

data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

bronx_pop_density['Pop. prop. under 18'] = None
columns_to_display = ['Zipcode', 'Total Population 2010', 'Pop. Under 18', 'Pop. prop. under 18']

display(bronx_pop_density[['Zipcode', 'Total Population 2010', 'Pop. Under 18', 'Pop. prop. under 18']])