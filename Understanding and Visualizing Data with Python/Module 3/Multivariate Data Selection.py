import numpy as np
import pandas as pd

df = pd.read_csv("nhanes_2015_2016.csv")

## Keep certain columns: 'BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC', 'BMXWAIST'
columns_to_keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC', 'BMXWAIST']
df = df[columns_to_keep]

## Dataframe that consists only of rows where the value of 'BMXWAIST' is greater its median AND 'BMXLEG' must be less than 32
median = np.nanmedian(df["BMXWAIST"])
df = df[(df['BMXWAIST'] > median) & (df["BMXLEG"] < 32)]





