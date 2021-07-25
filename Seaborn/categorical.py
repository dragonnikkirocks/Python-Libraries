import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.sql import DatabaseError
import seaborn as sns


#bar plot
print(sns.get_dataset_names())

tips_df = sns.load_dataset('tips')
crash_df = sns.load_dataset('car_crashes')

sns.barplot(x='sex',y ='total_bill', data= tips_df,estimator= np.mean)
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips_df,  hue='sex')
plt.legend(loc=0)
plt.show()

#violinplot - uses kde estimation of datapoints to create the plots - box+ kde
sns.violinplot(x='day',y='total_bill',data=tips_df,  hue='sex')
plt.legend(loc=0)
plt.show()

#scatterplot with one variable is categorically
sns.stripplot(x='day',y='total_bill',data=tips_df,hue='sex',dodge=True)
plt.legend(loc=0)
plt.show()

#swarm - kind of like a strip plot and violin plot combination
sns.swarmplot(x='day',y='total_bill',data=tips_df,hue='sex',dodge=True, palette= 'magma')
plt.legend(loc=3)
plt.show()

