from flask import Blueprint, request

from server.month import Month

api = Blueprint('api', __name__)


@api.route('/month_before', methods=['GET'])
def month_before():
    month = Month()
    month.month -= 1
    return month.get_month_data()


@api.route('/month_after', methods=['GET'])
def month_after():
    month = Month()
    month.month += 1
    data = month.get_month_data()
    return data


@api.route('/set_cycle_start_date', methods=['POST'])
def set_cycle_start_date():
    month = Month()
    cycle_start_date = request.data.decode('utf-8')
    month.set_cycle_start_date(cycle_start_date)
    data = month.get_month_data()
    return data


@api.route('/remove_cycle_start_date', methods=['POST'])
def remove_cycle_start_date():
    month = Month()
    date_to_remove = request.data.decode('utf-8')
    month.remove_cycle_start_date(date_to_remove)
    data = month.get_month_data()
    return data
