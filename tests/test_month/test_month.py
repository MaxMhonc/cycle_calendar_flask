from unittest import TestCase
from unittest.mock import MagicMock, patch
from datetime import date
from calendar import Calendar

from server.month import Month
from server.cycle_calculator import CycleCalculator
from server.models import Date, CycleEvent

MOCK_DATES = [
    Date(date_=date(2021, 1, 1),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 2, 2),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 3, 3),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 4, 4),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 5, 5),
         cycle_event=[CycleEvent(type_='cycle_start')]),
    Date(date_=date(2021, 6, 6),
         cycle_event=[CycleEvent(type_='cycle_start')]),
]
MOCK_PREDICTED_CYCLE_EVENTS = {
    date(2021, 7, 7): ['predicted_start0'],
    date(2021, 7, 8): ['predicted_start1'],
    date(2021, 7, 6): ['predicted_start1'],
    date(2021, 7, 5): ['predicted_start2'],
    date(2021, 7, 9): ['predicted_start2'],
    date(2021, 7, 10): ['predicted_start3'],
    date(2021, 7, 4): ['predicted_start3'],
    date(2021, 7, 3): ['predicted_start4'],
    date(2021, 7, 11): ['predicted_start4'],
    date(2021, 6, 16): ['cycle_middle'],
    date(2021, 6, 17): ['cycle_middle'],
    date(2021, 6, 18): ['cycle_middle'],
    date(2021, 6, 19): ['cycle_middle'],
    date(2021, 6, 20): ['cycle_middle']
}
MOCK_DATE_NOW = date(2021, 7, 1)


class TestMonth(TestCase):

    @patch('server.month.CycleCalculator.get_predicted_events')
    @patch('server.month.Date.get_dates')
    def test_get_month_data(
            self, mock_get_dates, mock_get_predicted_events
    ):
        mock_get_dates.return_value = MOCK_DATES
        mock_get_predicted_events.return_value = MOCK_PREDICTED_CYCLE_EVENTS
        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, MOCK_DATE_NOW
        )
        month_data = month.get_month_data()
        self.assertEqual(month_data, 'data')

    def test_set_cycle_start_date(self):
        pass

    def test_remove_cycle_start_date(self):
        pass

    def test_month_setter(self):
        pass

    def test_month_property(self):
        pass

    def test_month_name_property(self):
        pass

    def test_year_property(self):
        pass
