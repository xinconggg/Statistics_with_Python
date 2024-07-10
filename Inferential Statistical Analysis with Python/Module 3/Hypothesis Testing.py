import statsmodels.api as sm
import numpy as np 
import pandas as pd
import scipy.stats.distributions as dist

''' Single Population Proportion Test '''
## Example: In previous years 52% of parents reported a belief that social media is the cause of their teenager’s lack of sleep. 
## Do more parents today believe that their teenager’s lack of sleep is caused by social media?

# Population: Parents with a teenager (age 13-18)
# Parameter of Interest: p
# Null Hypothesis: p = 0.52
# Alternative Hypthosis: p > 0.52 (note that this is a one-sided test)

# We interview 1018 parents (who constitute an IID sample from the population of interest), and 56% of these parents report that they believe that 
# their teenager’s lack of sleep is caused by social media.

n = 1018 # Population
pnull = 0.52 # Null Hypothesis
phat = 0.56 # Population Proportion
# print(sm.stats.proportions_ztest(phat * n, n, pnull, alternative='larger', prop_var=0.52)) # Returns z-statistic & p-value

''' Two Population Proportion Test '''
## Is there a difference between the population proportions of parents of Black children and parents of Hispanic children who report that their child has ever had swimming lessons?

# Populations: All parents of Black children age 6-18 and all parents of Hispanic children age 6-18
# Parameter of Interest: p1 - p2, where p1 and p2 are the Black and Hispanic proportions, respectively
# Null Hypothesis: p1 - p2 = 0
# Alternative Hypthosis: p1 - p2 ≠ 0

# 91 out of 247 (36.8%) sampled parents of Black children report that their child has had some swimming lessons.
# 120 out of 308 (38.9%) sampled parents of Hispanic children report that their child has had some swimming lessons.

# print(sm.stats.test_proportions_2indep(91, 247, 120 , 308)) # Returns z-statistic & p-value

''' Single Population Mean Test '''
## Research Question: Is the average cartwheel distance (in inches) for adults more than 80 inches?

# Population: All adults
# Parameter of Interest: 𝜇, population mean cartwheel distance
# Null Hypothesis: 𝜇 = 80
# Alternative Hypthosis: 𝜇 > 80

# We observe data from a sample of 25 adults, who have a sample mean of 82.46 and a sample standard deviation of 15.06. 
# Note that the hypothesized mean of 80 is considered to be an exact value not an estimate from a dataset which would have uncertainty associated with it.

df = pd.read_csv("../../Cartwheeldata.csv")

# print(sm.stats.ztest(df["CWDistance"], value = 80, alternative = 'larger')) # Null Hypothesis = 80, Alternative Hypothesis > 80

''' Difference between 2 Population Means Test '''
## Research Question: Considering adults in the NHANES data, do males have greater mean Body Mass Index than females?

# Population: Adults in the NHANES data.
# Parameter of Interest: 𝜇1 − 𝜇2, Body Mass Index
# Null Hypothesis: 𝜇1 = 𝜇2
# Alternative Hypthosis: 𝜇1 ≠ 𝜇2
 
# After we collect our data, we find the following sample means and sample standard deviations:
# 2976 Females, 𝜇1=29.94
# 𝜎1=7.75

# 2759 Male Adults, 𝜇2=28.78
#  𝜎2=6.25
 
# 𝜇1 − 𝜇2=1.16

df = pd.read_csv("../../nhanes_2015_2016.csv")

females = df[df["RIAGENDR"] == 2]
males = df[df["RIAGENDR"] == 1]
print(sm.stats.ztest(females["BMXBMI"].dropna(), males["BMXBMI"].dropna()))