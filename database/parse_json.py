import os
import json

path = os.getcwd()

official = ["PHB", "EEPC", "SCAG", "VGM", "XGE"]

def filterRacesFrom(json_obj):
    allowed_races = {}
    # taking all the races that are from official sources
    for item in json_obj.get("race"):
        # straight get all races that are from official sources
        if item.get("source") in official:
                allowed_races[item.get("name")] = item

    # format subraces
    # filter subraces
    for race, features in allowed_races.items():
        subraces = {}
        for subrace in features.get("subraces", {}):
                if subrace.get("source", "PHB") in official:
                        subraces[subrace.get("name")] = subrace.copy()
        allowed_races[race]["subraces"] = subraces.copy()
    return allowed_races


def filterClassesFrom(json_obj):
        # filter class
        class_obj = json_obj.get("class")[0]
        filtered_class = class_obj.copy()
        subclasses = {}
        if not class_obj.get("source", "") in official:
                return None
        # filter subclasses
        for subclass in class_obj.get("subclasses", {}):
                if subclass.get("source") in official:
                        subclasses[subclass.get("name")] = subclass
        filtered_class["subclasses"] = subclasses
        return filtered_class

def writeJSON(file_name, dict_obj):
        file_path = path + "/data/" + file_name
        with open(file_path, "w") as j:
                j.writelines(json.dumps(dict_obj))
