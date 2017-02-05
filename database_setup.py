######## Database Design #######
'''
     ____________                _______________
    | Restaurant |              |   Menu_Item   |
    |------------|              |---------------|
    |    name    |              |      name     |
    |     id     |------        |  description  |
     ------------       |       |      price    |
                        |       |     course    |
                         ------>| restaurant_id |
                                 ---------------
'''

import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

######## Class ########### 
class Restaurant(Base):
    ####### Table #######
    __tablename__ = 'restaurant'

    ####### Mapper #######
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

####### Class #######
class MenuItem(Base):
    ####### Table #######
    __tablename__ = 'menu_item'

    ####### Mapper #######
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        ''' Returns object data in easily serializeable format that Flask can easily use. '''
        return {
                'name': self.name,
                'description': self.description,
                'id': self.id,
                'price': self.price,
                'course': self.course
                }
######## Configuration: at the end of the file ########
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
