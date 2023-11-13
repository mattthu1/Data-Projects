"""Create a new column in data frame exam_scores called "z-score", and then set the value of
this column to the -score of the exam score of that row."""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

exam_scores = pd.read_csv('~/shared/ps3_exam_scores.csv') 
exam_scores.head() 

exam_mean = np.mean(exam_scores['Exam Score'])
exam_std = np.std(exam_scores['Exam Score'])

exam_scores['z-score'] = (exam_scores['Exam Score']- exam_mean) /exam_std

display(exam_scores)