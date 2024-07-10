import numpy as np
import pandas as pd
from scipy.stats import t

pd.set_option("display.max_columns", 30)
df = pd.read_csv("nap_no_nap.csv")

## No. of napping & non-napping kids
nap_size = len(df[df["napping"] == 1])
no_nap_size = len(df[df["napping"] == 0])

## Isolate 'night bedtime' column for those who nap and those who dont into different columns
naps = df[df["napping"] == 1]
no_naps = df[df["napping"] == 0]
bedtime_nap = naps['night bedtime']
bedtime_no_nap = no_naps['night bedtime']

## Sample Mean bedtime for nap and no_nap
nap_mean_bedtime = np.mean(bedtime_nap)
no_nap_mean_bedtime = np.mean(bedtime_no_nap)

## Standard SD bedtime for nap and no_nap
nap_std_bedtime = np.std(bedtime_nap)
no_nap_std_bedtime = np.std(bedtime_no_nap)

## Standard Error for nap and no_nap
nap_se_mean_bedtime = nap_std_bedtime / np.sqrt(nap_size)
no_nap_se_mean_bedtime = no_nap_std_bedtime / np.sqrt(no_nap_size)

## Value of t* at 95% CI
confidence_level = 0.95
nap_t_star = t.ppf((1+confidence_level) / 2, df=14)
no_nap_t_star = t.ppf((1+confidence_level) / 2, df=4)
# print(f"{nap_t_star:.3f}")
# print(f"{no_nap_t_star:.3f}")

## Confidence Interval for "naps"
ci_lb = nap_mean_bedtime - (nap_t_star * nap_se_mean_bedtime)
ci_ub = nap_mean_bedtime + (nap_t_star * nap_se_mean_bedtime)
print(f"The CI of toddlers who naps is: ({ci_lb:.4f}, {ci_ub:.4f})")

## Confidence Interval for "no naps"
ci_lb = no_nap_mean_bedtime - (no_nap_t_star * no_nap_se_mean_bedtime)
ci_ub = no_nap_mean_bedtime + (no_nap_t_star * no_nap_se_mean_bedtime)
print(f"The CI of toddlers who doesn't nap is: ({ci_lb:.4f}, {ci_ub:.4f})")