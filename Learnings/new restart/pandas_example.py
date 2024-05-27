import pandas as pd
population=pd.Series([10927986,42691836,4631392,4328063])
hospitals=pd.Series([189,208,149,157])
schools=pd.Series([7916,8508,7226,7617])
org={"population":population,"hospitals":hospitals,"schools":schools}
ll=pd.DataFrame(org)
print(ll)
l1=pd.DataFrame(ll,index=["Delhi","Mumbai","Kolkata","chennai"],columns=[population,hospitals,schools])
print(l1)
