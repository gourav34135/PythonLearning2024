import pandas as pd
c11=pd.Series(data=[30,40,50],index=["science","commerce","humanities"])
c22=pd.Series(data=[37,44,45],index=["science","commerce","humanities"])
print("Total no. of students")
print(c11+c22)
