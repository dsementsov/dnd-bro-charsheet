import json
import os
from database import parse_json as pj
import requests


class Information:
    class __Information:
        """
        Singletone object that gives access to local database and ease the search
        """

        five_e_tools = "https://5etools.com/data/"
        five_tools_races = "races.json"
        five_tools_classes = "class/index.json"


        raceInfo = {}
        classInfo = {}
        path = os.getcwd()

        def __getAllRacesInfo(self):
            """Part of the constructor to parse data only once"""
            # file = self.path + "/data/allowed_races.json"
            # with open(file, "r") as f:
            #     j = (json.loads("".join(f.readlines())))
            # self.raceInfo = j
            url = self.five_e_tools + self.five_tools_races
            r = requests.get(url)
            self.raceInfo = pj.filterRacesFrom(r.json())
            # pj.writeJSON("allowed_rasses.json", self.raceInfo)

        def getRacesList(self):
            return [r for r in self.raceInfo.keys() if r is not None]

        def getRaceInfo(self, race):
            return self.raceInfo.get(race, "No information found!")

        def getSubracesList(self, race):
            return [s for s in self.raceInfo[race]["subraces"].keys() if s is not None]
        
        def getSubraceInfo(self, subrace, race = None):
            if race:
                raceFeatures = self.raceInfo.get(race, { "subraces" : { subrace : {"No race found!"}}})
                subraces = raceFeatures.get("subraces", {subrace : {"Race has no subraces!"}})
                if subraces == {}:
                    subraces = {subrace:{"Race has no subraces!"}}
                return subraces.get(subrace, {"No subrace found!"})
            else:
                for race, features in self.raceInfo.items():
                    for subname, subfeats in features.get("subraces").items():
                        if subname == subrace:
                            return subfeats


        def __getAllClassesInfo(self):
            """Part of the constructor to parse data only once"""
            url = self.five_e_tools + self.five_tools_classes
            r = requests.get(url)
            for cl, index in r.json().items():
                to_parse = self.five_e_tools + "class/" + index
                r_index = requests.get(to_parse)
                class_dict = pj.filterClassesFrom(r_index.json())
                if class_dict:
                    self.classInfo[cl] = class_dict.copy()
            # pj.writeJSON("allowed_classes.json", self.classInfo)


        def getClassesList(self):
            return [c for c in self.classInfo.keys() if c is not None]

        def getClassInfo(self, cl):
            return self.classInfo.get(cl, "No such class found!")

        def getSubclassList(self, cl):
            return self.classInfo.get(cl).get("subclasses", {})
            
        def getSubclassInfo(self, subclass, cl = None):
            if cl:
                return self.classInfo.get(cl, {subclass : "No such class found!"}).get(subclass, "No subclass found!")
            else:
                for c, f in self.classInfo.items():
                    if subclass in f.get("subclasses"):
                        return f.get("subclasses").get("subclass")
                return "No such subclass!"

        def __init__(self):
            self.__getAllRacesInfo()
            self.__getAllClassesInfo()

    instance = None

    def __init__(self):
        if not Information.instance:
            Information.instance = Information.__Information()
        else:
            pass

    def __getattr__(self, name):
        return getattr(self.instance, name)