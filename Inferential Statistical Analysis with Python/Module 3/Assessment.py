import numpy as np
import pandas as pd
from scipy.stats import t, ttest_ind
import scipy.stats.distributions as dist
pd.set_option("display.max_columns", 30)

df = pd.read_csv("../nap_no_nap.csv")

## Convert 'night bedtime' into decimalized time
df.loc[:,'night bedtime'] = np.floor(df['night bedtime'])*60 + np.round(df['night bedtime']%1,2 )*100

## Separate to those who naps & those who doesn't
nap = df[df["napping"] == 1]
no_nap = df[df["napping"] == 0]

## Size of those who naps & those who doesn't
nap_size = len(nap)
no_nap_size = len(no_nap)

## Isolate the column "night bedtime" for those who nap into a new variable, and those who didn't nap into another new variable. 
nap_bedtime = nap["night bedtime"]
no_nap_bedtime = no_nap["night bedtime"]

## Sample Mean Bedtime for nap & no_nap
nap_mean_bedtime = nap_bedtime.mean()
no_nap_mean_bedtime = no_nap_bedtime.mean()

## Sample SD for nap & no_nap
nap_sd_bedtime = nap_bedtime.std()
no_nap_sd_bedtime = no_nap_bedtime.std()

## SE of nap & no_nap
pooled_se = np.sqrt((((nap_size - 1) * nap_sd_bedtime ** 2) + ((no_nap_size - 1) * no_nap_sd_bedtime ** 2)) / (nap_size + no_nap_size - 2) * (1 / nap_size + 1 / no_nap_size))

## Degrees of Freedom
deg_f = nap_size + no_nap_size - 2

''' 1st Hypothesis Test '''
## t-test statistic 
t_stat_1 = (nap_mean_bedtime - no_nap_mean_bedtime) / pooled_se
## p-value
p_value_1 = dist.norm.cdf(-np.abs(t_stat_1))
print(p_value_1)

''' 2nd Hypothesis Test '''
t_stat_2, p_value_2 = ttest_ind(nap_bedtime, no_nap_bedtime, equal_var=True)
print(p_value_2)
