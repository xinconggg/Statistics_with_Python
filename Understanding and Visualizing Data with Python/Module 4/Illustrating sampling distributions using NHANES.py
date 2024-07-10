import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../nhanes_2015_2016.csv")

''' Sampling Distribution of Mean '''
m = 100 # Subsample size
sbp_diff = [] # Storage for subsample mean difference

for i in range(1000):
    dx = df.sample(2*m) # Need 2 subsamples of size m
    dx1 = dx.iloc[0:m, : ] # 1st Subsample
    dx2 = dx.iloc[m: , : ] # 2nd Subsample
    sbp_diff.append(dx1["BPXSY1"].mean() - dx2["BPXSY1"].mean())

# sns.displot(sbp_diff)
# plt.show()
# print(pd.Series(sbp_diff).describe())

''' Sampling Distribution of Correlation Coefficient '''
for m in 100, 400: # m == subsample size
    sbp_diff = []
    for i in range(1000):
        dx=df.sample(2*m)
        dx1 = dx.iloc[0:m, : ]
        dx2 = dx.iloc[m: , : ]
        r1 = dx1.loc[:, ["BPXSY1", "BPXDI1"]].corr().iloc[0,1]
        r2 = dx2.loc[:, ["BPXSY1", "BPXDI1"]].corr().iloc[0,1]
        sbp_diff.append(r1 - r2)

# sns.displot(df["BPXSY1"].dropna())
# plt.show()