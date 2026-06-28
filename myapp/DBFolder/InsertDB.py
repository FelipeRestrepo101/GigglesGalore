import sqlite3

def InsertDB():
    con = sqlite3.connect("GigglesGalore.db")
    cur = con.cursor()
    cur.execute("INSERT INTO CustomerComments VALUES ('NewUser','NewComment')")
    con.commit()

InsertDB()