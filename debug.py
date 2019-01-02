from database.information import Information
import os
import json

# print(json.JSONDecoder("\\data\\races.json"))
# dec = json.JSONDecoder()
# dec.decode("\\data/races.json")

path = os.getcwd()
new_file = path + "\\data\\new_races.json"



info = Information().instance

print(info.getRaceInfo("Elf"))



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