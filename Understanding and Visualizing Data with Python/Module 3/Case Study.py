import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("nhanes_2015_2016.csv")

'''Quantitative Bivariate Data'''
# # Scatterplot
# sns.regplot(data=df, x="BMXLEG", y="BMXARML", fit_reg=False, scatter_kws={"alpha":0.2})
# plt.show()

# #  Density Plot
# p = sns.jointplot(data=df, x='BMXLEG', y="BMXARML", kind="kde")
# r = df[["BMXLEG","BMXARML"]].corr().iloc[0:1]
# p.ax_joint.annotate(f"r={0:.2f}", xy=(0.1,0.9), xycoords="axes fraction", size=20)
# plt.show()

'''Heterogeneity and Stratification'''
# # Facet Grid
# df["RIAGENDR"] = df["RIAGENDR"].replace({1:"Male", 2:"Female"})
# sns.FacetGrid(df, col="RIAGENDR", height=5).map(sns.scatterplot, "BMXLEG", "BMXARML", alpha=0.4).add_legend()
# plt.show()

# Find correlation between leg and arm length of both Male & Female
print(df.loc[df["RIAGENDR"]=="Male", ["BMXLEG","BMXARML"]].dropna().corr())
print(df.loc[df["RIAGENDR"]=="Female", ["BMXLEG","BMXARML"]].dropna().corr())


