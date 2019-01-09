import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template, request

from database.information import Information
import json

from enums.nmap import NMap
from enums.characteristics import Skills, Characteristics

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


user_authentificated = False
username = ""
user_selected = {}

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
    context = {"mods" : [], "skills": [], "saves" : []}
    for key, value in mods.items():
        ability_dict = {}
        ability_dict["name"] = NMap.ability_abr[key]
        ability_dict["value"] = value
        ability_dict["mod"] = abs((value-10)//2)
        if ((value-10)//2) > 0:
            ability_dict["sign"] = "+" 
        elif ((value-10)//2) == 0:
            ability_dict["sign"] = "    " 
        else:
            ability_dict["sign"] = "-"
        context["mods"].append(ability_dict)

    for skill in Skills:
        skill_dict = {}
        skill_dict["prof"] = "•"
        skill_dict["mod"] = NMap.skill_to_ability.get(skill).value
        skill_dict["name"] = skill.value
        skill_dict["bonus"] = 0
        context["skills"].append(skill_dict)
    # return json.dumps(context)

    for mod in Characteristics:
        saves_dict = {}
        saves_dict["prof"] = "•"
        saves_dict["adv"] = "•"
        saves_dict["name"] = mod.value
        saves_dict["bonus"] = 0
        context["saves"].append(saves_dict)

    return render_template("charsheet.html", **context)


@app.route("/charsheet/<int:id>", methods = ["GET"])
def displayCharsheet(id):
    context = {}

    # generate character to display
        # query database
        # count everything
        # fill in context
        # pass to the template

    # get data about character
    # put context in place

    # render character template if character exists
    return render_template("charsheet.html")
    # render 404 if there is no character

@app.route('/build', methods = ["GET", "POST"])
def build_character(from_scratch=False):
    context = {}
    if from_scratch == "True":
        session['user_selected'] = {}
        return render_template("createchar.html", **context)
    
    context["selections"] = session['user_selected']
    if request.method == "POST":
        request.form.get("selector")
        context["Title"] = "Please select from the list:"

        if not "race" in context.get("selections"):
            l = sorted(info.getRacesList())
        elif not "subrace" in  context.get("selections"):
            l = sorted(info.getSubracesList(context["selections"]["race"]))
        elif not "class" in context.get("selections"):
            l = sorted(info.getClassesList())
        elif not "subclass" in context.get("selections"):
            l = sorted(info.getSubclassList(context["selections"]["class"]))
        context["selection"] = l
        return render_template("createchar.html", **context)
    
    for cl in sorted(info.getClassesList()):
        c = {}
        c["name"] = cl.capitalize()
        c["subclasses"] = sorted(info.getSubclassList(cl))
        context["classes"].append(c)
    return render_template("createchar.html", **context)

@app.route('/test')
def test():
   return str(info.getClassesList())
