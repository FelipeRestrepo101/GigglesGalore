import sqlite3

con = sqlite3.connect('GigglesGalore.db')

cur = con.cursor()

res = cur.execute("SELECT * FROM CustomerComments").fetchall()

print(res)