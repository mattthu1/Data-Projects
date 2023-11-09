"""Now that we've created a new column called "Pop. prop. under 18," we want to fill that column
with specific values.
Update values the of this column to contain the proportion (fraction) of the population that is
under 18 (the values should be between 0 and 1). For example, if the "Total Population 2010"
value is 98, and the "Pop. Under 18" value is 23, the "Pop. prop. under 18" value should be
23/98 ≈ 0.235"""


import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl
data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

bronx_pop_density['Pop. prop. under 18'] = bronx_pop_density["Pop. Under 18"] / bronx_pop_density["Total Population 2010"]

