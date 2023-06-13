import pandas as pd
dict={
    'Reg no:':['ABC123','CDE234','GHI789'],
    'Name':['Ganesh Kumar','John Mathew','Reena .K'],
    'Semester':['S8','S7','S6'],
    'College':['ABC','CDE','GHI'],
    'CGP':[9.8,9.9,9.7]
    }
df=pd.DataFrame(dict)
df.to_csv("topper.csv")
print(pd.read_csv("topper.csv"))
