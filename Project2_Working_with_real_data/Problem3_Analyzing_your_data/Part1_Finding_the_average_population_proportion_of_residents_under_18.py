"""To find the average value value of a column in a dataframe, you can use the command
np.mean(my_data_frame['my_col']) , which uses numpy to find the average value of the
column "my_col" in the data frame my_data_frame . Find the average value of the "Pop. prop. under 18" column in the bronx_pop_density data
frame"""


import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl

data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

bronx_pop_density['Pop. prop. under 18'] = bronx_pop_density["Pop. Under 18"]/bronx_po
display(bronx_pop_density[["Zipcode", "Total Population 2010", "Pop. Under 18","Pop. prop. under 18"]])
np.mean(bronx_pop_density['Pop. prop. under 18'])