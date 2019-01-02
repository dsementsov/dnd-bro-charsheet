import json

class Race(object):

    def __init__(self, race, subrace):
        self.race = race
        self.subrace = subrace
        self.getRacialStats(race, subrace)
        self.getRacialFeatures(race, subrace)

    @classmethod
    def fromSubrace(cls, subrace):
        # get race and subrace
        race = " "
        return Race(race, subrace)

    def getRacialStats(self, race, subrace):
        #
        self.stats = {}
        self.speed = "30ft"
    
    def getRacialFeatures(self, race, subrace):
        self.features = {}
