import pandas as pd
d = {'Sr.no.':[1,2,3,4],'Name':['Alex','John','Peter','Klaus'],'Age':[30,27,29,33],'Salary':[50000,65000,58000,66000]}
df = pd.DataFrame(d)
df.to_csv('new_file.csv', sep='\t', index=False)
new = pd.read_csv('new_file.csv')
print(new)
