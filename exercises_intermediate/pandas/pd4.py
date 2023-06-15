import pandas as pd
df=pd.read_csv("details.csv",index_col='roll no')
#details of students with marks greater than 40
print(df[df['marks']>40])
#3 rows with 2 colums with keyword 'iloc'
print(df.iloc[0:3,[0,2]])
#using keyword 'loc'
print(df.loc['101','anju'])#have error
