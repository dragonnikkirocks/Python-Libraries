import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.sql import DatabaseError
import seaborn as sns

print(sns.get_dataset_names())

crash_df = sns.load_dataset('car_crashes')
print(crash_df.head(5))

#Distribution plot- for univariant distributions
sns.distplot(crash_df['not_distracted'],kde=False, bins= 15)
plt.show()

#Joint plot - to compare two dists - scatterplot by default
#kde- KDE Plot described as Kernel Density Estimate is used for visualizing the Probability Density of a continuous variable.
#It depicts the probability density at different values in a continuous variable.
sns.jointplot(x='speeding', y = 'alcohol', data= crash_df,kind='kde')
plt.show()


#kde plot
sns.kdeplot(crash_df['alcohol'])
plt.show()

#pairplot - plots relation with all variables
sns.pairplot(crash_df,hue='no_previous', palette='Blues')
plt.show()

#rugplot- values are denser where more counts is present

sns.set_style('white') #darkgrid, whitegrid, dark, ticks are options
plt.figure(figsize=(8,8))
sns.set_context('paper', font_scale=1.4)
sns.jointplot(x='speeding', y = 'alcohol', data= crash_df,kind='reg')
plt.show()


