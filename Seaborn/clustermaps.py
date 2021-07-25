import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.sql import DatabaseError
import seaborn as sns

iris = sns.load_dataset("iris")
sns.PairGrid(iris)
sns.scatterplot()
plt.show()

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="sex", row="time", margin_titles=True, despine=False)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total bill", "Tip")
g.fig.subplots_adjust(wspace=0, hspace=0)
plt.show()
for (row_val, col_val), ax in g.axes_dict.items():
    if row_val == "Lunch" and col_val == "Female":
        ax.set_facecolor(".95")
    else:
        ax.set_facecolor((0, 0, 0, 0))

grd = sns.PairGrid(data=iris)
grd.map_diag(sns.distplot)
grd.map_upper(plt.scatter)
grd.map_lower(sns.kdeplot)
