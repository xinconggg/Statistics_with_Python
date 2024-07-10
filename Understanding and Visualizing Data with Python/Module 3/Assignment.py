import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Cartwheeldata.csv")

'''Scatterplot'''
# ## Scatterplot: "Height" vs "Wingspan"
# sns.scatterplot(x=df["Height"], y=df["Wingspan"], hue=df["Gender"])
# plt.xlabel("Height")
# plt.ylabel("Wingspan")
# plt.title("Relationship between Height & Wingspan")
# plt.show()

# ## Scatterplot: "Wingspan" vs "CWDistance"
# sns.scatterplot(x=df["Wingspan"], y=df["CWDistance"], hue=df["Gender"])
# plt.xlabel("Wingspan")
# plt.ylabel("Cartwheel Distance")
# plt.title("Relationship between Wingspan & Cartwheel Distance")
# plt.show()

'''Barplot'''
## Barplot: "Glasses" vs "CWDistance"
sns.barplot(x=df["Glasses"],y=df["CWDistance"], hue=df["Gender"])
plt.xlabel("Glasses")
plt.ylabel("Cartwheel Distance")
plt.title("Relationship between Glasses & Cartwheel Distance")
plt.show()

'''Basic Statistics of "CWDistance" & "Wingspan"'''
# print(df["CWDistance"].describe())
# print(df["Wingspan"].describe())
