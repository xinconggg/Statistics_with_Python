import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Given variables
r = 0.5
mean = [15, 5]
cov = [[1, r], [r, 1]]
x, y = np.random.multivariate_normal(mean, cov, 400).T

# ## Plot Histogram
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.hist(x=x, bins=15)
# plt.title("X")

# plt.subplot(1,2,2)
# plt.hist(x=y, bins=15)
# plt.title("Y")
# plt.show()

## Plot Scatterplot
# Joint Marginal Distribution of X and Y
plt.figure(figsize=(10,10))
plt.subplot(2,2,2)
plt.scatter(x=x,y=y)
plt.title("Joint Distribution of X and Y")
# Marginal Distribution of X
plt.subplot(2,2,4)
plt.hist(x=x, bins=15)
plt.title("Marginal Distribution of X")
# Marginal Distribution of Y
plt.subplot(2,2,1)
plt.hist(x=y, orientation="horizontal", bins=15)
plt.title("Marginal Distribution of Y")

plt.show()
