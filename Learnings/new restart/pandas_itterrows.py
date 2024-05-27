import pandas as pd
sales={'yr1':{'qtr1':34500,'qtr2':56000,'qtr3':47000,'qtr4':49000},\
       'yr2':{'qtr1':44900,'qtr2':46100,'qtr3':57000,'qtr4':59000},\
       'yr3':{'qtr1':54500,'qtr2':51000,'qtr3':57000,'qtr4':58500}}
df=pd.DataFrame(sales)
for (row,rowseries) in df.iterrows():
    print("ROW INDEX:",row)
    print("CONTAINS:")
    print(rowseries)
