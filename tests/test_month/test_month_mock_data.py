from datetime import date

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