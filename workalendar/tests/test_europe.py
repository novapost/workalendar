from datetime import date, timedelta, datetime
from collections import Counter
from unittest import TestCase

from . import GenericCalendarTest
from ..core import daterange, ISO_SAT
from ..europe import (
    Austria,
    Bulgaria,
    Belarus,
    Belgium,
    CaymanIslands,
    Croatia,
    Cyprus,
    CzechRepublic,
    Denmark,
    Slovakia,
    Finland,
    Estonia,
    Sweden,
    France, FranceAlsaceMoselle,
    Georgia,
    Greece,
    Guernsey,
    Hungary,
    Iceland,
    Ireland,
    Italy,
    Latvia,
    Lithuania,
    Luxembourg,
    Malta,
    Monaco,
    Netherlands,
    NetherlandsWithSchoolHolidays,
    Norway,
    Poland,
    Portugal,
    Romania,
    Russia,
    Serbia,
    Slovenia,
    Ukraine,
    UnitedKingdom,
    UnitedKingdomNorthernIreland,
    EuropeanCentralBank,
)
# Tests dedicated to Netherlands School holidays
from ..europe.netherlands import (
    SPRING_HOLIDAYS_EARLY_REGIONS,
    SUMMER_HOLIDAYS_EARLY_REGIONS,
    SUMMER_HOLIDAYS_LATE_REGIONS,
)


class AustriaTest(GenericCalendarTest):
    cal_class = Austria

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # New Years day
        self.assertIn(date(2016, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2016, 3, 28), holidays)  # easter monday
        self.assertIn(date(2016, 5, 1), holidays)  # National Holiday
        self.assertIn(date(2016, 5, 5), holidays)  # Ascension Day
        self.assertIn(date(2016, 5, 16), holidays)  # Whit monday
        self.assertIn(date(2016, 5, 26), holidays)  # Corpus Christi
        self.assertIn(date(2016, 8, 15), holidays)  # Assumption
        self.assertIn(date(2016, 10, 26), holidays)  # national day again
        self.assertIn(date(2016, 11, 1), holidays)  # all saints
        self.assertIn(date(2016, 12, 8), holidays)  # Immaculate conception
        self.assertIn(date(2016, 12, 25), holidays)  # Xmas
        self.assertIn(date(2016, 12, 26), holidays)  # St Stephens

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(holidays[date(2020, 5, 1)], "State Holiday")
        # a.k.a. Staatsfeiertag


class BelarusTest(GenericCalendarTest):
    cal_class = Belarus

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)  # New Years day
        self.assertIn(date(2019, 1, 2), holidays)  # Day after NYE
        self.assertIn(date(2019, 1, 7), holidays)  # Christmas (Orthodox)
        self.assertIn(date(2019, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2019, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2019, 5, 7), holidays)  # Radonitsa
        self.assertIn(date(2019, 5, 9), holidays)  # Victory Day
        self.assertIn(date(2019, 7, 3), holidays)  # Republic Day
        self.assertIn(date(2019, 11, 7), holidays)  # October Revolution Day
        self.assertIn(date(2019, 12, 25), holidays)  # Christmas (Catholic)

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New Years day
        self.assertIn(date(2020, 1, 2), holidays)  # Day after NYE
        self.assertIn(date(2020, 1, 7), holidays)  # Christmas (Orthodox)
        self.assertIn(date(2020, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2020, 4, 28), holidays)  # Radonitsa
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 9), holidays)  # Victory Day
        self.assertIn(date(2020, 7, 3), holidays)  # Republic Day
        self.assertIn(date(2020, 11, 7), holidays)  # October Revolution Day
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas (Catholic)


class BulgariaTest(GenericCalendarTest):
    cal_class = Bulgaria

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "International Workers' Day")

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2019, 3, 3), holidays)  # Liberation Day
        self.assertIn(date(2019, 3, 4), holidays)  # Liberation Day (shift)

        self.assertIn(date(2019, 4, 26), holidays)  # Good Friday
        self.assertIn(date(2019, 4, 27), holidays)  # Holy Saturday
        self.assertIn(date(2019, 4, 28), holidays)  # Easter day (sunday)
        self.assertIn(date(2019, 4, 29), holidays)  # Easter Monday

        self.assertIn(date(2019, 5, 1), holidays)  # International Workers' day
        self.assertIn(date(2019, 5, 6), holidays)  # St George's Day
        self.assertIn(date(2019, 5, 24), holidays)  # St Cyril & Methodius
        self.assertIn(date(2019, 9, 6), holidays)  # Unification Day

        self.assertIn(date(2019, 9, 22), holidays)  # Independence Day
        self.assertIn(date(2019, 9, 23), holidays)  # Independence Day (shift)

        self.assertIn(date(2019, 12, 24), holidays)  # Christmas Eve
        self.assertIn(date(2019, 12, 25), holidays)  # Christmas 1 (FRI)
        self.assertIn(date(2019, 12, 26), holidays)  # Christmas 2 (SAT)

    def test_holidays_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2020, 3, 3), holidays)  # Liberation Day
        self.assertIn(date(2020, 4, 17), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 18), holidays)  # Holy Saturday
        self.assertIn(date(2020, 4, 19), holidays)  # Easter day (sunday)
        self.assertIn(date(2020, 4, 20), holidays)  # Easter Monday

        self.assertIn(date(2020, 5, 1), holidays)  # International Workers' day
        self.assertIn(date(2020, 5, 6), holidays)  # St George's Day
        self.assertIn(date(2020, 5, 24), holidays)  # St Cyril & Methodius
        self.assertIn(date(2020, 5, 25), holidays)  # (shift)
        self.assertIn(date(2020, 9, 6), holidays)  # Unification Day
        self.assertIn(date(2020, 9, 7), holidays)  # Unification Day (shift)

        self.assertIn(date(2020, 9, 22), holidays)  # Independence Day

        self.assertIn(date(2020, 12, 24), holidays)  # Christmas Eve
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas 1 (FRI)
        self.assertIn(date(2020, 12, 26), holidays)  # Christmas 2 (SAT)
        self.assertIn(date(2020, 12, 28), holidays)  # Christmas 2b (shift)

    def test_holidays_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2021, 3, 3), holidays)  # Liberation Day
        self.assertIn(date(2021, 4, 30), holidays)  # Good Friday
        self.assertIn(date(2021, 5, 1), holidays)  # Holy Saturday
        self.assertIn(date(2021, 5, 2), holidays)  # Easter day (sunday)
        self.assertIn(date(2021, 5, 3), holidays)  # Easter Monday
        # International Workers' day (in lieu, because easter)
        self.assertIn(date(2021, 5, 4), holidays)
        self.assertIn(date(2021, 5, 6), holidays)  # St George's Day

        self.assertIn(date(2021, 5, 24), holidays)  # St Cyril & Methodius
        self.assertIn(date(2021, 9, 6), holidays)  # Unification Day
        self.assertIn(date(2021, 9, 22), holidays)  # Independence Day

        self.assertIn(date(2021, 12, 24), holidays)  # Christmas Eve
        self.assertIn(date(2021, 12, 25), holidays)  # Christmas 1 (SAT)
        self.assertIn(date(2021, 12, 26), holidays)  # Christmas 2
        self.assertIn(date(2021, 12, 27), holidays)  # Christmas 2b
        self.assertIn(date(2021, 12, 28), holidays)  # Christmas 2c

    def test_holidays_2022(self):
        holidays = self.cal.holidays_set(2022)
        self.assertIn(date(2022, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2022, 1, 3), holidays)  # New Year's Day (shift)
        self.assertIn(date(2022, 3, 3), holidays)  # Liberation Day
        self.assertIn(date(2022, 4, 22), holidays)  # Good Friday
        self.assertIn(date(2022, 4, 23), holidays)  # Holy Saturday
        self.assertIn(date(2022, 4, 24), holidays)  # Easter day (sunday)
        self.assertIn(date(2022, 4, 25), holidays)  # Easter Monday

        self.assertIn(date(2022, 5, 1), holidays)  # International Workers' day
        self.assertIn(date(2022, 5, 2), holidays)  # Labour day Shift
        self.assertIn(date(2022, 5, 6), holidays)  # St George's Day

        self.assertIn(date(2022, 5, 24), holidays)  # St Cyril & Methodius
        self.assertIn(date(2022, 9, 6), holidays)  # Unification Day
        self.assertIn(date(2022, 9, 22), holidays)  # Independence Day

        self.assertIn(date(2022, 12, 24), holidays)  # Christmas Eve
        self.assertIn(date(2022, 12, 25), holidays)  # Christmas 1 (SAT)
        self.assertIn(date(2022, 12, 26), holidays)  # Christmas 2
        self.assertIn(date(2022, 12, 27), holidays)  # Christmas 2b
        self.assertIn(date(2022, 12, 28), holidays)  # Christmas 2c


