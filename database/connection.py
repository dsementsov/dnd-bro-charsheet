import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
import os


class Connection: 

    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URI"))
        self.conn = self.engine.connect()
        # Session = scoped_session(sessionmaker(bind=self.engine))
        # self.db = Session()

    def executeQuery(self, query, insert = False):
    # make it a singleton?
        result = self.conn.execute(query)
        if insert:
            self.conn.commit()
        else:
            result.fetchone()
        return str(result)
        
        
        

