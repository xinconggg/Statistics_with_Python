import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
import statsmodels.api as sm
from sklearn.datasets import load_diabetes

df_dataset = load_diabetes()
df = pd.DataFrame(data=df_dataset.data, columns=df_dataset.feature_names)

''' Fit a Linear Regression model and Output the model summary '''
m0 = sm.OLS.from_formula("s6 ~ age + sex + bmi", df)
r0 = m0.fit()
# print(r0.summary())

''' Determine what would happen to the R-squared value when the predictor "bp" is added to the initial model '''
model = sm.OLS.from_formula("s6 ~ age + sex + bmi + bp", data=df)
result = model.fit()
# print(result.summary())

''' Generate a Logistics Regression and Output the model summary '''
da = pd.read_csv("../nhanes_2015_2016.csv")
da["RIAGENDRx"] = da.RIAGENDR.replace({1: "Male", 2: "Female"})
da["smq"] = da.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
da["DMDEDUC2x"] = da.DMDEDUC2.replace({1: "lt9", 2: "x9_11", 3: "HS", 4: "SomeCollege",
                                      5: "College", 7: np.nan, 9: np.nan})
model = sm.GLM.from_formula("smq ~ RIAGENDRx + RIDAGEYR + DMDEDUC2x", family=sm.families.Binomial(), data=da)
result = model.fit()
print(result.summary())