class CaymanIslandsTest(GenericCalendarTest):
    cal_class = CaymanIslands

    def test_holidays_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 28), holidays)  # National Heroes Day
        self.assertIn(date(2013, 2, 13), holidays)   # Ash Wednesday
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 20), holidays)  # Discovery Day
        self.assertIn(date(2013, 6, 17), holidays)  # Queen's Birthday
        self.assertIn(date(2013, 7, 1), holidays)   # Constitution Day
        self.assertIn(date(2013, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_holidays_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 27), holidays)  # National Heroes Day
        self.assertIn(date(2014, 3, 5), holidays)   # Ash Wednesday
        self.assertIn(date(2014, 4, 18), holidays)  # good friday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 19), holidays)  # Discovery Day
        self.assertIn(date(2014, 6, 16), holidays)  # Queen's Birthday
        self.assertIn(date(2014, 7, 7), holidays)   # Constitution Day
        self.assertIn(date(2014, 11, 10), holidays)  # Remembrance Day
        self.assertIn(date(2014, 12, 25), holidays)  # XMas
        self.assertIn(date(2014, 12, 26), holidays)  # Boxing Day (on week-end)

    def test_holidays_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 26), holidays)  # National Heroes Day
        self.assertIn(date(2015, 2, 18), holidays)   # Ash Wednesday
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 6), holidays)  # easter monday
        self.assertIn(date(2015, 5, 18), holidays)  # Discovery Day
        self.assertIn(date(2015, 6, 15), holidays)  # Queen's Birthday
        self.assertIn(date(2015, 7, 6), holidays)   # Constitution Day
        self.assertIn(date(2015, 11, 9), holidays)  # Remembrance Day
        self.assertIn(date(2015, 12, 25), holidays)  # XMas
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing Day (on week-end)
        self.assertIn(date(2015, 12, 28), holidays)  # Boxing Day observed

    def test_holidays_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 25), holidays)  # National Heroes Day
        self.assertIn(date(2016, 2, 10), holidays)   # Ash Wednesday
        self.assertIn(date(2016, 3, 25), holidays)  # good friday
        self.assertIn(date(2016, 3, 28), holidays)  # easter monday
        self.assertIn(date(2016, 5, 16), holidays)  # Discovery Day
        self.assertIn(date(2016, 6, 13), holidays)  # Queen's Birthday
        self.assertIn(date(2016, 7, 4), holidays)   # Constitution Day
        self.assertIn(date(2016, 11, 14), holidays)  # Remembrance Day
        self.assertIn(date(2016, 12, 26), holidays)  # XMas (in lieu)
        self.assertIn(date(2016, 12, 27), holidays)  # Boxing Day (in lieu)

    def test_holidays_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)
        self.assertIn(date(2017, 1, 2), holidays)  # New Year boxing
        self.assertIn(date(2017, 1, 23), holidays)  # National Heroes Day
        self.assertIn(date(2017, 3, 1), holidays)   # Ash Wednesday
        self.assertIn(date(2017, 4, 14), holidays)  # good friday
        self.assertIn(date(2017, 4, 17), holidays)  # easter monday
        self.assertIn(date(2017, 5, 15), holidays)  # Discovery Day
        self.assertIn(date(2017, 5, 24), holidays)  # Election Day
        self.assertIn(date(2017, 6, 19), holidays)  # Queen's Birthday
        self.assertIn(date(2017, 7, 3), holidays)   # Constitution Day
        self.assertIn(date(2017, 11, 13), holidays)  # Remembrance Day
        self.assertIn(date(2017, 12, 25), holidays)  # XMas
        self.assertIn(date(2017, 12, 26), holidays)  # Boxing Day

    def test_holidays_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)
        self.assertIn(date(2018, 1, 22), holidays)  # National Heroes Day
        self.assertIn(date(2018, 2, 14), holidays)   # Ash Wednesday
        self.assertIn(date(2018, 3, 30), holidays)  # good friday
        self.assertIn(date(2018, 4, 2), holidays)  # easter monday
        self.assertIn(date(2018, 5, 21), holidays)  # Discovery Day
        self.assertIn(date(2018, 6, 11), holidays)  # Queen's Birthday
        self.assertIn(date(2018, 7, 2), holidays)   # Constitution Day
        self.assertIn(date(2018, 11, 12), holidays)  # Remembrance Day
        self.assertIn(date(2018, 12, 25), holidays)  # XMas
        self.assertIn(date(2018, 12, 26), holidays)  # Boxing Day

    def test_holidays_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)
        self.assertIn(date(2019, 1, 28), holidays)  # National Heroes Day
        self.assertIn(date(2019, 3, 6), holidays)   # Ash Wednesday
        self.assertIn(date(2019, 4, 19), holidays)  # good friday
        self.assertIn(date(2019, 4, 22), holidays)  # easter monday
        self.assertIn(date(2019, 5, 20), holidays)  # Discovery Day
        self.assertIn(date(2019, 6, 10), holidays)  # Queen's Birthday
        self.assertIn(date(2019, 7, 1), holidays)   # Constitution Day
        self.assertIn(date(2019, 11, 11), holidays)  # Remembrance Day
        self.assertIn(date(2019, 12, 25), holidays)  # XMas
        self.assertIn(date(2019, 12, 26), holidays)  # Boxing Day

    def test_holidays_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)
        self.assertIn(date(2020, 1, 27), holidays)  # National Heroes Day
        self.assertIn(date(2020, 2, 26), holidays)   # Ash Wednesday
        self.assertIn(date(2020, 4, 10), holidays)  # good friday
        self.assertIn(date(2020, 4, 13), holidays)  # easter monday
        self.assertIn(date(2020, 5, 18), holidays)  # Discovery Day
        self.assertIn(date(2020, 6, 15), holidays)  # Queen's Birthday
        self.assertIn(date(2020, 7, 6), holidays)   # Constitution Day
        self.assertIn(date(2020, 11, 9), holidays)  # Remembrance Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # Boxing Day


class CroatiaTest(GenericCalendarTest):
    cal_class = Croatia

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # New Year's Day
        self.assertIn(date(2016, 1, 6), holidays)   # Epiphany / Bogojavljenje
        self.assertIn(date(2016, 3, 27), holidays)  # Easter Sunday
        self.assertIn(date(2016, 3, 28), holidays)  # Easter Monday
        self.assertIn(date(2016, 5, 1), holidays)   # Intl Workers' Day
        self.assertIn(date(2016, 5, 26), holidays)  # Corpus Christi / Tijelovo
        self.assertIn(date(2016, 6, 22), holidays)  # Anti-Fascist Day
        self.assertIn(date(2016, 6, 25), holidays)  # Statehood Day
        self.assertIn(date(2016, 8, 5), holidays)   # Victory & Homeland Thanks
        self.assertIn(date(2016, 8, 15), holidays)  # Assumption of Mary
        self.assertIn(date(2016, 10, 8), holidays)  # Independence Day Dan neov
        self.assertIn(date(2016, 11, 1), holidays)  # All Saints' Day Dan svih
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas Božić
        self.assertIn(date(2016, 12, 26), holidays)  # St. Stephen's Day Prvi d

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)   # New Year's Day
        self.assertIn(date(2020, 1, 6), holidays)   # Epiphany / Bogojavljenje
        self.assertIn(date(2020, 4, 12), holidays)  # Easter Sunday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 30), holidays)  # Statehood day
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 6, 22), holidays)  # Anti-Fascist Day
        # Victory & Homeland Thanksgiving
        self.assertIn(date(2020, 8, 5), holidays)
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption of Mary
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2020, 11, 18), holidays)  # Remembrance Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # St Stephen

    def test_statehood_day(self):
        holidays_2019 = self.cal.holidays_set(2019)
        holidays_2020 = self.cal.holidays_set(2020)

        # Statehood day was a holiday on June 25th until 2020
        self.assertIn(date(2019, 6, 25), holidays_2019)
        self.assertNotIn(date(2020, 6, 25), holidays_2020)

        # Statehood day as of 2020 happens on May 30th
        self.assertNotIn(date(2019, 5, 30), holidays_2019)
        self.assertIn(date(2020, 5, 30), holidays_2020)

    def test_independance_day(self):
        # Independence Day was a holiday until 2020
        holidays_2019 = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 10, 8), holidays_2019)
        holidays_2020 = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 10, 8), holidays_2020)

    def test_remembrance_day(self):
        # Remembrance Day was introduced as of 2020
        holidays_2018 = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 11, 18), holidays_2018)
        holidays_2019 = self.cal.holidays_set(2019)
        self.assertNotIn(date(2019, 11, 18), holidays_2019)
        holidays_2020 = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 11, 18), holidays_2020)

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "International Workers' Day")


class CyprusTest(GenericCalendarTest):
    cal_class = Cyprus

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)    # New Year's Day
        self.assertIn(date(2017, 1, 6), holidays)    # Epiphany
        self.assertIn(date(2017, 2, 27), holidays)   # Green Monday
        self.assertIn(date(2017, 3, 25), holidays)   # Greek Independence Day
        self.assertIn(date(2017, 4, 1), holidays)    # Cyprus National Holiday
        self.assertIn(date(2017, 4, 14), holidays)   # Good Friday (Orthodox)
        self.assertIn(date(2017, 4, 17), holidays)   # Easter Monday (Orthodox)
        self.assertIn(date(2017, 4, 18), holidays)   # Easter Tues banks only
        self.assertIn(date(2017, 5, 1), holidays)    # Labour Day/May Day
        self.assertIn(date(2017, 6, 5), holidays)    # Orthodox Pentecost Mon
        self.assertIn(date(2017, 7, 15), holidays)   # Assumption
        self.assertIn(date(2017, 10, 1), holidays)   # Cyprus Independence Day
        self.assertIn(date(2017, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2017, 12, 26), holidays)  # Boxing Day


class CzechRepublicTest(GenericCalendarTest):
    cal_class = CzechRepublic

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 7, 6), holidays)
        self.assertIn(date(2013, 9, 28), holidays)
        self.assertIn(date(2013, 10, 28), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)

    def test_year_good_friday(self):
        # Good Friday not yet a holiday before 2016
        holidays = self.cal.holidays_set(2015)
        self.assertNotIn(date(2015, 4, 3), holidays)
        # Good friday will be a holiday as of 2016
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 3, 25), holidays)


class DenmarkTest(GenericCalendarTest):
    cal_class = Denmark

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)    # Nytaarsdag
        self.assertIn(date(2015, 4, 2), holidays)    # Skærtorsdag
        self.assertIn(date(2015, 4, 3), holidays)    # Langfredag
        self.assertIn(date(2015, 4, 5), holidays)    # Paaskedag
        self.assertIn(date(2015, 4, 6), holidays)    # 2. paaskedag
        self.assertIn(date(2015, 5, 1), holidays)    # St bededag
        self.assertIn(date(2015, 5, 14), holidays)   # Kristi himmelfart
        self.assertIn(date(2015, 5, 24), holidays)   # Pinsedag
        self.assertIn(date(2015, 5, 25), holidays)   # 2. pinsedag
        self.assertIn(date(2015, 12, 24), holidays)  # Juleaften
        self.assertIn(date(2015, 12, 25), holidays)  # Juledag
        self.assertIn(date(2015, 12, 26), holidays)  # 2. juledag

    def test_year_2024(self):
        holidays = self.cal.holidays_set(2024)
        self.assertIn(date(2024, 1, 1), holidays)    # Nytaarsdag
        self.assertIn(date(2024, 3, 28), holidays)   # Skærtorsdag
        self.assertIn(date(2024, 3, 29), holidays)   # Langfredag
        self.assertIn(date(2024, 3, 31), holidays)   # Paaskedag
        self.assertIn(date(2024, 4, 1), holidays)    # 2. paaskedag
        # Store bededag is not a public holiday since 2024
        self.assertNotIn(date(2024, 4, 26), holidays)
        self.assertIn(date(2024, 5, 9), holidays)    # Kristi himmelfart
        self.assertIn(date(2024, 5, 19), holidays)   # Pinsedag
        self.assertIn(date(2024, 5, 20), holidays)   # 2. pinsedag
        self.assertIn(date(2024, 12, 24), holidays)  # Juleaften
        self.assertIn(date(2024, 12, 25), holidays)  # Juledag
        self.assertIn(date(2024, 12, 26), holidays)  # 2. juledag


class SlovakiaTest(GenericCalendarTest):
    cal_class = Slovakia

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 6), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 8, 29), holidays)
        self.assertIn(date(2013, 9, 1), holidays)
        self.assertIn(date(2013, 9, 15), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)

    def test_removed_duplicate(self):
        holidays = self.cal.holidays(2017)
        counter = Counter(day for day, label in holidays)
        # Only one "all saints"
        self.assertEqual(counter[date(2017, 11, 1)], 1)
        # Only one "XMas eve"
        self.assertEqual(counter[date(2017, 12, 24)], 1)
        # De-duplicate, XMas day was configured twice.
        # Refs #205.
        self.assertEqual(counter[date(2017, 12, 25)], 1)
        # Only one St Stephen
        self.assertEqual(counter[date(2017, 12, 25)], 1)


