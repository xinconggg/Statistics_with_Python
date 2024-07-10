import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(1738)
mu = 7 # Mean of population
sigma = 1.7 # SD of population

# Generate a large set of random observations
observations = np.random.normal(mu, sigma, size=100000)

''' Empirical '''
sns.displot(observations)
# 68%
plt.axvline(np.mean(observations) + np.std(observations), color = "g")
plt.axvline(np.mean(observations) - np.std(observations), color = "g")
# 95%
plt.axvline(np.mean(observations) + (2* np.std(observations)), color = "y")
plt.axvline(np.mean(observations) - (2* np.std(observations)), color = "y")
# 99.7%
plt.axvline(np.mean(observations) + (3* np.std(observations)), color = "b")
plt.axvline(np.mean(observations) - (3* np.std(observations)), color = "b")
plt.show()

