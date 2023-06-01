from flask import Flask, render_template, request, make_response, redirect, url_for
from db_connect import db as mysql
import pymysql, re

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.args.get("logout"):
        return render_template("index.html", logout=True)
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method != "POST":
        return render_template("error.html")

    full_data = request.form

    if "id" not in full_data.keys() or "pw" not in full_data.keys():
        return render_template("error.html")

    id = full_data["id"]
    pw = full_data["pw"]

    p = re.compile("[;\"\']")
    if p.match(id) or p.match(pw):
        return render_template("error.html", error="죄송합니다. 입력하신 패스워드가 SIF에 의해 차단되었습니다.")

    db, cursor = mysql()
    cursor.execute("select * from dreamhack.test where uid='"+str(id)+"' and upw='"+str(pw)+"'")
    result = cursor.fetchall()
    if len(result) == 0:
        return render_template("login.html", error=1)
    elif len(result) != 1:
        return render_template("login.html", error=2)

    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("ID", id)
    resp.set_cookie("PW", pw)

    return resp

@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index", logout=True)))
    resp.set_cookie("ID", "", expires=0)
    resp.set_cookie("PW", "", expires=0)
    return resp


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)
