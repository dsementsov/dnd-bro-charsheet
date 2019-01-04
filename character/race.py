import json
import sys

sys.path.append("..")

from database.information import Information

info = Information().instance

class Race(object):

    def __init__(self, subrace, race):
        self.race = race
        self.subrace = subrace
        feats = info.getSubraceInfo(subrace, race)

        self.size = feats.get("size", "M")
        self.getRacialStats(race, subrace)
        self.getRacialFeatures(race, subrace)


    def getRacialStats(self, race, subrace):
        #
        self.stats = {}
        self.speed = "30ft"
    
    def getRacialFeatures(self, race, subrace):
        self.features = {}