class SwedenTest(GenericCalendarTest):
    cal_class = Sweden

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 6), holidays)  # national day
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints
        self.assertIn(date(2013, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2013, 12, 25), holidays)  # xmas day
        self.assertIn(date(2013, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2013, 12, 31), holidays)  # new year's eve

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # new year
        self.assertIn(date(2014, 1, 6), holidays)  # epiphany
        self.assertIn(date(2014, 4, 18), holidays)  # good friday
        self.assertIn(date(2014, 4, 20), holidays)  # easter sunday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # may day
        self.assertIn(date(2014, 5, 29), holidays)  # ascension
        self.assertIn(date(2014, 6, 6), holidays)  # national day
        self.assertIn(date(2014, 6, 8), holidays)  # pentecost
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints
        self.assertIn(date(2014, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2014, 12, 25), holidays)  # xmas day
        self.assertIn(date(2014, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2014, 12, 31), holidays)  # new year's eve

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # new year
        self.assertIn(date(2015, 1, 6), holidays)  # epiphany
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 5), holidays)  # easter sunday
        self.assertIn(date(2015, 4, 6), holidays)  # easter monday
        self.assertIn(date(2015, 5, 1), holidays)  # may day
        self.assertIn(date(2015, 5, 14), holidays)  # ascension
        self.assertIn(date(2015, 5, 24), holidays)  # pentecost
        self.assertIn(date(2015, 6, 6), holidays)  # national day
        self.assertIn(date(2015, 6, 19), holidays)  # midsummer eve
        self.assertIn(date(2015, 6, 20), holidays)  # midsummer day
        self.assertIn(date(2015, 10, 31), holidays)  # all saints
        self.assertIn(date(2015, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2015, 12, 25), holidays)  # xmas day
        self.assertIn(date(2015, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2015, 12, 31), holidays)  # new year's eve

    def test_pentecost(self):
        holidays = self.cal.holidays(2015)
        self.assertIn((date(2015, 5, 24), 'Pentecost'), holidays)


class FinlandTest(GenericCalendarTest):
    cal_class = Finland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints (special)
        self.assertIn(date(2013, 12, 6), holidays)  # Independence day
        self.assertIn(date(2013, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens

    def test_year_2014(self):
        # testing the special rule variable holidays
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints (special)


class FranceTest(GenericCalendarTest):

    cal_class = France

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 4, 1), holidays)   # easter
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 8), holidays)   # 39-45
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 20), holidays)  # Pentecote
        self.assertIn(date(2013, 7, 14), holidays)  # Nation day
        self.assertIn(date(2013, 8, 15), holidays)  # Assomption
        self.assertIn(date(2013, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

    def test_working_days(self):
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 1)))  # holiday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 5)))  # saturday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 6)))  # sunday
        self.assertTrue(self.cal.is_working_day(date(2013, 1, 7)))   # monday

    def test_business_days_computations(self):
        day = date(2013, 10, 30)
        self.assertEqual(
            self.cal.add_working_days(day, 0), date(2013, 10, 30))
        self.assertEqual(
            self.cal.add_working_days(day, 1), date(2013, 10, 31))
        self.assertEqual(self.cal.add_working_days(day, 2), date(2013, 11, 4))
        self.assertEqual(self.cal.add_working_days(day, 3), date(2013, 11, 5))


class FranceAlsaceMoselleTest(FranceTest):
    cal_class = FranceAlsaceMoselle

    def test_year_2013(self):
        super().test_year_2013()
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 29), holidays)  # Good friday
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_working_days(self):
        super().test_working_days()

    def test_business_days_computations(self):
        super().test_business_days_computations()


class GeorgiaTest(GenericCalendarTest):
    cal_class = Georgia

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)

        self.assertIn(date(2016, 1, 1), holidays)  # New Year
        self.assertIn(date(2016, 1, 2), holidays)  # Second day of the New Year
        self.assertIn(date(2016, 1, 7), holidays)  # Orthodox Christmas
        self.assertIn(date(2016, 1, 19), holidays)  # Orthodox Epiphany
        self.assertIn(date(2016, 3, 3), holidays)  # Mother's Day
        self.assertIn(date(2016, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2016, 4, 9), holidays)  # Day of National Unity
        self.assertIn(date(2016, 4, 29), holidays)  # Orthodox Good Friday
        self.assertIn(date(2016, 4, 30), holidays)  # Great Saturday
        self.assertIn(date(2016, 5, 1), holidays)  # Orthodox Easter Day
        self.assertIn(date(2016, 5, 2), holidays)  # Orthodox Easter Monday
        self.assertIn(date(2016, 5, 9), holidays)  # Day of victory
        self.assertIn(date(2016, 5, 12), holidays)  # St Andrew's day
        self.assertIn(date(2016, 5, 26), holidays)  # Independence Day
        self.assertIn(date(2016, 8, 28), holidays)  # St Mary's Day
        self.assertIn(date(2016, 10, 14), holidays)  # Day of Svetitskovloba
        self.assertIn(date(2016, 11, 23), holidays)  # St George's day

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)

        self.assertIn(date(2020, 1, 1), holidays)  # New Year
        self.assertIn(date(2020, 1, 2), holidays)  # Second day of the New Year
        self.assertIn(date(2020, 1, 7), holidays)  # Orthodox Christmas
        self.assertIn(date(2020, 1, 19), holidays)  # Orthodox Epiphany
        self.assertIn(date(2020, 3, 3), holidays)  # Mother's Day
        self.assertIn(date(2020, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2020, 4, 9), holidays)  # Day of National Unity
        self.assertIn(date(2020, 4, 17), holidays)  # Orthodox Good Friday
        self.assertIn(date(2020, 4, 18), holidays)  # Great Saturday
        self.assertIn(date(2020, 4, 19), holidays)  # Orthodox Easter Day
        self.assertIn(date(2020, 4, 20), holidays)  # Orthodox Easter Monday
        self.assertIn(date(2020, 5, 9), holidays)  # Day of victory
        self.assertIn(date(2020, 5, 12), holidays)  # St Andrew's Day
        self.assertIn(date(2020, 5, 26), holidays)  # Independence Day
        self.assertIn(date(2020, 8, 28), holidays)  # St Mary's Day
        self.assertIn(date(2020, 10, 14), holidays)  # Day of Svetitskovloba
        self.assertIn(date(2020, 11, 23), holidays)  # St George's Day

    def test_no_labor_day(self):
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 5, 1), holidays)

    def test_no_christmas(self):
        holidays = self.cal.holidays_set(2016)
        self.assertNotIn(date(2016, 12, 24), holidays)
        self.assertNotIn(date(2016, 12, 25), holidays)

        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 12, 24), holidays)
        self.assertNotIn(date(2020, 12, 25), holidays)


class GreeceTest(GenericCalendarTest):
    cal_class = Greece

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 18), holidays)  # Clean monday
        # Annunciation & Independence day
        self.assertIn(date(2013, 3, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 5, 3), holidays)  # good friday
        self.assertIn(date(2013, 5, 5), holidays)  # easter
        self.assertIn(date(2013, 5, 6), holidays)  # easter monday
        self.assertIn(date(2013, 6, 23), holidays)  # pentecost sunday
        self.assertIn(date(2013, 6, 24), holidays)  # whit monday
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Glorifying mother of God

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # new year
        self.assertIn(date(2020, 1, 6), holidays)  # epiphany
        self.assertIn(date(2020, 3, 2), holidays)  # Clean monday
        # Annunciation & Independence day
        self.assertIn(date(2020, 3, 25), holidays)
        self.assertIn(date(2020, 4, 17), holidays)  # good friday
        self.assertIn(date(2020, 4, 19), holidays)  # easter
        self.assertIn(date(2020, 4, 20), holidays)  # easter monday
        self.assertIn(date(2020, 5, 1), holidays)  # labour day
        self.assertIn(date(2020, 6, 7), holidays)  # pentecost sunday
        self.assertIn(date(2020, 6, 8), holidays)  # whit monday
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption
        self.assertIn(date(2020, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2020, 12, 25), holidays)  # XMas
        self.assertIn(date(2020, 12, 26), holidays)  # Glorifying mother of God

    def test_no_orthodox_christmas(self):
        # This calendar is an Orthodox calendar, but there's no Jan XMas
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 1, 7), holidays)


class HungaryTest(GenericCalendarTest):
    cal_class = Hungary

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 15), holidays)  # national day
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 5, 19), holidays)  # Whit sunday
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 8, 20), holidays)  # St Stephen's day
        self.assertIn(date(2013, 10, 23), holidays)  # national day (again?)
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Second day of XMas

    def test_year_good_friday(self):
        # Since the year 2017, Good Friday is a non-working day un Hungary
        # Refs #203
        holidays = self.cal.holidays_set(2016)
        good_friday_2016 = date(2016, 3, 25)
        self.assertNotIn(good_friday_2016, holidays)
        # 2017
        holidays = self.cal.holidays_set(2017)
        good_friday_2017 = date(2017, 4, 14)
        self.assertIn(good_friday_2017, holidays)


class MaltaTest(GenericCalendarTest):
    """Rollover rules changed in 2005"""
    cal_class = Malta

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        # National Holidays
        self.assertIn(date(2017, 3, 31), holidays)  # Jum il-Ħelsien
        self.assertIn(date(2017, 6, 7), holidays)  # Sette Giugno
        self.assertIn(date(2017, 9, 8), holidays)  # Jum il-Vitorja
        self.assertIn(date(2017, 9, 21), holidays)  # Jum l-Indipendenza
        self.assertIn(date(2017, 12, 13), holidays)  # Jum ir-Repubblika
        # Public Holidays
        self.assertIn(date(2017, 1, 1), holidays)  # L-Ewwel tas-Sena
        self.assertIn(date(2017, 2, 10), holidays)  # Nawfraġju ta' San Pawl
        self.assertIn(date(2017, 3, 19), holidays)  # San Ġużepp
        self.assertIn(date(2017, 4, 14), holidays)  # Il-Ġimgħa l-Kbira
        self.assertIn(date(2017, 5, 1), holidays)  # Jum il-Ħaddiem
        self.assertIn(date(2017, 6, 29), holidays)  # L-Imnarja
        self.assertIn(date(2017, 8, 15), holidays)  # Santa Marija
        self.assertIn(date(2017, 12, 8), holidays)  # Il-Kunċizzjoni
        self.assertIn(date(2017, 12, 25), holidays)  # Il-Milied

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "Worker's Day")


