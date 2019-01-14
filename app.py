import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import render_template, request, redirect

from database.information import Information
import json

from enums.nmap import NMap
from enums.characteristics import Skills, Characteristics

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Session(app)

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
def build_race():
    #  get arguments
    from_scratch = request.args.get("from_scratch", "False")
    # debug
    if session['user_selected'] == None:
            session['user_selected'] = {}
    print(session)
    context = {}
    context["next"] = "build_race"
    context['options'] = info.getRacesList()
    context['infolink'] = "/info/race/"
    context['title'] = "Choose a Race:"

    if request.method == "POST":
        if from_scratch == "True" or request.form.get("race", "None") == "None":
            session['user_selected'] = {}
            return render_template("createchar.html", **context)
        session['user_selected']['race'] = request.form.get("race")
        link = "/build/" + request.form.get("race") + "/subrace"
        return redirect(link, code = 301)
    return render_template("createchar.html", **context)

@app.route('/build/<arg>/subrace', methods=['GET', 'POST'])
def build_subrace(arg):
    # degug
    if session['user_selected']["race"] == None or session['user_selected']["race"] == "null":
            session['user_selected'] = {}
            return redirect("/build")
    context = {}
    if not session['user_selected']["race"] == None:
        context["next"] = "build_subrace"
        context["dynlink"] = arg
        context["infolink"] = "/info/subrace/"
        context["options"] = info.getSubracesList(arg)
        context["title"] = "Choose a subrace"
        return render_template("createchar.html", **context)

    if request.method == "POST":
        return json.dumps(session["user_selected"])

############################################### INFOLINKS ##############################################
@app.route('/info/race/<race>')
def get_race_info(race):
    return json.dumps(info.getRaceInfo(race))

@app.route('/info/subrace/<subrace>')
def method_name(subrace):
    race = session["user_selected"].get("race")
    return json.dumps(info.getSubraceInfo(subrace, race))


