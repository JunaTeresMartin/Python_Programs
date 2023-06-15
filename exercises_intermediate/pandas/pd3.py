import pandas as pd
df=pd.read_csv("details.csv")
print(df)
df=pd.read_csv("details.csv",index_col="roll no")
print(df)
#gives a description
print(df.describe())
#gives the number of columns and rows
print(df.shape)
#sum of marks
print(df["marks"].sum())
#minimum value in marks
print(df["marks"].min())
#max
print(df["marks"].max())
#varience
print(df["marks"].var())
#mean
print(df["marks"].mean())
#std deviation
print(df["marks"].std())
