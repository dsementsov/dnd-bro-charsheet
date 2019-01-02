import json
import os


class Information:
    class __Information:

        raceInfo = {}
        classInfo = {}
        path = os.getcwd()

        def __getAllRacesInfo(self):
            file = self.path + "\\data\\races.json"
            with open(file, "r") as f:
                j = (json.loads("".join(f.readlines())))
            self.raceInfo = j

        def getRaceInfo(self, race):
            return self.raceInfo.get(race, "No information found!")

        def getSubracesList(self, race):
            pass
        
        def getSubraceInfo(self, subrace):
            pass

        def __getAllClassesInfo(self):
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