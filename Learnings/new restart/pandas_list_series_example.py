import pandas as pd
import numpy as np
staff=pd.Series([20,36,44])
salaries=pd.Series([279000,396800,563000])
avg=salaries/staff
org={"people":staff,"amount":salaries,"average":avg}
dtf=pd.DataFrame(org)
print(dtf)
