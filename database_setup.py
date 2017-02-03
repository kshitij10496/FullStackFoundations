import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

######## Class ########### 
class Restaurant(Base):
    __tablename__ = 'restaurant'

class MenuItem(Base):
    __tablename__ = 'menu_item'

######## Configuration: at the end of the file ########
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
