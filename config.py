import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # quantity of last months to forecast start of cycle
    MONTHS_FOR_AVERAGE = 6
    # average period before the start of the cycle
    AVERAGE_DAYS_PERIOD = 27
    # average period before the middle of the cycle
    MIDDLE_START = 10

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev secret key'
