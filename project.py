from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem # importing classes

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db') 
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')
def hello():
    items = session.query(MenuItem).all()
    output = ''
    for item in items:
        output += item.name + '<br>'
        output += item.price + '<br>'
        output += item.description + '<br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
