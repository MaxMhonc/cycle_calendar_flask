import datetime

TEST_ONE_DATA_RANGE = {
    datetime.date(2021, 1, 11): ['cycle_middle'],
    datetime.date(2021, 1, 12): ['cycle_middle'],
    datetime.date(2021, 1, 13): ['cycle_middle'],
    datetime.date(2021, 1, 14): ['cycle_middle'],
    datetime.date(2021, 1, 15): ['cycle_middle'],
    datetime.date(2021, 1, 24): ['predicted_start4'],
    datetime.date(2021, 1, 25): ['predicted_start3'],
    datetime.date(2021, 1, 26): ['predicted_start2'],
    datetime.date(2021, 1, 27): ['predicted_start1'],
    datetime.date(2021, 1, 28): ['predicted_start0'],
    datetime.date(2021, 1, 29): ['predicted_start1'],
    datetime.date(2021, 1, 30): ['predicted_start2'],
    datetime.date(2021, 1, 31): ['predicted_start3'],
    datetime.date(2021, 2, 1): ['predicted_start4']
}
TEST_TWO_DATA_RANGE = {
    datetime.date(2021, 2, 12): ['cycle_middle'],
    datetime.date(2021, 2, 13): ['cycle_middle'],
    datetime.date(2021, 2, 14): ['cycle_middle'],
    datetime.date(2021, 2, 15): ['cycle_middle'],
    datetime.date(2021, 2, 16): ['cycle_middle'],
    datetime.date(2021, 3, 2): ['predicted_start4'],
    datetime.date(2021, 3, 3): ['predicted_start3'],
    datetime.date(2021, 3, 4): ['predicted_start2'],
    datetime.date(2021, 3, 5): ['predicted_start1'],
    datetime.date(2021, 3, 6): ['predicted_start0'],
    datetime.date(2021, 3, 7): ['predicted_start1'],
    datetime.date(2021, 3, 8): ['predicted_start2'],
    datetime.date(2021, 3, 9): ['predicted_start3'],
    datetime.date(2021, 3, 10): ['predicted_start4']
}
TEST_LONG_DATA_RANGE = {
    datetime.date(2021, 6, 29): ['cycle_middle'],
    datetime.date(2021, 6, 30): ['cycle_middle'],
    datetime.date(2021, 7, 1): ['cycle_middle'],
    datetime.date(2021, 7, 2): ['cycle_middle'],
    datetime.date(2021, 7, 3): ['cycle_middle'],
    datetime.date(2021, 7, 12): ['predicted_start4'],
    datetime.date(2021, 7, 13): ['predicted_start3'],
    datetime.date(2021, 7, 14): ['predicted_start2'],
    datetime.date(2021, 7, 15): ['predicted_start1'],
    datetime.date(2021, 7, 16): ['predicted_start0'],
    datetime.date(2021, 7, 17): ['predicted_start1'],
    datetime.date(2021, 7, 18): ['predicted_start2'],
    datetime.date(2021, 7, 19): ['predicted_start3'],
    datetime.date(2021, 7, 20): ['predicted_start4']
}
TEST_WITH_EVENTS_INTERSECTION = {
    datetime.date(2021, 2, 28): ['cycle_middle'],
    datetime.date(2021, 3, 1): ['cycle_middle'],
    datetime.date(2021, 3, 2): ['predicted_start4', 'cycle_middle'],
    datetime.date(2021, 3, 3): ['predicted_start3', 'cycle_middle'],
    datetime.date(2021, 3, 4): ['predicted_start2', 'cycle_middle'],
    datetime.date(2021, 3, 5): ['predicted_start1'],
    datetime.date(2021, 3, 6): ['predicted_start0'],
    datetime.date(2021, 3, 7): ['predicted_start1'],
    datetime.date(2021, 3, 8): ['predicted_start2'],
    datetime.date(2021, 3, 9): ['predicted_start3'],
    datetime.date(2021, 3, 10): ['predicted_start4']
}
