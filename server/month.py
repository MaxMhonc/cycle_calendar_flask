import calendar
from calendar import Calendar
from datetime import datetime, date
from typing import Iterable, List, Dict, Any, Union, Optional

from server.models import Date, CycleEvent
from server.cycle_calculator import CycleCalculator


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        # ToDo: remove this bullshit
        print('<><><><><><><>< I WAS CALLED ><><><><><><><>')
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Month:
    """
    Month-class is responsible for providing info about month to UI
    in next format:
        data = {
            'days': {
                'date': date,
                'events': [events]
            },
            'month': month_name,
            'year': year
        }
    and converting data from UI to appropriate for
    'date_class' and 'event_class' format.
    For handling dates and events classes 'date_class' and 'event_class'
    are required.
    For calculating predicted cycle dates - 'calculator'
    """

    def __init__(
            self,
            date_class, event_class, calculator, calendar_handler, date_now
    ):
        self.date_now = date_now
        self.date_class = date_class
        self.event_class = event_class
        self.calculator = calculator
        self.dates_events = self._get_dates_events()
        self.calendar = calendar_handler()
        self._year, self._month = self._get_current_year_month()

    @staticmethod
    def _convert_date(event_date):
        """Convert event date to appropriate for date_class format"""
        return date(*map(int, event_date.split('-')))

    def _get_current_year_month(self) -> Iterable[int]:
        """Get start values for month and year"""
        return map(int, self.date_now.strftime('%Y %m').split())

    def _update_dates_events(self):
        """Update date-events after changes"""
        return self._get_dates_events()

    def _get_dates_events(self) -> Dict[date, List[str]]:
        """Returns dates and lists of events for them"""

        def dict_union(
                dict1: Dict[Any, List], dict2: Dict[Any, List]
        ) -> Dict[Any, List]:
            """
            Takes two dicts with lists as value.
            Returns merged dict If taken dicts have some equal keys,
            in result dict, value for those keys will be sum of lists-values.
            """
            keys = set(list(dict1) + list(dict2))
            union_dict = {
                key: (dict1.get(key) or []) + (dict2.get(key) or []) for key
                in keys
            }
            return union_dict

        # get dates and events for them from db
        dates_events = {
            day.date_: self.event_class.repr_from_list(day.cycle_event)
            for day in self.date_class.get_dates()
        }
        # extract start-cycle dates
        start_cycle_dates = [
            day for day, events in dates_events.items()
            if 'cycle_start' in events
        ]
        # get date-events of predicted cycle-events
        predicted_cycle_events = self.calculator(
            start_cycle_dates
        ).get_predicted_events()
        res = dict_union(dates_events, predicted_cycle_events)
        return res

    def _get_dates(self) -> List[date]:
        """Create list of dates for the one month"""
        dates = list(self.calendar.itermonthdates(self._year, self._month))
        return dates

    def _enrich_dates(
            self
    ) -> List[Dict[str, Union[str, List[Optional[str]]]]]:
        """
        Convert list of dates to list of next dicts:
        {
          'date': <date item from list>,
          'event': <list of events, determined for date item or empty list>
        }
        """
        enriched_dates = [
            {
                'date': str(date_to_enrich),
                'events': self.dates_events.get(date_to_enrich) or []
            } for date_to_enrich in self._get_dates()
        ]
        return enriched_dates

    def set_cycle_start_date(self, event_date: str) -> None:
        """Write cycle start date to DB via date_class"""
        event_date = self._convert_date(event_date)
        self.date_class.set_date(event_date)
        self._update_dates_events()

    def remove_cycle_start_date(self, event_date: str) -> None:
        """Remove date of cycle start event from DB via event_class"""
        event_date = self._convert_date(event_date)
        self.event_class.remove_date_from_start_cycle(event_date)
        self._update_dates_events()

    @property
    def month(self) -> int:
        """Return month number"""
        return self._month

    @property
    def month_name(self) -> str:
        """Return month name"""
        return calendar.month_name[self.month]

    @property
    def year(self) -> int:
        """Return year number"""
        return self._year

    @month.setter
    def month(self, value: int) -> None:
        """
        Controls month number during stepping by one back and forth.
        Holds month number in range 0-12
        """
        self._month = value
        if self._month == 0:
            self._month = 12
            self._year -= 1
        if self._month == 13:
            self._month = 1
            self._year += 1

    def get_month_data(
            self
    ) -> Dict[str, Union[str, List[Dict[str, List[Optional[str]]]]]]:
        """Prepare month info to output"""
        data = {
            'days': self._enrich_dates(),
            'month': self.month_name,
            'year': self.year
        }
        return data
