from unittest import TestCase
from datetime import date

from server.cycle_calculator import CycleCalculator
from .test_cycle_calculator_mock_data import (
    TEST_ONE_DATA_RANGE,
    TEST_TWO_DATA_RANGE,
    TEST_LONG_DATA_RANGE,
    TEST_WITH_EVENTS_INTERSECTION
)


class CycleCalculatorTest(TestCase):

    def test_empty_data_range(self):
        data_range = []
        calculator = CycleCalculator(data_range)
        events = calculator.get_predicted_events()
        self.assertEqual(events, {})
        self.assertEqual(calculator.dates_range, [])
        self.assertEqual(calculator.last_cycle_date, None)
        self.assertEqual(calculator.period_for_average, 0)

    def test_one_data_range(self):
        data_range = [date(2021, 1, 1)]
        calculator = CycleCalculator(data_range)
        events = calculator.get_predicted_events()
        self.assertEqual(events, TEST_ONE_DATA_RANGE)
        self.assertEqual(calculator.dates_range, data_range)
        self.assertEqual(calculator.last_cycle_date, date(2021, 1, 1))
        self.assertEqual(calculator.period_for_average, 1)

    def test_two_data_range(self):
        data_range = [date(2021, 1, 1), date(2021, 2, 2)]
        calculator = CycleCalculator(data_range)
        events = calculator.get_predicted_events()
        self.assertEqual(events, TEST_TWO_DATA_RANGE)
        self.assertEqual(calculator.dates_range, data_range)
        self.assertEqual(calculator.last_cycle_date, date(2021, 2, 2))
        self.assertEqual(calculator.period_for_average, 2)

    def test_long_data_range(self):
        data_range = [
            date(2021, 1, 7), date(2021, 2, 3),
            date(2021, 3, 6), date(2021, 3, 31),
            date(2021, 4, 28), date(2021, 5, 22),
            date(2021, 6, 19)
        ]
        calculator = CycleCalculator(data_range)
        events = calculator.get_predicted_events()
        self.assertEqual(events, TEST_LONG_DATA_RANGE)
        self.assertEqual(calculator.dates_range, data_range[-6:])
        self.assertEqual(calculator.last_cycle_date, date(2021, 6, 19))
        self.assertEqual(calculator.period_for_average, 6)

    def test_with_events_intersection(self):
        data_range = [
            date(2021, 1, 1), date(2021, 1, 15),
            date(2021, 2, 3), date(2021, 2, 18)
        ]
        calculator = CycleCalculator(data_range)
        events = calculator.get_predicted_events()
        self.assertEqual(events, TEST_WITH_EVENTS_INTERSECTION)
        self.assertEqual(calculator.dates_range, data_range)
        self.assertEqual(calculator.last_cycle_date, date(2021, 2, 18))
        self.assertEqual(calculator.period_for_average, 4)
