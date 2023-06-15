import pandas as pd
df=pd.read_csv("details.csv")
print(df)
df=pd.read_csv("details.csv",index_col="roll no")
print(df)
