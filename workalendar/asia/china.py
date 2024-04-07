from datetime import date
import warnings

from ..core import ChineseNewYearCalendar
from ..registry_tools import iso_register
from ..exceptions import CalendarError

holidays = {
    2018:
        {
            'Ching Ming Festival': [(4, 5), (4, 6), (4, 7)],
            'Labour Day Holiday': [(4, 29), (4, 30), (5, 1)],
            'Dragon Boat Festival': [(6, 18)],
            'Mid-Autumn Festival': [(9, 24)],
            'New year': [(12, 30), (12, 31)]
        },
    2019:
        {
            'Ching Ming Festival': [(4, 5)],
            'Labour Day Holiday': [(5, 1), (5, 2), (5, 3)],
            'Dragon Boat Festival': [(6, 7)],
            'Mid-Autumn Festival': [(9, 13)]
        },
    2020:
        {
            'Ching Ming Festival': [(4, 4), (4, 5), (4, 6)],
            'Labour Day Holiday': [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
            'Dragon Boat Festival': [(6, 25), (6, 26), (6, 27)],
            'National Day': [(10, 8)]
        },
    2021:
        {
            'Ching Ming Festival': [(4, 3), (4, 4), (4, 5)],
            'Labour Day Holiday': [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)],
            'Dragon Boat Festival': [(6, 12), (6, 13), (6, 14)],
            'Mid-Autumn Festival': [(9, 19), (9, 20), (9, 21)]
        },
    2022:
        {
            'Ching Ming Festival': [(4, 3), (4, 4), (4, 5)],
            'Labour Day Holiday': [(4, 30), (5, 1), (5, 2), (5, 3), (5, 4)],
            'Dragon Boat Festival': [(6, 3), (6, 4), (6, 5)],
            'Mid-Autumn Festival': [(9, 10), (9, 11), (9, 12)]
        },
    2023:
        {
            'Ching Ming Festival': [(4, 5)],
            'Labour Day Holiday': [(4, 29), (4, 30), (5, 1), (5, 2), (5, 3)],
            'Dragon Boat Festival': [(6, 22), (6, 23), (6, 24)],
            'Mid-Autumn Festival': [(9, 29)],
            'National Day': [(9, 30)]
        },
    2024:
        {
            'Spring Festival': [(2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17)],
            'Ching Ming Festival':[(4,4),(4,5),(4,6)],
            'Labour Day Holiday': [(5, 1), (5, 2), (5, 3), (5,4), (5, 5)],
            'Dragon Boat Festival': [(6,8),(6, 9),(6,10)],
            'Mid-Autumn Festival': [(9,15),(9,16),(9,17)],
            'National Day': [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7)],
            'New year': [(1,1)]
        }
}

workdays = {
    2018:
        {
            'Spring Festival Shift': [(2, 11), (2, 24)],
            'Ching Ming Festival Shift': [(4, 8)],
            'Labour Day Holiday Shift': [(4, 28)],
            'National Day Shift': [(9, 29), (9, 30)],
            'New year Shift': [(12, 29)]
        },
    2019:
        {
            'Spring Festival Shift': [(2, 2), (2, 3)],
            'Labour Day Holiday Shift': [(4, 28), (5, 5)],
            'National Day Shift': [(9, 29), (10, 12)],
        },
    2020:
        {
            'Spring Festival Shift': [(1, 19), (2, 1)],
            'Labour Day Holiday Shift': [(4, 26), (5, 9)],
            'Dragon Boat Festival Shift': [(6, 28)],
            'National Day Shift': [(9, 27), (10, 10)]
        },
    2021:
        {
            'Spring Festival Shift': [(2, 7), (2, 20)],
            'Labour Day Holiday Shift': [(4, 25), (5, 8)],
            'Mid-Autumn Festival Shift': [(9, 18)],
            'National Day Shift': [(9, 26), (10, 9)]
        },
    2022:
        {
            'Spring Festival Shift': [(1, 29), (1, 30)],
            'Ching Ming Festival Shift': [(4, 2)],
            'Labour Day Holiday Shift': [(4, 24), (5, 7)],
            'National Day Shift': [(10, 8), (10, 9)]
        },
    2023:
        {
            'Spring Festival Shift': [(1, 28), (1, 29)],
            'Labour Day Holiday Shift': [(4, 23), (5, 6)],
            'Dragon Boat Festival Shift': [(6, 25)],
            'National Day Shift': [(10, 7), (10, 8)]
        },
    2024:
        {
           'Spring Festival Shift': [(2, 4), (2,18)],
           'Ching Ming Festival Shift': [(4,7)],
           'Labour Day Holiday Shift': [(4,28), (5,11)],
           'Dragon Boat Festival Shift':[],
           'Mid-Autumn Festival Shift':[(9,14)],
           'National Day Shift': [(9,29),(10,12)],
           'New year Shift': []
        }
}


@iso_register('CN')
class China(ChineseNewYearCalendar):
    "China"
    # WARNING: Support 2018-2023 currently, need update every year.
    shift_new_years_day = True
    include_chinese_new_year_eve = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra_working_days = []
        for year, data in workdays.items():
            for holiday_name, day_list in data.items():
                for v in day_list:
                    self.extra_working_days.append(date(year, v[0], v[1]))

    def get_calendar_holidays(self, year):
        year_min, year_max = min(holidays), max(holidays)
        warnings.warn(
            f"Support years {year_min}-{year_max} currently, "
            f"need update every year."
        )
        if year not in holidays:
            msg = f"Need configure {year} for China."
            raise CalendarError(msg)
        return super().get_calendar_holidays(year)

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        # Spring Festival, eve, 1.1, and 1.2 - 1.6 in lunar day
        for i in range(2, 7):
            days.append((ChineseNewYearCalendar.lunar(year, 1, i),
                         "Spring Festival"))
        # National Days, 10.1 - 10.7 in general
        for i in range(1, 8):
            if date(year, 10, i) not in self.extra_working_days:
                days.append((date(year, 10, i), "National Day"))

        # other holidays
        for holiday_name, day_list in holidays[year].items():
            for v in day_list:
                days.append((date(year, v[0], v[1]), holiday_name))
        return days

    def is_working_day(self, day,
                       extra_working_days=None, extra_holidays=None):
        extra_working_days = extra_working_days or self.extra_working_days
        return super().is_working_day(day, extra_working_days, extra_holidays)

    def add_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        extra_working_days = extra_working_days or self.extra_working_days
        return super().add_working_days(day, delta,
                                        extra_working_days,
                                        extra_holidays,
                                        keep_datetime)

    def sub_working_days(self, day, delta,
                         extra_working_days=None, extra_holidays=None,
                         keep_datetime=False):
        extra_working_days = extra_working_days or self.extra_working_days
        return super().sub_working_days(day, delta,
                                        extra_working_days,
                                        extra_holidays,
                                        keep_datetime)
