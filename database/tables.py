
# Import relational database libs
import sqlalchemy
from sqlalchemy import create_engine
# database import
from sqlalchemy import Integer, String, ForeignKey, Column, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
import json
import os

engine = create_engine(os.getenv("DATABASE_URI"), echo = True)
Base = declarative_base()

class Characters(Base):
    __tablename__ = "characters"
    char_id = Column(Integer, primary_key = True)
    user_id = Column(String)
    char_name = Column(String)
    level = Column(Integer)

    def __repr__(self):
        context = {
            "char_id" : self.char_id,
            "iser_ud" : self.user_id,
            "char_name" : self.char_name
        }
        return json.dumps(context)

class Characteristics(Base):
    __tablename__ = "characteristics"
    char_id = Column(Integer, primary_key = True)
    STR = Column(SmallInteger)
    DEX = Column(SmallInteger)
    CON = Column(SmallInteger)
    INT = Column(SmallInteger)
    WIS = Column(SmallInteger)
    CON = Column(SmallInteger)
    
    def __repr__(self):
        context = {
            "STR" : self.STR,
            "DEX" : self.DEX,
            "CON" : self.CON,
            "INT" : self.INT,
            "WIS" : self.WIS,
            "CON" : self.CON
        }
        return json.dumps(context)


class Proficiencies(Base):
    __tablename__ = "proficiencies"
    pass

Base.metadata.create_all(engine)