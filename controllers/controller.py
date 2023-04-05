from app import app

from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template('order.html', title='Home', orders=orders)

@app.route('/<int:id>')
def single_order(id):
    return render_template('show.html', title='Single Order', order=orders[id-1])

