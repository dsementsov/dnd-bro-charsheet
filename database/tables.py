
import json
import os

# Import relational database libs
import sqlalchemy
# database import
from sqlalchemy import (Column, ForeignKey, Integer, SmallInteger, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv("DATABASE_URI"), echo=True)
Base = declarative_base()


class Characters(Base):
    __tablename__ = "characters"
    char_id = Column(Integer, primary_key=True)
    user_id = Column(String)
    char_name = Column(String)
    level = Column(Integer)

    def __repr__(self):
        context = {
            "char_id": self.char_id,
            "iser_ud": self.user_id,
            "char_name": self.char_name
        }
        return json.dumps(context)


class Abilities(Base):
    __tablename__ = "abilities"
    char_id = Column(Integer, ForeignKey("characters.char_id"), primary_key = True)
    STR = Column(SmallInteger, nullable = False)
    DEX = Column(SmallInteger, nullable = False)
    CON = Column(SmallInteger, nullable = False)
    INT = Column(SmallInteger, nullable = False)
    WIS = Column(SmallInteger, nullable = False)
    CON = Column(SmallInteger, nullable = False)
    
    def __repr__(self):
        context = {
            "STR": self.STR,
            "DEX": self.DEX,
            "CON": self.CON,
            "INT": self.INT,
            "WIS": self.WIS,
            "CON": self.CON
        }
        return json.dumps(context)


class SkillProficiencies(Base):
    __tablename__ = "skill_proficiencies"
    char_id = Column(Integer, ForeignKey("characters.char_id"), primary_key = True)
    ATHLETICS = Column(SmallInteger, default = 0)
    ACROBATICS = Column(SmallInteger, default = 0)
    SLEIGHT_OF_HAND = Column(SmallInteger, default = 0)
    STEALTH = Column(SmallInteger, default = 0)
    ARCANA = Column(SmallInteger, default = 0)
    HISTORY = Column(SmallInteger, default = 0)
    INVESTIGATION = Column(SmallInteger, default = 0)
    NATURE = Column(SmallInteger, default = 0)
    RELIGION = Column(SmallInteger, default = 0)
    ANIMAL_HANDLING = Column(SmallInteger, default = 0)
    INSIGH = Column(SmallInteger, default = 0)
    MEDICINE = Column(SmallInteger, default = 0)
    PERCEPTION = Column(SmallInteger, default = 0)
    SURVIVAL = Column(SmallInteger, default = 0)
    DECEPTION = Column(SmallInteger, default = 0)
    INTIMIDATION = Column(SmallInteger, default = 0)
    PERFORMANCE = Column(SmallInteger, default = 0)
    PERSUATION = Column(SmallInteger, default = 0)
    

class AbilProficiencies(Base):
    __tablename__ = "abli_proficiencies"
    char_id = Column(Integer, ForeignKey("characters.char_id"), primary_key = True)
    STR = Column(SmallInteger, default = 0)
    DEX  = Column(SmallInteger, default = 0)
    CON = Column(SmallInteger, default = 0)
    INT = Column(SmallInteger, default = 0)
    WIS = Column(SmallInteger, default = 0)
    CHA = Column(SmallInteger, default = 0)


# Table to hold characteristics <- ability to update it each 4 lvls
# Table to hold chosen proficiencies <- ablility to frequently update it
# Hold table of spellcasting? 
# Hol


Base.metadata.create_all(engine)
