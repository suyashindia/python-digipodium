from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base=declarative_base()

class books(base):
    _tablename_="books"
    id=Column(Integer,primary_key=true)
    title=Column(String(100))
    rating=Column(Integer)
    added_on=Column(DateTime,default=datetime.now())

    def str_(self):
        return self.title

    if name_=="_main_":
        Base.metadata.create_all(create_engine("sqlite:////db.sqlite3  ")
