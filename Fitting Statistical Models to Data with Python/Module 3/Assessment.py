import numpy as np
import statsmodels.api as sm
import pandas as pd  

df = pd.read_csv("../nhanes_2015_2016.csv")

''' Drop unused columns & drop rows with missing values '''
useful_columns = ["BPXSY1", "RIDAGEYR", "RIAGENDR", "RIDRETH1", "DMDEDUC2", "BMXBMI",
        "SMQ020", "SDMVSTRA", "SDMVPSU"]
df = df[useful_columns].dropna()
## Define "group" & "smq"
df["group"] = 10*df.SDMVSTRA + df.SDMVPSU
df["smq"] = df.SMQ020.replace({2: 0, 7: np.nan, 9: np.nan})
## Generate random seed
np.random.seed(123)

''' Determine Correlation of all features '''
for v in ["BPXSY1", "SDMVSTRA", "RIDAGEYR", "BMXBMI", "smq"]:
    model = sm.GEE.from_formula(v + " ~ 1", groups="group",
           cov_struct=sm.cov_struct.Exchangeable(), data=df)
    result = model.fit()
    print(v, result.cov_struct.summary())