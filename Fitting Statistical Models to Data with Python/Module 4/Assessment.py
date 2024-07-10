import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set a random seed for repeated computation
np.random.seed(123)

# Global constants - these are what we need to change
# This is my initial belief about the mean of the average IQ score on campus
prior_sigma = 10  # my uncertainty about the mean
prior_mean = 100  # my initial belief about the mean
sigma_observations = 3  # uncertainty in my observations

# New observations - We are going to be updating this list to see how observing
# different data changes our beliefs about the average IQ score
new_data = [110, 110, 110, 125 ,125]

# Compute some statistics on the new data
n = len(new_data)

# Some hairy math to avoid doing integrals (Wikipedia has the math!)
if n != 0:
    posterior_mean = ((1 / prior_sigma ** 2) + n / sigma_observations ** 2) ** (-1) * ((prior_mean / prior_sigma ** 2) + sum(new_data) / sigma_observations ** 2)
    posterior_sd = (1 / prior_sigma ** 2 + n / sigma_observations ** 2) ** (-1)
else:
    posterior_mean = prior_mean
    posterior_sd = prior_sigma

# Plot the distribution of the prior and the posterior
x = np.linspace(50, 150, 100)
plt.plot(x, norm.pdf(x, prior_mean, prior_sigma), color="blue")
plt.plot(x, norm.pdf(x, posterior_mean, posterior_sd), color="red", linestyle='--')
plt.title("Red = Posterior, Blue = Prior")

plt.show()
print(posterior_mean)
print(posterior_sd)