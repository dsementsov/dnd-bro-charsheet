import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template

from database.information import Information
import json

from enums.nmap import NMap

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


user_authentificated = False
username = ""

info = Information().instance

@app.route("/")
def index():
    mods = {
        "STR": 15,
        "DEX": 10,
        "CON": 12,
        "INT": 14,
        "WIS": 8,
        "CHA": 16
    }
    context = { "mods" : []}
    for key, value in mods.items():
        ability_dict = {}
        ability_dict["name"] = NMap.abilityAbbreviations[key]
        ability_dict["value"] = value
        ability_dict["mod"] = abs((value-10)//2)
        if ((value-10)//2) > 0:
            ability_dict["sign"] = "+" 
        elif ((value-10)//2) == 0:
            ability_dict["sign"] = "    " 
        else:
            ability_dict["sign"] = "-"
        context["mods"].append(ability_dict)
    # return json.dumps(context)
    return render_template("charsheet.html", **context)


@app.route("/charsheet/<int:id>", methods = ["GET"])
def displayCharsheet(id):
    context = {}

    # get data about character
    # put context in place

    # render character template if character exists
    return render_template("charsheet.html")
    # render 404 if there is no character

@app.route('/createchar')
def createchar():
    context = {}
    context["races"] = sorted(info.getRacesList())
    return render_template("createchar.html", **context)
