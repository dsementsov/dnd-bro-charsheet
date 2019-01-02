from enums.characteristics import Characteristics

class Skeleton:

    characteristics = {
        Characteristics.STR : 0,
        Characteristics.DEX : 0,
        Characteristics.CON : 0,
        Characteristics.INT : 0,
        Characteristics.WIS : 0,
        Characteristics.CHA : 0
    }

    mods = {
        Characteristics.STR : 0,
        Characteristics.DEX : 0,
        Characteristics.CON : 0,
        Characteristics.INT : 0,
        Characteristics.WIS : 0,
        Characteristics.CHA : 0
    }
    
    

    def __init__(self, characteristics):
        pass


    def getCharContext(self):
        context = {}
        return context

    
    def __del__(self):
        del self

    