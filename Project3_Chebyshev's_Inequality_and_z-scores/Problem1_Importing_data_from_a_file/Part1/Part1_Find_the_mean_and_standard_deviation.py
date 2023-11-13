"""Find the mean and (population) standard deviation of the "Exam Score" column of our
exam_scores data frame. Store these in the variables exam_mean and exam_std ,
respectively. Then, print them out so we can see their values."""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

exam_scores = pd.read_csv('~/shared/ps3_exam_scores.csv') 
exam_scores.head() 

exam_mean = np.mean(exam_scores['Exam Score'])
exam_std = np.std(exam_scores['Exam Score'])
display(exam_mean,exam_std)