class MonacoTest(GenericCalendarTest):
    cal_class = Monaco

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        # National Holidays
        self.assertIn(date(2020, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2020, 1, 27), holidays)  # Saint Dévote's Day
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        self.assertIn(date(2020, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2020, 5, 21), holidays)  # Ascension Day
        self.assertIn(date(2020, 6, 1), holidays)  # Whit Monday
        self.assertIn(date(2020, 6, 11), holidays)  # Corpus Christi
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption Day
        self.assertIn(date(2020, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2020, 11, 19), holidays)  # Sovereign Prince's Day
        self.assertIn(date(2020, 12, 8), holidays)  # Conception Day
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas Day

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        # National Holidays
        self.assertIn(date(2018, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2018, 1, 27), holidays)  # Saint Dévote's Day
        self.assertIn(date(2018, 4, 2), holidays)  # Easter Monday
        self.assertIn(date(2018, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2018, 5, 10), holidays)  # Ascension Day
        self.assertIn(date(2018, 5, 21), holidays)  # Whit Monday
        self.assertIn(date(2018, 5, 31), holidays)  # Corpus Christi
        self.assertIn(date(2018, 8, 15), holidays)  # Assumption Day
        self.assertIn(date(2018, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2018, 11, 19), holidays)  # Sovereign Prince's Day
        self.assertIn(date(2018, 12, 8), holidays)  # Conception Day
        self.assertIn(date(2018, 12, 25), holidays)  # Christmas Day


class NorwayTest(GenericCalendarTest):
    cal_class = Norway

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 3, 28), holidays)   # maundy thursday
        self.assertIn(date(2013, 3, 29), holidays)   # good friday
        self.assertIn(date(2013, 3, 31), holidays)   # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)   # easter monday
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 17), holidays)   # constitution day
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 12, 25), holidays)  # Xmas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens


class PolandTest(GenericCalendarTest):
    cal_class = Poland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New Year
        self.assertIn(date(2013, 1, 6), holidays)  # Trzech Kroli
        self.assertIn(date(2013, 3, 31), holidays)  # Easter Sunday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labor Day
        self.assertIn(date(2013, 5, 3), holidays)  # Constitution Day
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2013, 11, 11), holidays)  # Independence Day
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_shift_2016(self):
        # Poland does not roll christmas and boxing day
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas - Sunday
        self.assertIn(date(2016, 12, 26), holidays)  # Boxing day - Monday
        self.assertNotIn(date(2016, 12, 27), holidays)  # Christmas shift


class IcelandTest(GenericCalendarTest):
    cal_class = Iceland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 28), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 9), holidays)
        self.assertIn(date(2013, 5, 20), holidays)
        self.assertIn(date(2013, 6, 17), holidays)
        self.assertIn(date(2013, 8, 5), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)
        self.assertIn(date(2013, 12, 31), holidays)


class IrelandTest(GenericCalendarTest):
    cal_class = Ireland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)    # Tue New Year's Day
        self.assertIn(date(2013, 3, 17), holidays)   # Sun St Patricks day
        self.assertIn(date(2013, 3, 18), holidays)   # Mon St Patricks shift
        self.assertIn(date(2013, 4, 1), holidays)    # Mon Easter Monday
        self.assertIn(date(2013, 5, 6), holidays)    # Mon May day
        self.assertIn(date(2013, 6, 3), holidays)    # Mon June Holiday
        self.assertIn(date(2013, 8, 5), holidays)    # Mon August Holiday
        self.assertIn(date(2013, 10, 28), holidays)  # Mon October Holiday
        self.assertIn(date(2013, 12, 25), holidays)  # Wed Christmas
        self.assertIn(date(2013, 12, 26), holidays)  # Thu St Stepehen's

    def test_shift_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)    # new year day
        self.assertIn(date(2012, 1, 2), holidays)    # new year day shift

    def test_shift_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 12, 25), holidays)  # Christmas it's sunday
        self.assertIn(date(2011, 12, 26), holidays)  # Xmas day shift
        self.assertIn(date(2011, 12, 27), holidays)  # St Stephen's day shift

    def test_shift_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas it's friday
        self.assertIn(date(2015, 12, 26), holidays)  # St. Stephen's day Sat
        self.assertIn(date(2015, 12, 28), holidays)  # St. Stephen's day shift

    def test_whit_mon(self):
        holidays_1972 = self.cal.holidays_set(1972)
        holidays_1973 = self.cal.holidays_set(1973)
        # holidays_1974 = self.cal.holidays_set(1974) Overlaps with June Hol
        holidays_1975 = self.cal.holidays_set(1975)
        self.assertIn(date(1972, 5, 22), holidays_1972)     # Whit Monday
        self.assertIn(date(1973, 6, 11), holidays_1973)
        # self.assertNotIn(date(1974, 6, 3), holidays_1974) # Overlaps Jun Hol
        self.assertNotIn(date(1975, 5, 19), holidays_1975)  # No Whit Monday

    def test_may_day(self):
        holidays_1993 = self.cal.holidays_set(1993)
        holidays_1994 = self.cal.holidays_set(1994)
        holidays_1995 = self.cal.holidays_set(1995)
        self.assertNotIn(date(1993, 5, 1), holidays_1993)  # No May Day
        self.assertIn(date(1994, 5, 2), holidays_1994)     # May Day
        self.assertIn(date(1995, 5, 1), holidays_1995)

    def test_october_holiday(self):
        holidays_1976 = self.cal.holidays_set(1976)
        holidays_1977 = self.cal.holidays_set(1977)
        holidays_1978 = self.cal.holidays_set(1978)
        self.assertNotIn(date(1976, 10, 25), holidays_1976)  # No October Hol
        self.assertIn(date(1977, 10, 31), holidays_1977)     # October Hol
        self.assertIn(date(1978, 10, 30), holidays_1978)


class ItalyTest(GenericCalendarTest):
    cal_class = Italy

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new years day
        self.assertIn(date(2013, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 4, 25), holidays)  # liberation day
        self.assertIn(date(2013, 5, 1), holidays)  # workers day
        self.assertIn(date(2013, 6, 2), holidays)  # Republic day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 8), holidays)  # immaculate Conception
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        self.assertIn(date(2013, 12, 26), holidays)  # San Stefano

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "International Workers' Day")


class LatviaTest(GenericCalendarTest):

    cal_class = Latvia

    def test_year_2017(self):
        """
        https://www.bank.lv/en/about-us/public-holidays-in-latvia
        """
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2017, 4, 14), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 4, 16), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 4, 17), holidays)  # Easter 14 and 17 april
        self.assertIn(date(2017, 5, 1), holidays)  # Labour Day, C
        self.assertIn(date(2017, 5, 4), holidays)  # Restoration of Independe
        self.assertIn(date(2017, 6, 23), holidays)  # Midsummer Day
        self.assertIn(date(2017, 6, 24), holidays)  # St. John's Day
        self.assertIn(date(2017, 11, 18), holidays)  # Proclamation
        self.assertIn(date(2017, 11, 20), holidays)  # Proclamation Observed
        self.assertIn(date(2017, 12, 24), holidays)  # Christmas
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas
        self.assertIn(date(2017, 12, 26), holidays)  # Christmas
        self.assertIn(date(2017, 12, 31), holidays)  # New Year's Eve

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 5, 6), holidays)  # Restoration Day Observed


class LuxembourgTest(GenericCalendarTest):

    cal_class = Luxembourg

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # new year
        self.assertIn(date(2016, 3, 28), holidays)   # easter
        self.assertIn(date(2016, 5, 1), holidays)   # labour day
        self.assertIn(date(2016, 5, 5), holidays)   # Ascension
        self.assertIn(date(2016, 5, 16), holidays)  # Pentecote
        self.assertIn(date(2016, 6, 23), holidays)  # Luxembourg National Day
        self.assertIn(date(2016, 8, 15), holidays)  # Assomption
        self.assertIn(date(2016, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas
        self.assertIn(date(2016, 12, 26), holidays)  # St. Stephen´s Day

        self.assertNotIn(date(2016, 5, 9), holidays)  # Europe Day (>=2019)

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)

        self.assertIn(date(2019, 5, 9), holidays)   # Europe Day (>=2019)


class NetherlandsTest(GenericCalendarTest):

    cal_class = Netherlands

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)   # New Year
        self.assertIn(date(2015, 4, 3), holidays)   # Good friday
        self.assertIn(date(2015, 4, 5), holidays)   # Easter Sunday
        self.assertIn(date(2015, 4, 6), holidays)   # Easter Monday
        self.assertIn(date(2015, 4, 27), holidays)  # King's Day
        self.assertIn(date(2015, 5, 5), holidays)   # Liberation Day
        self.assertIn(date(2015, 5, 14), holidays)  # Ascension
        self.assertIn(date(2015, 5, 24), holidays)  # whit sunday
        self.assertIn(date(2015, 5, 25), holidays)  # whit monday
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas
        self.assertIn(date(2015, 12, 26), holidays)  # St. Stephen´s Day

    def test_king_day_2014(self):
        # As of 2014, King's Day replaces Queen's Day.
        # It's normally happening on April 27th, except when it's on SUN
        queen_day = date(2014, 4, 30)
        real_king_day = date(2014, 4, 27)
        king_day = date(2014, 4, 26)
        holidays = dict(self.cal.holidays(2014))
        self.assertNotIn(queen_day, holidays)
        self.assertNotIn(real_king_day, holidays)
        self.assertIn(king_day, holidays)
        self.assertEqual(holidays[king_day], "King's day")

    def test_king_day_2020(self):
        # Regular King's day
        king_day = date(2020, 4, 27)
        holidays = dict(self.cal.holidays(2020))
        self.assertIn(king_day, holidays)
        self.assertEqual(holidays[king_day], "King's day")

    def test_king_day_2025(self):
        # In 2025, it's shifted to the 26th, because it happens on SUN
        holidays = self.cal.holidays_set(2025)
        real_king_day = date(2025, 4, 27)
        king_day = date(2025, 4, 26)
        self.assertNotIn(real_king_day, holidays)
        self.assertIn(king_day, holidays)

    def test_queen_day(self):
        # In 1990 Queen's day was on 30 April. So it was until 2013.
        queen_day = date(1990, 4, 30)
        holidays = dict(self.cal.holidays(1990))
        self.assertIn(queen_day, holidays)
        # Check for label
        self.assertEqual(holidays[queen_day], "Queen's day")

        # Check in 2010
        queen_day = date(2010, 4, 30)
        holidays = dict(self.cal.holidays(2010))
        self.assertIn(queen_day, holidays)
        # Check for label
        self.assertEqual(holidays[queen_day], "Queen's day")

        # No more in 2014
        queen_day = date(2014, 4, 30)
        holidays = self.cal.holidays_set(2014)
        self.assertNotIn(queen_day, holidays)

    def test_queen_day_on_sunday(self):
        # On April 30th, 2006 Queen's day happened on SUN.
        queen_day = date(2006, 4, 29)
        holidays = dict(self.cal.holidays(2006))
        # The regular holiday
        self.assertNotIn(date(2006, 4, 30), holidays)
        # It's shifted to the previous day
        self.assertIn(queen_day, holidays)
        self.assertEqual(holidays[queen_day], "Queen's day")

    def test_new_years_eve(self):
        # For some reason, the new year's eve was added to the list of fixed
        # holidays. It appears it's not a holiday
        holidays = self.cal.holidays_set(2016)
        self.assertNotIn(date(2016, 12, 31), holidays)


