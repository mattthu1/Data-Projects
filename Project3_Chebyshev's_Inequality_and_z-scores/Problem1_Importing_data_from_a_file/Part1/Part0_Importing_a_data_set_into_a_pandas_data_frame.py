"""Execute the cell below, which uses the pd.read_csv() function to read in
ps3_exam_scores.csv file and save it into a data frame called exam_scores . Then, it uses
the head() attribute to look at the first few rows of your data frame."""


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

exam_scores = pd.read_csv('~/shared/ps3_exam_scores.csv') 
exam_scores.head() 