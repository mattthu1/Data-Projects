"""Execute the cell below so you can see the "Zipcode," "Total Population 2010," "Pop. Under 18",
and "Pop. prop. under 18" columns, and that all of its values of your new column are indeed
None ."""


import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl
data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

bronx_pop_density['Pop. prop. under 18'] = bronx_pop_density["Pop. Under 18"] / bronx_pop_density["Total Population 2010"]

display(bronx_pop_density[["Zipcode", "Total Population 2010", "Pop. Under 18","Pop. prop. under 18"]])