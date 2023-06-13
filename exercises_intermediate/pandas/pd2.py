import pandas as pd
d={
    'carat':[24,22,23,24,24,24,22,23,20,21],
    'cut':['oval','oval','round brilliant','pear','emerald','oval','round brilliant','pear','pear','oval'],
    'color':['steel gray', 'white', 'blue', 'yellow', 'orange', 'red', 'green', 'pink' ,'purple', 'brown'],
    'depth':['57%','58%','57%','58%','60%','61%','58%','58%','59%','57%'],
    'price':[40000000,50000000,80000000,8560000,14580000,54400000,40000000,50000000,80000000,8560000]
}

df=pd.DataFrame(d)
df.to_csv("diamond.csv")
print(pd.read_csv("diamond.csv"))
print("\nNumber of rows and columns: ",df.shape)
print("\nData in first 5 rows: ",df.head(5))
print("\nData in last 3 rows",df.tail(3))
print(df['color'])
print(df.sort_values(by='cut', ascending=False))