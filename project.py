from flask import Flask, render_template, request, redirect, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem # importing classes

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db') 
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)

    return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here
@app.route('/restaurant/new/<int:restaurant_id>', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash('New Menu Item created')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here
@app.route('/restaurant/edit/<int:restaurant_id>/<int:menu_id>/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    oldItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        oldItem.name = request.form['name']
        session.add(oldItem)
        session.commit()
        flash('Menu Item edited')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, item=oldItem)

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/delete/<int:restaurant_id>/<int:menu_id>/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash('Menu Item deleted')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    else:
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, item=item)


if __name__ == '__main__':
    app.secret_key='SECRET_KEY' # Flask will use this to create "sessions"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
