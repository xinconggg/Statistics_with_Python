import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

df = pd.read_csv("../../nhanes_2015_2016.csv")

''' Restrict the sample to women between 35 and 50, then use the marital status variable DMDMARTL to partition this sample into two groups - 
women who are currently married, and women who are not currently married. 
Within each of these groups, calculate the proportion of women who have completed college. 
Calculate 95% confidence intervals for each of these proportions. '''      
## Women between 35 & 50
women = df[((df["RIDAGEYR"] >= 35) & (df["RIDAGEYR"] <= 50)) & (df["RIAGENDR"] == 2)]
## Women who are married & un-married
married = women[women["DMDMARTL"] == 1]
unmarried = women[women["DMDMARTL"] != 1]
## Married & completed college & above
married_college = married["DMDEDUC2"] == 5
p_hat_married = np.mean(married_college)
married_sample_size = np.size(married_college)
## Unmarried & completed college & above
unmarried_college = unmarried["DMDEDUC2"] == 5
p_hat_unmarried = np.mean(unmarried_college)
unmarried_sample_size = np.size(unmarried_college)
## Compute confidence interval
z_multiplier = scipy.stats.norm.ppf(q = 0.95)
married_standard_error = np.sqrt(p_hat_married * (1 - p_hat_married) / married_sample_size)
ci_married_lb = p_hat_married - z_multiplier * married_standard_error
ci_married_ub = p_hat_married + z_multiplier * married_standard_error
# print(f"The 95% confidence interval for the proportion of married women who completed college is: ({ci_married_lb:.2f}, {ci_married_ub:.2f})")
