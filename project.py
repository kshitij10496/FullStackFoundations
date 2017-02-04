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
    items = session.query(MenuItem).first()
    output = ''
    for item in items:
        output += item.name + '<br>'
        output += item.price + '<br>'
        output += item.description + '<br>'
    return output

# Task 1: Create route for newMenuItem function here
@app.route('/restaurant/new/<int:restaurant_id>')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/edit/<int:restaurant_id>/<int:menu_id>/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/delete/<int:restaurant_id>/<int:menu_id>/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
