import json

from flask import render_template, Blueprint

from server.month import Month

home_page = Blueprint('home_page', __name__)


@home_page.route('/', methods=['GET'])
def home():
    month = Month()
    data = json.dumps(month.get_month_data())
    return render_template('calendar.html', data=data)
