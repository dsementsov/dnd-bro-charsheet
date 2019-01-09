from enums.characteristics import Skills, Characteristics

class NMap():

    ability_abr = {
    "STR" : "STRENGTH",
    "DEX" : "DEXTERITY",
    "CON" : "CONSTITUTION",
    "INT" : "INTELECT",
    "WIS" : "WISDOM",
    "CHA" : "CHARISMA"
    }

    skill_to_ability = {
        Skills.ACROBATICS : Characteristics.DEX,
        Skills.ANIMAL_HANDLING : Characteristics.WIS,
        Skills.ARCANA : Characteristics.INT,
        Skills.ATHLETICS : Characteristics.STR,
        Skills.DECEPTION : Characteristics.CHA,
        Skills.HISTORY : Characteristics.INT,
        Skills.INSIGHT : Characteristics.WIS,
        Skills.INTIMIDATION : Characteristics.CHA,
        Skills.INVESTIGATION : Characteristics.INT,
        Skills.MEDICINE : Characteristics.WIS,
        Skills.NATURE : Characteristics.INT,
        Skills.PERCEPTION : Characteristics.WIS,
        Skills.PERFORMANCE : Characteristics.CHA,
        Skills.PERSUATION : Characteristics.CHA,
        Skills.RELIGION : Characteristics.INT,
        Skills.SLEIGHT_OF_HAND : Characteristics.DEX,
        Skills.STEALTH : Characteristics.DEX,
        Skills.SURVIVAL : Characteristics.WIS
    }

