import pandas as pd
section=['A','B','C','D','E']
contri=[6700,5600,5000,5200,7000]
s11=pd.Series(data=contri,index=section)
print(s11)
