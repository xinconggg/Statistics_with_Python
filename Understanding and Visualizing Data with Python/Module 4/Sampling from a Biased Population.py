import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

''' Given Data '''
# Parameters to recreate the simulations from the video 
mean_nogym = 155
sd_nogym = 5
mean_gym = 185 
sd_gym = 5 
gymperc = .3
popSize = 40000

# Create the two subpopulations
nogym = np.random.normal(mean_nogym, sd_nogym, int(popSize * (1 - gymperc)))
gym = np.random.normal(mean_gym, sd_gym, int(popSize * (gymperc)))

# Create the total population from the subpopulations
all_students = np.concatenate((nogym, gym))
gym_01 = np.concatenate((np.zeros(len(nogym)), np.ones(len(gym))))
df = pd.DataFrame({"weight": all_students, "gym": gym_01})


''' Histogram: Weight '''
# # Non-gym Goers
# sns.displot(df[df["gym"]==0], x="weight", kde=True)
# plt.title("Non Gym Goers only")
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()

# # Gym Goers
# sns.displot(df[df["gym"]==1], kde=True, x="weight")
# plt.title("Gym Goers only")
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()

# # Overall Population
# sns.displot(df, kde=True, x="weight")
# plt.title("Overall Population")
# plt.axvline(x=np.mean(df["weight"]), color="red") # Create a mean line
# plt.grid(True)
# plt.xlim([140, 200])
# plt.show()

''' Sample from the entire population '''
# Simulation parameters
numberSamps = 5000
sampSize = 50

# Get the sampling distribution of the mean form only the gym
mean_distribution = np.empty(numberSamps) # Create a np array with size equal to "numberSamps"
for i in range(numberSamps):
    student_sample = np.random.choice(df["weight"], sampSize)
    mean_distribution[i] = np.mean(student_sample)

# # Plot Distribution sample
# sns.histplot(mean_distribution)
# plt.axvline(x=np.mean(df["weight"]), color="red")
# plt.grid(True)
# plt.xlabel("Weight")
# plt.xlim([140,200])
# plt.show()

''' Non-representative sample '''
# Simulation parameters
numberSamps = 5000
sampSize = 50

# Get the sampling distribution of the mean form only the gym
biased_mean_distribution = np.empty(numberSamps)
db = df[df["gym"]==1]
for i in range(numberSamps):
    student_sample = np.random.choice(db["weight"], sampSize)
    biased_mean_distribution[i] = np.mean(student_sample)

# Plot Distribution sample
sns.histplot(biased_mean_distribution)
plt.axvline(x=np.mean(df["weight"]), color="red")
plt.axvline(x=np.mean(biased_mean_distribution), color="blue")
plt.grid(True)
plt.xlabel("Weight")
plt.xlim([140,200])
plt.show()
