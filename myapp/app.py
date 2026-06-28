from flask import Flask
from flask import render_template
from flask import request

import sqlite3

# Query Database
def QueryDB():
    con = sqlite3.connect("./DBFolder/GigglesGalore.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM CustomerComments ORDER BY rowid DESC LIMIT 3").fetchall()
    return res
    # print(type(res))
    # print(res)
    # print(res[0][0])
    # print(res[0][1])

# Insert into Database
def InsertDB(Username, Comments):
    con = sqlite3.connect("GigglesGalore.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO CustomerComments VALUES ('{Username}','{Comments}')")
    con.commit()


app = Flask(__name__)

@app.route("/")
def renderHomePage():
    return render_template("GigglesGalore.html")

@app.route("/products/")
def renderProductsPage():
    return render_template("products.html")

@app.route("/about/")
def renderAboutPage():
    return render_template("about.html")

@app.route("/contact/")
def renderContactPage():
    return render_template("contact.html")

@app.route("/extra/", methods=["GET", "POST"])
def renderExtraPage():
    if request.method == "POST":
        FormUsername = request.form["Username"]
        FormComments = request.form["Comments"]        
        InsertDB(FormUsername, FormComments)
        Entries = QueryDB()
        return render_template("extra.html", Entries=Entries)
    else:
        Entries = QueryDB()
        return render_template("extra.html", Entries=Entries)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")