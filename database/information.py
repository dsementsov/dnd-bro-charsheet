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

        def getRacesList(self):
            return list(self.raceInfo.keys())

        def getRaceInfo(self, race):
            return self.raceInfo.get(race, "No information found!")

        def getSubracesList(self, race):
            return list(self.raceInfo[race]["subraces"].keys())
        
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
            pj.writeJSON("classes_alowed.json", self.classInfo)


        def getClassesList(self):
            pass

        def getClassInfo(self, cl):
            pass

        def getSubclassList(self, cl):
            pass
            
        def getSubclassInfo(self, subclass):
            pass

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