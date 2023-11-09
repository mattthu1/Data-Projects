"""The display() function is useful, but can display almost too much information. Sometimes,
you just want to see how the data frame is structured: the columns and maybe the first few
rows.
Use the head() attribute of a data frame to display only the first 5 rows."""



import numpy as np # the "as np" command allows us to use the abbreviation "np" when r
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats # isntead of importing the entire scipy package, we import onl

data_URL = "https://bronx.lehman.cuny.edu/api/views/2q3n-mzjq/rows.csv?accessType=DOWNLOAD"
bronx_pop_density = pd.read_csv(data_URL)

display(bronx_pop_density.head(5))