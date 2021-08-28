from unittest import TestCase
from unittest.mock import patch
from calendar import Calendar
from datetime import date

from server.month import Month
from server.cycle_calculator import CycleCalculator
from server.models import Date, CycleEvent
from tests.test_month.test_month_mock_data import (
    MOCK_DATES,
    MOCK_PREDICTED_CYCLE_EVENTS,
    MOCK_PREDICTED_CYCLE_EVENTS_PLUS_DATE,
    MOCK_DATE_NOW,
    MOCK_MONTH_DATA,
    MOCK_DATES_EVENTS,
    MOCK_DATES_EVENTS_PLUS_DAY
)


@patch('server.month.CycleCalculator.get_predicted_events')
@patch('server.month.Date.get_dates')
class TestMonth(TestCase):

    def test_get_month_data(
            self, mock_get_dates, mock_get_predicted_events
    ):
        mock_get_dates.return_value = MOCK_DATES
        mock_get_predicted_events.return_value = MOCK_PREDICTED_CYCLE_EVENTS
        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, MOCK_DATE_NOW
        )
        month_data = month.get_month_data()
        self.assertEqual(month_data, MOCK_MONTH_DATA)
        del month

    @patch('server.month.Date.set_date')
    def test_set_cycle_start_date(
            self, mock_set_date, mock_get_dates,
            mock_get_predicted_events
    ):
        test_cycle_start_date = '2021-7-7'
        mock_get_dates.side_effect = [
            MOCK_DATES,
            MOCK_DATES + [
                Date(date_=date(2021, 7, 7),
                     cycle_event=[CycleEvent(type_='cycle_start')])
            ]
        ]
        mock_get_predicted_events.side_effect = [
            MOCK_PREDICTED_CYCLE_EVENTS,
            MOCK_PREDICTED_CYCLE_EVENTS_PLUS_DATE
        ]
        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, MOCK_DATE_NOW
        )
        self.assertEqual(month.dates_events, MOCK_DATES_EVENTS)

        month.set_cycle_start_date(test_cycle_start_date)

        mock_set_date.assert_called_once_with(date(2021, 7, 7))
        self.assertEqual(month.dates_events, MOCK_DATES_EVENTS_PLUS_DAY)
        del month

    @patch('server.month.CycleEvent.remove_date_from_start_cycle')
    def test_remove_cycle_start_date(
            self, mock_set_date, mock_get_dates,
            mock_get_predicted_events
    ):
        test_cycle_start_date = '2021-7-7'
        mock_get_dates.side_effect = (
            MOCK_DATES + [
                Date(date_=date(2021, 7, 7),
                     cycle_event=[CycleEvent(type_='cycle_start')])
            ],
            MOCK_DATES
        )
        mock_get_predicted_events.side_effect = (
            MOCK_PREDICTED_CYCLE_EVENTS_PLUS_DATE,
            MOCK_PREDICTED_CYCLE_EVENTS
        )
        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, MOCK_DATE_NOW
        )
        self.assertEqual(month.dates_events, MOCK_DATES_EVENTS_PLUS_DAY)

        month.remove_cycle_start_date(test_cycle_start_date)

        mock_set_date.assert_called_once_with(date(2021, 7, 7))
        self.assertEqual(month.dates_events, MOCK_DATES_EVENTS)
        del month

    def test_month_setter(
            self, mock_get_dates, mock_get_predicted_events
    ):
        mock_get_dates.return_value = MOCK_DATES
        mock_get_predicted_events.return_value = MOCK_PREDICTED_CYCLE_EVENTS

        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, date(2021, 12, 1)
        )
        month.month += 1
        self.assertEqual(month._month, 1)
        self.assertEqual(month._year, 2022)
        del month

        month = Month(
            Date, CycleEvent, CycleCalculator, Calendar, date(2021, 1, 1)
        )
        month.month -= 1
        self.assertEqual(month._month, 12)
        self.assertEqual(month._year, 2020)
        del month
