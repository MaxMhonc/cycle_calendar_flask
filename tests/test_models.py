from unittest import TestCase
from datetime import date

from app import app, db
from server.models import Date, CycleEvent
from tests.mock_data import DATES_EVENTS


class ModelsTest(TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        db.session.remove()
        with app.app_context():
            db.drop_all()

    # def test_models(self):
    #     with app.app_context():
    #         db.session.add(CycleEvent(type_='cycle_start'))
    #         db.session.commit()
    #         Date.set_date(date(2021, 1, 1))
    #         Date.set_date(date(2021, 2, 2))
    #
    #         dates_events = Date.dates_events_to_json(
    #             Date.get_dates_events())
    #     self.assertEqual(dates_events, DATES_EVENTS)
