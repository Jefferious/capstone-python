from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

app = Flask(__name__)

@app.route("/normal")
def normal_tic():
    normal = crud.get_normal()

    return render_template("normal.html", normal=normal)

@app.route("/super")
def super_tic():
    super = crud.get_super()

    return render_template("super.html", super=super)

@app.route("/homepage.html")
def homepage():
    homepage = crud.get_home()

    return render_template("hompeage.html", homepage=homepage)