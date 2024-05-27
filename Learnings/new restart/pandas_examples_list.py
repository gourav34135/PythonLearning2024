import pandas as pd
target=[56000,70000,75000,60000]
sales=[58000,68000,78000,61000]
zonesales=[target,sales]
df=pd.DataFrame(zonesales,columns=["zoneA","zoneB","zoneC","zoneD"],index=["Trget","Sales"])
print(df)