class NetherlandsWithSchoolHolidaysWithInvalidRegionTest(TestCase):

    def test_instanciate_invalid_region(self):
        with self.assertRaises(ValueError) as cm:
            NetherlandsWithSchoolHolidays(region="east")
        assert "Set region" in str(cm.exception)

        with self.assertRaises(ValueError) as cm:
            NetherlandsWithSchoolHolidays(region="")
        assert "Set region" in str(cm.exception)

    def test_instanciate_no_region(self):
        with self.assertRaises(TypeError) as cm:
            NetherlandsWithSchoolHolidays()
        assert "missing 1 required positional argument" in str(cm.exception)


class NetherlandsWithSchoolHolidaysInvalidRanges(TestCase):

    def test_spring_holidays_invalid_range(self):
        max_year = max(SPRING_HOLIDAYS_EARLY_REGIONS)
        calendar = NetherlandsWithSchoolHolidays(region="north")
        with self.assertRaises(NotImplementedError):
            calendar.get_spring_holidays(max_year + 1)

    def test_summer_early_holidays_invalid_range(self):
        max_year = max(SUMMER_HOLIDAYS_EARLY_REGIONS)
        calendar = NetherlandsWithSchoolHolidays(region="north")
        with self.assertRaises(NotImplementedError):
            calendar.get_summer_holidays(max_year + 1)

    def test_summer_late_holidays_invalid_range(self):
        max_year = max(SUMMER_HOLIDAYS_LATE_REGIONS)
        calendar = NetherlandsWithSchoolHolidays(region="north")
        with self.assertRaises(NotImplementedError):
            calendar.get_summer_holidays(max_year + 1)


class NetherlandsNorthWithSchoolHolidaysTest(GenericCalendarTest):

    cal_class = NetherlandsWithSchoolHolidays
    kwargs = dict(region="north")

    def test_year_2010(self):
        with self.assertRaises(NotImplementedError):
            dict(self.cal.holidays(2010))

    def test_year_2020(self):
        year = 2020
        christmas_holiday_end = date(2020, 1, 5)
        spring_holiday_start = date(2020, 2, 15)
        may_holiday_start = date(2020, 4, 25)
        summer_holiday_start = date(2020, 7, 4)
        fall_holiday_start = date(2020, 10, 10)
        christmas_holiday_start = date(2020, 12, 19)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def test_year_2021(self):
        year = 2021
        christmas_holiday_end = date(2021, 1, 3)
        spring_holiday_start = date(2021, 2, 20)
        may_holiday_start = date(2021, 5, 1)
        summer_holiday_start = date(2021, 7, 10)
        fall_holiday_start = date(2021, 10, 16)
        christmas_holiday_start = date(2021, 12, 25)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def _test_school_holidays(
            self,
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
    ):
        holidays = {}
        for h in self.cal.holidays(year):
            holidays.setdefault(h[0], []).append(h[1])

        for d in range(christmas_holiday_end.day):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_end - timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Spring holiday",
                holidays[spring_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "May holiday",
                holidays[may_holiday_start + timedelta(days=d)],
            )
        for d in range(44):
            self.assertIn(
                "Summer holiday",
                holidays[summer_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Fall holiday",
                holidays[fall_holiday_start + timedelta(days=d)],
            )
        for d in range(31 - christmas_holiday_start.day + 1):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_start + timedelta(days=d)],
            )

    def test_may_holidays_exceptions(self):
        # In 2017, May holidays started on week 17 instead of 18

        # First, make sure we have a coherent date for 2021
        may_holidays_2021 = self.cal.get_may_holidays(2021)
        start_2021 = may_holidays_2021[0][0]
        self.assertEqual(
            start_2021,
            # Preceding SAT
            self.cal.get_iso_week_date(2021, 18 - 1, ISO_SAT)
        )

        # Then, get the start date for 2017
        may_holidays_2017 = self.cal.get_may_holidays(2017)
        start_2017 = may_holidays_2017[0][0]
        self.assertEqual(
            start_2017,
            # Preceding SAT
            self.cal.get_iso_week_date(2017, 17 - 1, ISO_SAT)
        )

    def test_fall_holidays_exceptions(self):
        # In 2024, May holidays start on week 44 instead of 43

        # First, make sure we have a coherent date for 2019
        # (using 2019 to avoid being in FALL_HOLIDAYS_EARLY_REGIONS)
        fall_holidays_2019 = self.cal.get_fall_holidays(2019)
        start_2019 = fall_holidays_2019[0][0]
        self.assertEqual(
            start_2019,
            # Preceding SAT
            self.cal.get_iso_week_date(2019, 43 - 1, ISO_SAT)
        )

        # Then, get the start date for 2024
        fall_holidays_2024 = self.cal.get_fall_holidays(2024)
        start_2024 = fall_holidays_2024[0][0]
        self.assertEqual(
            start_2024,
            # Preceding SAT
            self.cal.get_iso_week_date(2024, 44 - 1, ISO_SAT)
        )


class NetherlandsMiddleWithSchoolHolidaysTest(GenericCalendarTest):

    cal_class = NetherlandsWithSchoolHolidays
    kwargs = dict(region="middle")

    def test_year_2010(self):
        with self.assertRaises(NotImplementedError):
            dict(self.cal.holidays(2010))

    def test_year_2020(self):
        year = 2020
        christmas_holiday_end = date(2020, 1, 5)
        spring_holiday_start = date(2020, 2, 22)
        may_holiday_start = date(2020, 4, 25)
        summer_holiday_start = date(2020, 7, 18)
        fall_holiday_start = date(2020, 10, 17)
        christmas_holiday_start = date(2020, 12, 19)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def test_year_2021(self):
        year = 2021
        christmas_holiday_end = date(2021, 1, 3)
        spring_holiday_start = date(2021, 2, 20)
        may_holiday_start = date(2021, 5, 1)
        summer_holiday_start = date(2021, 7, 17)
        fall_holiday_start = date(2021, 10, 16)
        christmas_holiday_start = date(2021, 12, 25)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def _test_school_holidays(
            self,
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
    ):
        holidays = {}
        for h in self.cal.holidays(year):
            holidays.setdefault(h[0], []).append(h[1])

        for d in range(christmas_holiday_end.day):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_end - timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Spring holiday",
                holidays[spring_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "May holiday",
                holidays[may_holiday_start + timedelta(days=d)],
            )
        for d in range(44):
            self.assertIn(
                "Summer holiday",
                holidays[summer_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Fall holiday",
                holidays[fall_holiday_start + timedelta(days=d)],
            )
        for d in range(31 - christmas_holiday_start.day + 1):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_start + timedelta(days=d)],
            )


class NetherlandsSouthWithSchoolHolidaysTest(GenericCalendarTest):

    cal_class = NetherlandsWithSchoolHolidays
    kwargs = dict(region="south")

    def test_year_2010(self):
        with self.assertRaises(NotImplementedError):
            dict(self.cal.holidays(2010))

    def test_year_2020(self):
        year = 2020
        christmas_holiday_end = date(2020, 1, 5)
        spring_holiday_start = date(2020, 2, 22)
        may_holiday_start = date(2020, 4, 25)
        summer_holiday_start = date(2020, 7, 11)
        fall_holiday_start = date(2020, 10, 17)
        christmas_holiday_start = date(2020, 12, 19)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def test_year_2021(self):
        year = 2021
        christmas_holiday_end = date(2021, 1, 3)
        spring_holiday_start = date(2021, 2, 13)
        may_holiday_start = date(2021, 5, 1)
        summer_holiday_start = date(2021, 7, 24)
        fall_holiday_start = date(2021, 10, 23)
        christmas_holiday_start = date(2021, 12, 25)

        self._test_school_holidays(
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
        )

    def _test_school_holidays(
            self,
            year,
            christmas_holiday_start,
            spring_holiday_start,
            may_holiday_start,
            summer_holiday_start,
            fall_holiday_start,
            christmas_holiday_end,
    ):
        holidays = {}
        for h in self.cal.holidays(year):
            holidays.setdefault(h[0], []).append(h[1])

        for d in range(christmas_holiday_end.day):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_end - timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Spring holiday",
                holidays[spring_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "May holiday",
                holidays[may_holiday_start + timedelta(days=d)],
            )
        for d in range(44):
            self.assertIn(
                "Summer holiday",
                holidays[summer_holiday_start + timedelta(days=d)],
            )
        for d in range(9):
            self.assertIn(
                "Fall holiday",
                holidays[fall_holiday_start + timedelta(days=d)],
            )
        for d in range(31 - christmas_holiday_start.day + 1):
            self.assertIn(
                "Christmas holiday",
                holidays[christmas_holiday_start + timedelta(days=d)],
            )


class NetherlandsWithCarnivalTest(GenericCalendarTest):

    cal_class = Netherlands
    kwargs = dict(include_carnival=True)

    def test_year_2020(self):
        holidays = dict(self.cal.holidays(2020))
        self.assertEqual(
            holidays[date(2020, 2, 23)], "Carnival"
        )
        self.assertEqual(
            holidays[date(2020, 2, 24)], "Carnival"
        )
        self.assertEqual(
            holidays[date(2020, 2, 25)], "Carnival"
        )

    def test_year_2021(self):
        holidays = dict(self.cal.holidays(2021))
        self.assertEqual(
            holidays[date(2021, 2, 14)], "Carnival"
        )
        self.assertEqual(
            holidays[date(2021, 2, 15)], "Carnival"
        )
        self.assertEqual(
            holidays[date(2021, 2, 16)], "Carnival"
        )


class NetherlandsWithSchoolHolidaysAndCarnivalTest(GenericCalendarTest):
    cal_class = NetherlandsWithSchoolHolidays
    kwargs = dict(region="south", carnival_instead_of_spring=True)

    def test_year_2020(self):
        holidays = dict(self.cal.holidays(2020))
        for d in range(9):
            self.assertIn(
                "Carnival holiday",
                holidays[date(2020, 2, 22) + timedelta(days=d)],
            )

    def test_year_2021(self):
        holidays = dict(self.cal.holidays(2021))
        for d in range(9):
            self.assertIn(
                "Carnival holiday",
                holidays[date(2021, 2, 13) + timedelta(days=d)],
            )


