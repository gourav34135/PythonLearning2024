import sqlite3
conn=sqlite3.connect("aquarium.db")
cursor=conn.cursor()
roll=cursor.execute("insert into fish values('samay','shark',1),('jamie','uttlefish',7)")
print(roll)
