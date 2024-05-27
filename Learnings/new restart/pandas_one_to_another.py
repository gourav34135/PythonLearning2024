import pandas as pd
df1 = pd.Series([4,7,3,10])
df2 = pd.Series([9,4,3])
print("First series: \n",df1)
print("Second series: \n",df2)
result = df1[~df1.isin(df2)]
print(result)