class RomaniaTest(GenericCalendarTest):
    cal_class = Romania

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # Anul Nou New Year's Day
        self.assertIn(date(2017, 1, 2), holidays)  # Anul Nou Day after New Yr
        self.assertIn(date(2017, 1, 24), holidays)  # Unirea Principatelor Rom
        self.assertIn(date(2017, 4, 14), holidays)  # Orthodox Good Fri
        self.assertIn(date(2017, 4, 16), holidays)  # Orthodox Easter Sun
        self.assertIn(date(2017, 4, 17), holidays)  # Orthodox Easter Mon
        self.assertIn(date(2017, 5, 1), holidays)  # Ziua Muncii Labour Day
        self.assertIn(date(2017, 6, 1), holidays)  # Ziua Copilului Children's
        self.assertIn(date(2017, 6, 4), holidays)  # Pentecost
        self.assertIn(date(2017, 6, 5), holidays)  # Whit Monday
        self.assertIn(date(2017, 8, 15), holidays)  # Adormirea Maicii Domnului
        self.assertIn(date(2017, 11, 30), holidays)  # Sfântul Andrei St. Andre
        self.assertIn(date(2017, 12, 1), holidays)  # Ziua Națională/Marea Unir
        self.assertIn(date(2017, 12, 25), holidays)  # Crăciunul Christmas
        self.assertIn(date(2017, 12, 26), holidays)  # Crăciunul Christmas

    def test_year_2019(self):
        holidays = self.cal.holidays_set(2019)
        self.assertIn(date(2019, 1, 1), holidays)  # Anul Nou New Year's Day
        self.assertIn(date(2019, 1, 2), holidays)  # Anul Nou Day after New Yr
        self.assertIn(date(2019, 1, 24), holidays)  # Unirea Principatelor Rom
        self.assertIn(date(2019, 4, 26), holidays)  # Orthodox Good Fri
        self.assertIn(date(2019, 4, 28), holidays)  # Orthodox Easter Sun
        self.assertIn(date(2019, 4, 29), holidays)  # Orthodox Easter Mon
        self.assertIn(date(2019, 5, 1), holidays)  # Ziua Muncii Labour Day
        self.assertIn(date(2019, 6, 1), holidays)  # Ziua Copilului Children's
        self.assertIn(date(2019, 6, 16), holidays)  # Pentecost
        self.assertIn(date(2019, 6, 17), holidays)  # Whit Monday
        self.assertIn(date(2019, 8, 15), holidays)  # Adormirea Maicii Domnului
        self.assertIn(date(2019, 11, 30), holidays)  # Sfântul Andrei St. Andre
        self.assertIn(date(2019, 12, 1), holidays)  # Ziua Națională/Marea Unir
        self.assertIn(date(2019, 12, 25), holidays)  # Crăciunul Christmas
        self.assertIn(date(2019, 12, 26), holidays)  # Crăciunul Christmas

    def test_liberation_day(self):
        # Liberation day only happened between 1949 and 1990 (incl.)
        liberation_day_1989 = date(1989, 8, 23)
        holidays = self.cal.holidays_set(1989)
        self.assertIn(liberation_day_1989, holidays)

        liberation_day_1990 = date(1990, 8, 23)
        holidays = self.cal.holidays_set(1990)
        self.assertIn(liberation_day_1990, holidays)

        liberation_day_1991 = date(1991, 8, 23)
        holidays = self.cal.holidays_set(1991)
        self.assertNotIn(liberation_day_1991, holidays)

    def test_no_orthodox_christmas(self):
        # This calendar is an Orthodox calendar, but there's no Jan XMas
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 1, 7), holidays)


class RussiaTest(GenericCalendarTest):
    cal_class = Russia

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertIn(date(2018, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2018, 1, 2), holidays)  # Day after New Year
        self.assertIn(date(2018, 1, 7), holidays)  # Christmas
        self.assertIn(date(2018, 2, 23), holidays)  # Defendence of Fatherland
        self.assertIn(date(2018, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2018, 5, 1), holidays)  # Labour Day
        self.assertIn(date(2018, 5, 9), holidays)  # Victory Day
        self.assertIn(date(2018, 6, 12), holidays)  # National Day
        self.assertIn(date(2018, 11, 4), holidays)  # Independence Day

    def test_year_2020_shift(self):
        holidays = dict(self.cal.holidays(2020))
        # Defender of the Fatherland Day
        self.assertIn(date(2020, 2, 23), holidays)
        # SUN => Shift to MON
        self.assertIn(date(2020, 2, 24), holidays)
        self.assertEqual(
            holidays[date(2020, 2, 24)],
            "Defendence of the Fatherland shift"
        )
        # International Women's Day
        self.assertIn(date(2020, 3, 8), holidays)
        # SUN => Shift to MON
        self.assertIn(date(2020, 3, 9), holidays)
        self.assertEqual(
            holidays[date(2020, 3, 9)],
            "International Women's Day shift"
        )
        # Victory Day
        self.assertIn(date(2020, 5, 9), holidays)
        # SAT => Shift to MON
        self.assertIn(date(2020, 5, 11), holidays)
        self.assertEqual(
            holidays[date(2020, 5, 11)],
            "Victory Day shift"
        )

    def test_covid19_2020(self):
        # By decree, several days of March and April were defined
        # as non-working days because of the COVID-19 crisis.
        # It spans from March 28th to April 30th (included).
        holidays = self.cal.holidays_set(2020)
        start = date(2020, 3, 28)
        end = date(2020, 4, 30)
        for day in daterange(start, end):
            self.assertIn(day, holidays)
        # COVID-19 days in May
        self.assertIn(date(2020, 5, 6), holidays)  # Covid-19 May #1
        self.assertIn(date(2020, 5, 7), holidays)  # Covid-19 May #2
        self.assertIn(date(2020, 5, 8), holidays)  # Covid-19 May #3

        # Not for 2019, though
        holidays = self.cal.holidays_set(2019)
        start = date(2019, 3, 28)
        end = date(2019, 4, 30)
        for day in daterange(start, end):
            self.assertNotIn(day, holidays)

    def test_covid19_2020_label(self):
        # no "shift" for those days, all of them were non-working days
        holidays = self.cal.holidays(2020)
        start = date(2020, 3, 28)
        end = date(2020, 4, 30)
        for day, label in holidays:
            if start <= day <= end:
                self.assertNotIn("shift", label)

    def test_extra_days_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 5, 4), holidays)  # extra day, no other info
        self.assertIn(date(2020, 5, 5), holidays)  # Day of spring/labor day
        # Constitution Vote Public Holiday
        self.assertIn(date(2020, 7, 1), holidays)
        # Not in 2019
        holidays = self.cal.holidays_set(2019)
        self.assertNotIn(date(2019, 5, 4), holidays)
        self.assertNotIn(date(2019, 5, 5), holidays)
        self.assertNotIn(date(2019, 7, 1), holidays)

    def test_new_year_holidays_2004(self):
        # At that time, only Jan 1st/2nd were holidays.
        holidays = self.cal.holidays_set(2004)
        self.assertIn(date(2004, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2004, 1, 2), holidays)  # Day after New Year
        self.assertNotIn(date(2004, 1, 3), holidays)  # Shift of Jan 2nd
        self.assertNotIn(date(2004, 1, 4), holidays)  # Not until 2005
        self.assertNotIn(date(2004, 1, 5), holidays)  # Not until 2005
        self.assertNotIn(date(2004, 1, 6), holidays)  # Not until 2005
        self.assertIn(date(2004, 1, 7), holidays)  # XMas
        self.assertNotIn(date(2004, 1, 8), holidays)  # Not until 2005

    def test_new_year_holidays_2005(self):
        holidays = self.cal.holidays_set(2005)
        self.assertIn(date(2005, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2005, 1, 2), holidays)  # Day after New Year
        self.assertIn(date(2005, 1, 3), holidays)  # Holiday since 2005
        self.assertIn(date(2005, 1, 4), holidays)  # Holiday since 2005
        self.assertIn(date(2005, 1, 5), holidays)  # Holiday since 2005
        self.assertIn(date(2005, 1, 6), holidays)  # Holiday since 2005
        self.assertIn(date(2005, 1, 7), holidays)  # XMas
        self.assertIn(date(2005, 1, 8), holidays)  # Part of the holiday week

    def test_no_december_christmas(self):
        # This calendar is an Orthodox calendar & it doesn't include Dec 25th
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 12, 25), holidays)

    def test_holidays_2021(self):
        holidays = self.cal.holidays(2021)
        holidays_2021 = [
            (date(2021, 1, 1), "New year"),
            (date(2021, 1, 2), "Day After New Year"),  # SAT
            (date(2021, 1, 3), "Third Day after New Year"),  # SUN
            (date(2021, 1, 4), "Fourth Day after New Year"),
            (date(2021, 1, 5), "Fifth Day after New Year"),
            (date(2021, 1, 6), "Sixth Day after New Year"),
            (date(2021, 1, 7), "Christmas"),
            (date(2021, 1, 8),  "Eighth Day after New Year"),
            (date(2021, 2, 22), "Day Before Defendence of the Fatherland"),
            (date(2021, 2, 23), "Defendence of the Fatherland"),
            (date(2021, 3, 8), "International Women's Day"),
            (date(2021, 5, 1), "The Day of Spring and Labour"),
            (date(2021, 5, 3), "The Day of Spring and Labour shift"),
            (date(2021, 5, 9), "Victory Day"),
            (date(2021, 5, 10), "Victory Day shift"),
            (date(2021, 6, 12), "National Day"),
            (date(2021, 6, 14), "National Day shift"),
            (date(2021, 11, 4), "Day of Unity"),
            (date(2021, 11, 5), "Day After Day of Unity"),
            (date(2021, 12, 31), "New Year's Eve")
        ]
        self.assertEqual(holidays, holidays_2021)

    def test_year_2021_extra_working_day(self):
        self.assertTrue(self.cal.is_working_day(date(2021, 2, 20)))
        self.assertTrue(self.cal.is_working_day(datetime(2021, 2, 20)))

        self.assertTrue(self.cal.is_working_day(date(2021, 2, 19)))
        self.assertTrue(self.cal.is_working_day(datetime(2020, 2, 19)))

    def test_labour_day_label(self):
        # After 1992:
        self.cal.get_fixed_holidays(2021)
        self.assertEqual(
            self.cal.labour_day_label, "The Day of Spring and Labour")

        # Before 1992:
        self.cal.get_fixed_holidays(1991)
        self.assertEqual(
            self.cal.labour_day_label, "International Workers' Day")


