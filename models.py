from sqlalchemy import Column,String,Integer
from database import Base

class Exptracker(Base):
    __tablename__="exptracker"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    amount=Column(Integer)
    