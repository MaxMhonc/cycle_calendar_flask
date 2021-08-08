from datetime import datetime, timedelta
from typing import List, Tuple


# def calc_pred_100_delta(dates: List[datetime.date]) -> timedelta:
#     """"""
#     timedelta_sum = timedelta()
#
#     if len(dates) < 2:
#         return timedelta(days=27)
#
#     for i, date_ in enumerate(dates[1:], 1):
#         timedelta_sum += date_ - dates[i - 1]
#
#     res = timedelta_sum / len(dates)
#     return res


def calc_predicted_cycle_start(
        start_cycle_day: datetime.date,
        predict_cycle_delta: timedelta,
        days_near=0
) -> Tuple[datetime.date, ...]:
    """"""
    dates = {
        start_cycle_day + predict_cycle_delta + timedelta(days=days_near),
        start_cycle_day + predict_cycle_delta - timedelta(days=days_near)
    }
    return tuple(dates)


def calc_cycle_middle(
        start_cycle_day: datetime.date,
        middle_start: int
) -> Tuple[datetime.date, ...]:
    """"""
    cycle_middle_range = [
        start_cycle_day + timedelta(days=middle_start) + timedelta(days=i)
        for i in range(5)
    ]
    return tuple(cycle_middle_range)