class UkraineTest(GenericCalendarTest):
    cal_class = Ukraine

    def test_year_1991(self):
        holidays = self.cal.holidays_set(1991)
        self.assertIn(date(1991, 6, 16), holidays)  # Independence Day
        self.assertNotIn(date(1991, 8, 24), holidays)

    def test_year_1992(self):
        holidays = self.cal.holidays_set(1992)
        self.assertNotIn(date(1992, 6, 16), holidays)
        self.assertIn(date(1992, 8, 24), holidays)  # Independence Day

    def test_year_2010(self):
        holidays = self.cal.holidays_set(2010)
        self.assertIn(date(2010, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2010, 1, 7), holidays)  # Christmas (Orthodox)
        self.assertIn(date(2010, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2010, 5, 1), holidays)  # Workers Solidarity Day
        self.assertIn(date(2010, 5, 9), holidays)  # Victory Day
        self.assertIn(date(2010, 5, 24), holidays)  # Whit Monday
        self.assertIn(date(2010, 6, 28), holidays)  # Constitution Day
        self.assertIn(date(2010, 8, 24), holidays)  # Independence Day

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 29), holidays)  # Constitution Day (moved)
        self.assertIn(date(2015, 10, 14), holidays)  # Defender of Ukraine

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # New Year's Day
        self.assertIn(date(2016, 1, 7), holidays)  # Christmas (Orthodox)
        self.assertIn(date(2016, 3, 8), holidays)  # International Women's Day
        self.assertIn(date(2016, 5, 1), holidays)  # Workers Solidarity Day
        self.assertIn(date(2016, 5, 2), holidays)  # Workers Solidarity Day
        self.assertIn(date(2016, 5, 2), holidays)
        self.assertIn(date(2016, 5, 9), holidays)  # Victory Day
        self.assertIn(date(2016, 6, 20), holidays)
        self.assertIn(date(2016, 6, 28), holidays)  # Constitution Day
        self.assertIn(date(2016, 8, 24), holidays)  # Day of Unity
        self.assertIn(date(2016, 10, 14), holidays)  # Defender of Ukraine
        self.assertNotIn(date(2016, 12, 25), holidays)  # Christmas Day

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 2), holidays)  # New Year's Day (postponed)
        self.assertIn(date(2017, 1, 9), holidays)  # Christmas Orthodox (moved)
        self.assertIn(date(2017, 12, 25), holidays)  # Christmas Day

    def test_year_2018(self):
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 5, 2), holidays)  # Workers Solidarity Day

    def test_may_1st_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(holidays[date(2020, 5, 1)], "Workers Solidarity Day")


class UnitedKingdomTest(GenericCalendarTest):
    cal_class = UnitedKingdom

    def test_year_1973(self):
        holidays = self.cal.holidays_set(1973)
        self.assertIn(date(1973, 11, 14), holidays)  # royal wedding

    def test_year_1977(self):
        holidays = self.cal.holidays_set(1977)
        self.assertIn(date(1977, 6, 6), holidays)  # Early May Bank Holiday
        self.assertIn(date(1977, 6, 7), holidays)  # queen's silver jubilee

    def test_year_1981(self):
        holidays = self.cal.holidays_set(1981)
        self.assertIn(date(1981, 7, 29), holidays)  # royal wedding

    def test_year_1999(self):
        holidays = self.cal.holidays_set(1999)
        self.assertIn(date(1999, 12, 31), holidays)  # new year's eve

    def test_year_2002(self):
        holidays = self.cal.holidays_set(2002)
        self.assertIn(date(2002, 1, 1), holidays)  # new year day
        self.assertIn(date(2002, 3, 29), holidays)  # good friday
        self.assertIn(date(2002, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2002, 4, 1), holidays)  # easter monday
        self.assertIn(date(2002, 5, 6), holidays)  # Early May Bank Holiday
        self.assertIn(date(2002, 6, 3), holidays)  # queen's golden jubilee
        self.assertIn(date(2002, 6, 4), holidays)  # Spring Bank Holiday
        self.assertIn(date(2002, 8, 26), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2002, 12, 25), holidays)  # Christmas
        self.assertIn(date(2002, 12, 26), holidays)  # Boxing Day

    def test_year_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 4, 29), holidays)  # royal wedding

    def test_year_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)  # new year day
        self.assertIn(date(2012, 1, 2), holidays)  # new year shift
        self.assertIn(date(2012, 4, 6), holidays)  # good friday
        self.assertIn(date(2012, 4, 8), holidays)  # easter sunday
        self.assertIn(date(2012, 4, 9), holidays)  # easter monday
        self.assertIn(date(2012, 5, 7), holidays)  # Early May Bank Holiday
        self.assertIn(date(2012, 6, 4), holidays)  # Spring Bank Holiday
        self.assertIn(date(2012, 6, 5), holidays)  # queen's diamond jubilee
        self.assertIn(date(2012, 8, 27), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2012, 12, 25), holidays)  # Christmas
        self.assertIn(date(2012, 12, 26), holidays)  # Boxing Day

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year day
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 6), holidays)  # Early May Bank Holiday
        self.assertIn(date(2013, 5, 27), holidays)  # Spring Bank Holiday
        self.assertIn(date(2013, 8, 26), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_shift_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)  # new year day
        self.assertIn(date(2012, 1, 2), holidays)  # new year day shift

    def test_shift_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 12, 25), holidays)  # Christmas it's sunday
        self.assertIn(date(2011, 12, 26), holidays)  # XMas day shift
        self.assertIn(date(2011, 12, 27), holidays)  # Boxing day shift

    def test_shift_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas it's friday
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day it's saturday
        self.assertIn(date(2015, 12, 28), holidays)  # Boxing day shift

    def test_shift_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas - Sunday
        self.assertIn(date(2016, 12, 26), holidays)  # Boxing day - Monday
        self.assertIn(date(2016, 12, 27), holidays)  # Christmas - shift to Tue

    def test_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New Year
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 12), holidays)  # Easter Sunday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        # This is where the year 2020 becomes special:
        # The Early May Bank Holiday has been moved to May 8th
        # to commemorate the 75th anniversary of the end of WWII
        self.assertNotIn(date(2020, 5, 4), holidays)
        self.assertIn(date(2020, 5, 25), holidays)  # Spring Bank Holiday
        self.assertIn(date(2020, 8, 31), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2020, 12, 26), holidays)  # 'Boxing Day
        self.assertIn(date(2020, 12, 28), holidays)  # Boxing Day Shift

        # May the 8th is VE day
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertIn(date(2020, 5, 8), holidays)
        self.assertEqual(
            holidays[date(2020, 5, 8)], "Early May bank holiday (VE day)"
        )

    def test_2022(self):
        holidays = self.cal.holidays_set(2022)
        self.assertIn(date(2022, 1, 3), holidays)  # New Year
        self.assertIn(date(2022, 4, 15), holidays)  # Good Friday
        self.assertIn(date(2022, 4, 18), holidays)  # Easter Monday
        self.assertIn(date(2022, 5, 2), holidays)  # Early May Bank Holiday
        self.assertNotIn(date(2022, 5, 30), holidays)  # Spring Bank Holiday
        self.assertIn(date(2022, 6, 2), holidays)  # Spring Bank Holiday
        # Platinum Jubilee Bank Holiday
        self.assertIn(date(2022, 6, 3), holidays)
        self.assertIn(date(2022, 8, 29), holidays)  # Summer bank holiday
        # State Funeral of Queen Elizabeth II
        self.assertIn(date(2022, 9, 19), holidays)
        self.assertIn(date(2022, 12, 26), holidays)  # Boxing Day
        self.assertIn(date(2022, 12, 27), holidays)  # Christmas Day

    def test_2023(self):
        holidays = self.cal.holidays_set(2023)
        self.assertIn(date(2023, 1, 2), holidays)  # New Year
        self.assertIn(date(2023, 4, 7), holidays)  # Good Friday
        self.assertIn(date(2023, 4, 10), holidays)  # Easter Monday
        self.assertIn(date(2023, 5, 1), holidays)  # Early May Bank Holiday
        # Coronation of His Majesty King Charles III
        self.assertIn(date(2023, 5, 8), holidays)
        self.assertIn(date(2023, 5, 29), holidays)  # Spring Bank Holidays
        self.assertIn(date(2023, 8, 28), holidays)  # Summer bank holiday
        self.assertIn(date(2023, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2023, 12, 26), holidays)  # Boxing Day


class UnitedKingdomNorthernIrelandTest(UnitedKingdomTest):
    cal_class = UnitedKingdomNorthernIreland

    def test_regional_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 17), holidays)  # St Patrick's day
        self.assertIn(date(2013, 3, 18), holidays)  # St Patrick's sub
        self.assertIn(date(2013, 7, 12), holidays)  # Battle of the Boyne

    def test_regional_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 7, 12), holidays)  # Battle of the Boyne
        self.assertIn(date(2014, 7, 14), holidays)  # Battle of the Boyne sub


class GuernseyTest(GenericCalendarTest):
    cal_class = Guernsey

    def test_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # New Year
        self.assertIn(date(2020, 4, 10), holidays)  # Good Friday
        self.assertIn(date(2020, 4, 13), holidays)  # Easter Monday
        # This is where the year 2020 becomes special:
        # The Early May Bank Holiday has been moved to May 8th
        # to commemorate the 75th anniversary of the end of WWII
        self.assertNotIn(date(2020, 5, 4), holidays)
        self.assertIn(date(2020, 5, 25), holidays)  # Spring Bank Holiday
        self.assertIn(date(2020, 8, 31), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2020, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2020, 12, 26), holidays)  # 'Boxing Day
        self.assertIn(date(2020, 12, 28), holidays)  # Boxing Day Shift

        # May the 8th is VE day
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertIn(date(2020, 5, 8), holidays)
        self.assertEqual(
            holidays[date(2020, 5, 8)], "Early May bank holiday (VE day)"
        )

    def test_2021(self):
        holidays = self.cal.holidays_set(2021)
        self.assertIn(date(2021, 1, 1), holidays)  # New Year
        self.assertIn(date(2021, 4, 2), holidays)  # Good Friday
        self.assertIn(date(2021, 4, 5), holidays)  # Easter Monday
        self.assertIn(date(2021, 5, 3), holidays)  # May Day Bank Holiday
        self.assertIn(date(2021, 5, 9), holidays)  # Liberation Day
        self.assertIn(date(2021, 5, 31), holidays)  # Spring Bank Holiday
        self.assertIn(date(2021, 8, 30), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2021, 12, 27), holidays)  # Christmas Day
        self.assertIn(date(2021, 12, 28), holidays)  # Boxing Day Shift

    def test_2022(self):
        holidays = self.cal.holidays_set(2022)
        self.assertIn(date(2022, 1, 3), holidays)  # New Year
        self.assertIn(date(2022, 4, 15), holidays)  # Good Friday
        self.assertIn(date(2022, 4, 18), holidays)  # Easter Monday
        self.assertIn(date(2022, 5, 2), holidays)  # May Day bank Holiday
        self.assertIn(date(2022, 5, 9), holidays)  # Liberation Day
        self.assertIn(date(2022, 5, 30), holidays)  # Spring Bank Holiday
        self.assertIn(date(2022, 8, 29), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2022, 12, 26), holidays)  # 'Boxing Day
        self.assertIn(date(2022, 12, 27), holidays)  # Christmas Day


class EuropeanCentralBankTest(GenericCalendarTest):
    cal_class = EuropeanCentralBank

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # New year's day
        self.assertIn(date(2014, 4, 18), holidays)  # Good friday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # Labour day
        self.assertIn(date(2014, 12, 25), holidays)  # XMas
        self.assertIn(date(2014, 12, 26), holidays)  # St Stephen


