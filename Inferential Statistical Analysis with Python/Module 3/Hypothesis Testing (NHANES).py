import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats.distributions as dist

df = pd.read_csv("../../nhanes_2015_2016.csv")

df["SMQ020x"] = df.SMQ020.replace({1: "Yes", 2: "No", 7: np.nan, 9: np.nan})  
df["RIAGENDRx"] = df.RIAGENDR.replace({1: "Male", 2: "Female"})
df["DMDCITZNx"] = df.DMDCITZN.replace({1: "Yes", 2: "No", 7: np.nan, 9: np.nan})

''' Hypothesis Tests for Single Proportions '''
## Imagine that the rate of lifetime smoking in another country was known to be 40%, and we wished to assess whether the rate of lifetime smoking in the US were different from 40%.
x = df["SMQ020x"].dropna() == "Yes"
p = x.mean()
se = np.sqrt(0.4 * 0.6 / len(x))
test_stat = (p - 0.4) / se
pvalue = 2 * dist.norm.cdf(-np.abs(test_stat))
# print(test_stat, pvalue)

## Print Test Statistic & p-value
# print(sm.stats.proportions_ztest(x.sum(), len(x), 0.4)) # Normal approximation with estimated proportion in SE
# print(sm.stats.proportions_ztest(x.sum(), len(x), 0.4, prop_var=0.4)) # Normal approximation with null proportion in SE
# print(sm.stats.binom_test(x.sum(), len(x), 0.4)) # Exact binomial p-value

''' Hypothesis Tests for Two Proportions '''
## Compare the smoking rates between females and males. Since smoking rates vary strongly with age, we do this in the subpopulation of people between 20 and 25 years of age.
dx = df[["SMQ020x", "RIDAGEYR", "RIAGENDRx"]].dropna()
dx = dx.loc[(dx["RIDAGEYR"] >= 20) & (dx["RIDAGEYR"] <= 25)] # People between 20 and 25 year old

# Summarize the data by calculating the proportion of yes responses and the sample size
p = dx.groupby("RIAGENDRx")["SMQ020x"].agg([lambda z: np.mean(z=="Yes"), "size"])
p.columns = ["Smoke", "N"]

# Pooled Rate of yes responses and the SE of the estimated difference of proportionsm
p_comb = (dx["SMQ020x"]=="Yes").mean()
va = p_comb * (1-p_comb)
se = np.sqrt(va * (1/p.N.Female + 1 / p.N.Male))

# Calculate the test statistic and p-value
test_stat = (p.Smoke.Female - p.Smoke.Male) / se
pvalue = 2*dist.norm.cdf(-np.abs(test_stat))
# print(test_stat, pvalue)

''' Hypothesis Tests Comparing Means '''
dx = df[["BMXBMI", "RIDAGEYR", "RIAGENDRx"]].dropna()
df["agegrp"] = pd.cut(df.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
df.groupby(["agegrp", "RIAGENDRx"])["BMXBMI"].agg(np.std).unstack()

for k, v in df.groupby("agegrp"):
    bmi_female = v.loc[v.RIAGENDRx=="Female", "BMXBMI"].dropna()
    bmi_female = sm.stats.DescrStatsW(bmi_female)
    bmi_male = v.loc[v.RIAGENDRx=="Male", "BMXBMI"].dropna()
    bmi_male = sm.stats.DescrStatsW(bmi_male)
    # print(k)
    # print("pooled: ", sm.stats.CompareMeans(bmi_female, bmi_male).ztest_ind(usevar='pooled'))
    # print("unequal:", sm.stats.CompareMeans(bmi_female, bmi_male).ztest_ind(usevar='unequal'))
    # print()

''' Paired Test '''
dx = df[["BPXSY1", "BPXSY2"]].dropna()
db = dx.BPXSY1 - dx.BPXSY2
sm.stats.ztest(db)

dx = df[["RIAGENDRx", "BPXSY1", "BPXSY2", "RIDAGEYR"]].dropna()
dx["agegrp"] = pd.cut(dx.RIDAGEYR, [18, 30, 40, 50, 60, 70, 80])
for k, g in dx.groupby(["RIAGENDRx", "agegrp"]):
    db = g.BPXSY1 - g.BPXSY2
    print(k) # Stratum Definition
    print(db.mean()) # Mean Difference
    print(db.size) # Sample Size
    print(sm.stats.ztest(db.values, value=0)) #Test statistic, p-value
