"""Make a histogram for the "Exam Scores" column with
6 bins,
title it "Exam Performance",
label the horizontal axis "Exam Score",
and label the vertical axis "Number of Students"."""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

exam_scores = pd.read_csv('~/shared/ps3_exam_scores.csv') 
exam_scores.head() 

exam_mean = np.mean(exam_scores['Exam Score'])
exam_std = np.std(exam_scores['Exam Score'])

exam_scores['z-score'] = (exam_scores['Exam Score']- exam_mean) /exam_std


plt.hist(exam_scores['Exam Score'],bins=6)
plt.title("Exam Performance")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")