class BelgiumTest(GenericCalendarTest):
    cal_class = Belgium

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 7, 21), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 11, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 21), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class PortugalTest(GenericCalendarTest):
    cal_class = Portugal

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2015, 4, 3), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2015, 4, 5), holidays)  # Domingo de Páscoa
        self.assertIn(date(2015, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2015, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2015, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2015, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2015, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2015, 12, 25), holidays)  # Natal

        self.assertNotIn(date(2015, 6, 4), holidays)  # Corpus Christi
        self.assertNotIn(date(2015, 10, 5), holidays)  # Todos os santos
        self.assertNotIn(date(2015, 11, 1), holidays)  # todos os santos
        # Restauração da Independência
        self.assertNotIn(date(2015, 12, 1), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2016, 3, 25), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2016, 3, 27), holidays)  # Domingo de Páscoa
        self.assertIn(date(2016, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2016, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2016, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2016, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2016, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2016, 12, 25), holidays)  # Natal

        self.assertIn(date(2016, 5, 26), holidays)  # Corpus Christi
        self.assertIn(date(2016, 10, 5), holidays)  # Implantação da República
        self.assertIn(date(2016, 11, 1), holidays)  # Todos os santos
        # Restauração da Independência
        self.assertIn(date(2016, 12, 1), holidays)

    def test_labour_day_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(
            holidays[date(2020, 5, 1)], "Dia do Trabalhador")

    def test_immaculate_conception_label(self):
        holidays = self.cal.holidays(2020)
        holidays = dict(holidays)
        self.assertEqual(holidays[date(2020, 12, 8)], "Imaculada Conceição")


class SerbiaTest(GenericCalendarTest):
    cal_class = Serbia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 2), holidays)
        self.assertIn(date(2015, 1, 7), holidays)
        self.assertIn(date(2015, 2, 15), holidays)
        self.assertIn(date(2015, 2, 16), holidays)
        self.assertIn(date(2015, 4, 10), holidays)
        self.assertIn(date(2015, 4, 12), holidays)
        self.assertIn(date(2015, 4, 13), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 2), holidays)
        self.assertIn(date(2015, 11, 11), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 1, 2), holidays)
        self.assertIn(date(2016, 1, 7), holidays)
        self.assertIn(date(2016, 2, 15), holidays)
        self.assertIn(date(2016, 2, 16), holidays)
        self.assertIn(date(2016, 4, 29), holidays)
        self.assertIn(date(2016, 5, 1), holidays)
        self.assertIn(date(2016, 5, 2), holidays)
        self.assertIn(date(2016, 11, 11), holidays)

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)
        self.assertIn(date(2017, 1, 2), holidays)
        self.assertIn(date(2017, 1, 7), holidays)
        self.assertIn(date(2017, 2, 15), holidays)
        self.assertIn(date(2017, 2, 16), holidays)
        self.assertIn(date(2017, 4, 14), holidays)
        self.assertIn(date(2017, 4, 16), holidays)
        self.assertIn(date(2017, 4, 17), holidays)
        self.assertIn(date(2017, 5, 1), holidays)
        self.assertIn(date(2017, 5, 2), holidays)
        self.assertIn(date(2017, 11, 11), holidays)

    def test_no_december_christmas(self):
        # This calendar is an Orthodox calendar & it doesn't include Dec 25th
        holidays = self.cal.holidays_set(2020)
        self.assertNotIn(date(2020, 12, 25), holidays)


class SloveniaTest(GenericCalendarTest):
    cal_class = Slovenia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 2, 8), holidays)
        self.assertIn(date(2015, 4, 5), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 4, 27), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 2), holidays)
        self.assertIn(date(2015, 5, 24), holidays)
        self.assertIn(date(2015, 6, 25), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)
        self.assertIn(date(2016, 2, 8), holidays)
        self.assertIn(date(2016, 3, 27), holidays)
        self.assertIn(date(2016, 3, 28), holidays)
        self.assertIn(date(2016, 4, 27), holidays)
        self.assertIn(date(2016, 5, 1), holidays)
        self.assertIn(date(2016, 5, 2), holidays)
        self.assertIn(date(2016, 5, 15), holidays)
        self.assertIn(date(2016, 6, 25), holidays)
        self.assertIn(date(2016, 8, 15), holidays)
        self.assertIn(date(2016, 10, 31), holidays)
        self.assertIn(date(2016, 11, 1), holidays)
        self.assertIn(date(2016, 12, 25), holidays)
        self.assertIn(date(2016, 12, 26), holidays)

    def test_january_second(self):
        # From 1955 until May 2012, when the National Assembly of Slovenia
        # passed the Public Finance Balance Act, 2 January was a work-free day.
        # It has been re-introduced in 2017.
        # Source - Wikipedia
        # https://en.wikipedia.org/wiki/Public_holidays_in_Slovenia

        # Before 1955...
        holidays = self.cal.holidays_set(1953)
        self.assertNotIn(date(1953, 1, 2), holidays)
        holidays = self.cal.holidays_set(1954)
        self.assertNotIn(date(1953, 1, 2), holidays)
        # Ranging from 1955 to 2012
        for year in range(1955, 2013):
            holidays = self.cal.holidays_set(year)
            self.assertIn(date(year, 1, 2), holidays)

        # As of 2012, it was no more
        for year in range(2013, 2017):
            holidays = self.cal.holidays_set(year)
            self.assertNotIn(date(year, 1, 2), holidays)

        # In 2017, january 2nd became a state holiday
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 2), holidays)


class EstoniaTest(GenericCalendarTest):
    cal_class = Estonia

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # new year
        self.assertIn(date(2015, 2, 24), holidays)  # independence day
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 5), holidays)  # easter sunday
        self.assertIn(date(2015, 5, 1), holidays)  # spring day
        self.assertIn(date(2015, 5, 24), holidays)  # pentecost
        self.assertIn(date(2015, 6, 23), holidays)  # victory day
        self.assertIn(date(2015, 6, 24), holidays)  # midsummer day
        self.assertIn(date(2015, 8, 20), holidays)  # restoration of independ.
        self.assertIn(date(2015, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2015, 12, 25), holidays)  # XMas
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # new year
        self.assertIn(date(2016, 2, 24), holidays)  # independence day
        self.assertIn(date(2016, 3, 25), holidays)  # good friday
        self.assertIn(date(2016, 3, 27), holidays)  # easter sunday
        self.assertIn(date(2016, 5, 1), holidays)  # spring day
        self.assertIn(date(2016, 5, 15), holidays)  # pentecost
        self.assertIn(date(2016, 6, 23), holidays)  # victory day
        self.assertIn(date(2016, 6, 24), holidays)  # midsummer day
        self.assertIn(date(2016, 8, 20), holidays)  # restoration of independ.
        self.assertIn(date(2016, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2016, 12, 25), holidays)  # XMas
        self.assertIn(date(2016, 12, 26), holidays)  # Boxing day


class LithuaniaTest(GenericCalendarTest):
    cal_class = Lithuania

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # new year
        self.assertIn(date(2016, 2, 16), holidays)  # restoration of the state
        self.assertIn(date(2016, 3, 11), holidays)  # restoration of independ.
        self.assertIn(date(2016, 3, 27), holidays)  # easter sunday
        self.assertIn(date(2016, 3, 28), holidays)  # easter monday
        self.assertIn(date(2016, 5, 1), holidays)  # labour day / mother's day
        self.assertIn(date(2016, 6, 5), holidays)  # father's day
        self.assertIn(date(2016, 6, 24), holidays)  # st john's day
        self.assertIn(date(2016, 7, 6), holidays)  # Anniversary of King Mind.
        self.assertIn(date(2016, 8, 15), holidays)  # Assumption day
        self.assertIn(date(2016, 11, 1), holidays)  # All saints day
        self.assertIn(date(2016, 12, 24), holidays)  # Xmas eve
        self.assertIn(date(2016, 12, 25), holidays)  # Xmas day
        self.assertIn(date(2016, 12, 26), holidays)  # 2nd day of xmas

    def test_year_2017(self):
        holidays = self.cal.holidays_set(2017)
        self.assertIn(date(2017, 1, 1), holidays)  # new year
        self.assertIn(date(2017, 2, 16), holidays)  # restoration of the state
        self.assertIn(date(2017, 3, 11), holidays)  # restoration of independ.
        self.assertIn(date(2017, 4, 16), holidays)  # easter sunday
        self.assertIn(date(2017, 4, 17), holidays)  # easter monday
        self.assertIn(date(2017, 5, 1), holidays)  # labour day
        self.assertIn(date(2017, 5, 7), holidays)  # mother's day
        self.assertIn(date(2017, 6, 4), holidays)  # father's day
        self.assertIn(date(2017, 6, 24), holidays)  # st john's day
        self.assertIn(date(2017, 7, 6), holidays)  # Anniversary of King Mind.
        self.assertIn(date(2017, 8, 15), holidays)  # Assumption day
        self.assertIn(date(2017, 11, 1), holidays)  # All saints day
        self.assertIn(date(2017, 12, 24), holidays)  # Xmas eve
        self.assertIn(date(2017, 12, 25), holidays)  # Xmas day
        self.assertIn(date(2017, 12, 26), holidays)  # 2nd day of xmas

    def test_year_2020(self):
        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 1, 1), holidays)  # new year
        self.assertIn(date(2020, 2, 16), holidays)  # restoration of the state
        self.assertIn(date(2020, 3, 11), holidays)  # restoration of independ.
        self.assertIn(date(2020, 4, 12), holidays)  # easter sunday
        self.assertIn(date(2020, 4, 13), holidays)  # easter monday
        self.assertIn(date(2020, 5, 1), holidays)  # labour day
        self.assertIn(date(2020, 5, 3), holidays)  # mother's day
        self.assertIn(date(2020, 6, 7), holidays)  # father's day
        self.assertIn(date(2020, 6, 24), holidays)  # st john's day
        self.assertIn(date(2020, 7, 6), holidays)  # Anniversary of King Mind.
        self.assertIn(date(2020, 8, 15), holidays)  # Assumption day
        self.assertIn(date(2020, 11, 1), holidays)  # All saints day
        self.assertIn(date(2020, 11, 2), holidays)  # All souls day
        self.assertIn(date(2020, 12, 24), holidays)  # Xmas eve
        self.assertIn(date(2020, 12, 25), holidays)  # Xmas day
        self.assertIn(date(2020, 12, 26), holidays)  # 2nd day of xmas

    def test_all_souls_day(self):
        # All Souls day was introduced as of 2020
        # https://en.wikipedia.org/wiki/Public_holidays_in_Lithuania
        holidays = self.cal.holidays_set(2018)
        self.assertNotIn(date(2018, 11, 2), holidays)
        holidays = self.cal.holidays_set(2019)
        self.assertNotIn(date(2019, 11, 2), holidays)

        holidays = self.cal.holidays_set(2020)
        self.assertIn(date(2020, 11, 2), holidays)
