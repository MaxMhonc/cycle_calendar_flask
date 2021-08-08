from datetime import date, timedelta
from typing import List, Optional, Tuple, Dict


class CycleCalculator:
    """
    CycleCalculator calculates possible next cycle beginning dates and cycle
    middle dates.
    init constants:
    period_for_average - number of cycles to calculate average;
    default_delta - standard average distance between cycles;
    middle_delta - standard average distance between start cycle and
                   start ovulation
    ovulation_period - standard average ovulation length in days
    Value of all constants should be clarified via medical sources.
    """
    # variable "predicted_types" contain type names for possible
    # cycle start dates as events. predicted_start0 corresponds to the most
    # opportune start date, predicted_start4 - the less opportune,
    # which limits cycle start range as predicted_start0 +/- predicted_start4.
    predicted_types = (
        'predicted_start0',
        'predicted_start1',
        'predicted_start2',
        'predicted_start3',
        'predicted_start4'
    )

    def __init__(
            self,
            dates_range: List[Optional[date]],
            period_for_average: int = 6,
            default_delta: int = 27,
            middle_delta: int = 10,
            ovulation_period: int = 5
    ) -> None:
        self.dates_range = (
            dates_range if len(dates_range) <= 6 else dates_range[-6:]
        )
        self.last_cycle_date = dates_range[-1] if dates_range else None
        self.period_for_average = (
            period_for_average if period_for_average < len(dates_range)
            else len(dates_range)
        )
        self.default_delta = timedelta(days=default_delta)
        self.middle_delta = timedelta(days=middle_delta)
        self.ovulation_period = ovulation_period

    def get_one_day_events(self, date_: date) -> List[str]:
        """Return predicted cycle events for input date"""
        event = self.get_predicted_events()[date_]
        return event
    
    def get_predicted_events(self) -> Dict[date, List[str]]:
        """Gathers event dates and types to final output format.
        Adds {'type': 'cycle_middle'} to cycle_middle events."""
        events = {}
        for day_near, type_ in enumerate(self.predicted_types):
            dates = self._calculate_prediction(day_near)
            for d in dates:
                events[d] = [type_]
        for day in self._calculate_middle():
            if events.get(day):
                events[day] += ['cycle_middle']
            else:
                events[day] = ['cycle_middle']
        print('AAAA!!!!! I WAE CALLED!!!!')
        return events

    def _calculate_delta(self) -> timedelta:
        """Calculates average distance between cycles if number of its > 1,
        else - returns default."""
        if not self.dates_range or len(self.dates_range) < 2:
            return self.default_delta
        sum_delta = sum(
            [d - self.dates_range[i - 1]
             for i, d in enumerate(self.dates_range[1:], 1)], timedelta()
        )
        res = sum_delta / (self.period_for_average - 1)
        return res

    def _calculate_prediction(
            self, days_near: int = 0) -> Tuple[date, ...]:
        """Calculate predicted cycle start dates.
           days_near = 0 for most opportune start date."""
        calculated_delta = self._calculate_delta()
        days_near = timedelta(days=days_near)
        if not self.last_cycle_date:
            return ()
        predicted_dates = {
            self.last_cycle_date + calculated_delta + days_near,
            self.last_cycle_date + calculated_delta - days_near
        }
        return tuple(predicted_dates)

    def _calculate_middle(self) -> Tuple[date, ...]:
        """Calculate predicted cycle middle dates."""
        if not self.last_cycle_date:
            return ()
        middle_range = [
            self.last_cycle_date + self.middle_delta + timedelta(days=i)
            for i in range(self.ovulation_period)
        ]
        return tuple(middle_range)
