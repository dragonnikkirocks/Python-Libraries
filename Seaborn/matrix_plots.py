import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.sql import DatabaseError
import seaborn as sns


#bar plot
print(sns.get_dataset_names())

tips_df = sns.load_dataset('tips')
crash_df = sns.load_dataset('car_crashes')



plt.figure(figsize=(8,4))
sns.set_context('paper',font_scale=1.4)

#data has to be in matrix formate
#1. correlation of data - in matrix 
crash_mx= crash_df.corr()
print(crash_mx)

sns.heatmap(crash_mx, annot=True,cmap='Blues')
plt.show()

flights_df = sns.load_dataset('flights')
flights_df= flights_df.pivot_table(index='month',columns='year',values='passengers')
sns.heatmap(flights_df,cmap='Blues',linecolor='white',linewidth=2)
plt.show()

