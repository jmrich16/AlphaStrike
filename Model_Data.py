import sqlite3


conn = sqlite3.connect('modelstats.db')
print("Opened database Succesfully")

c = conn.cursor()
#Create model table

c.execute('''CREATE TABLE model_stats(
                ModelName varchar(255),
                ModelPoints int,
                Move int,
                WS int,
                BS int,
                Strength int,
                Toughness int,
                Wounds int,
                Attacks int,
                Leadership int,
                Faction varchar(255)
                )''')

#Insert a test row in table

c.execute("INSERT INTO model_stats VALUES ('Bloodthirster of Unfettered Fury',100,12,2,2,7,7,16,6,10,'Daemons')")

conn.commit()
conn.close

