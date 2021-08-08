from unittest import TestCase
from unittest.mock import patch
from calendar import Calendar

from server.month import Month
from server.cycle_calculator import CycleCalculator
from server.models import Date, CycleEvent
from tests.test_month.test_month_mock_data import MOCK_DATES, \
    MOCK_PREDICTED_CYCLE_EVENTS, MOCK_DATE_NOW


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
