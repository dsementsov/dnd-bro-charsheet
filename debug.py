from database.information import Information
import os
import json

# print(json.JSONDecoder("\\data\\races.json"))
# dec = json.JSONDecoder()
# dec.decode("\\data/races.json")

path = os.getcwd()
new_file = path + "\\data\\new_races.json"

info = Information().instance.raceInfo

official = ["PHB", "EEPC", "SCAG", "VGM", "XGE"]
included = []
not_included = []

official_races = {}

# print(info)

print("Analyzing races...")
for race in info.keys():
    source = info[race].get("source", "")
    included.append(f"{race} from {source}")
print("Analysing subraces")
for race, value in info.items():
    for subrace, features in value.get("subraces", {}).items():
        source = features.get("source", "")
        if source in official:
            included.append(f"{race} of {subrace}  from {source} is included")
        else:
            not_included.append(f"{race} of {subrace}  from  {source} is not included")

# for item in sorted(included):
#     print(item)
# print("===========")
# for item in sorted(not_included):
#     print(item)





# Editing races info

# right_subraces = info.raceInfo.copy()
# for key,item in info.raceInfo.items():
#     subraces = item.get("subraces", [])
#     # print(subraces)
#     sub_dict = {}
#     for item in subraces:
#         sub_dict[item.get("name", "None")] = item
#     info.raceInfo[key]["subraces"] = sub_dict.copy()

# with open (new_file, "w") as f:
#     print("writing file")
#     f.writelines(json.dumps(info.raceInfo))
#     print("done")