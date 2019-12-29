# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from gettext import gettext as _

from ..core import FRI
from ..registry_tools import iso_register

from .core import UnitedStates


@iso_register('US-HI')
class Hawaii(UnitedStates):
    """Hawaii"""
    include_good_friday = True
    include_columbus_day = False
    include_election_day_even = True

    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (3, 26, _("Prince Jonah Kuhio Kalanianaole Day")),
        (6, 11, _("King Kamehameha Day")),
    )

    def get_statehood_day(self, year):
        """
        Statehood Day: 3rd Friday in August.
        """
        return (
            self.get_nth_weekday_in_month(year, 8, FRI, 3),
            _("Statehood Day")
        )

    def get_variable_days(self, year):
        days = super(Hawaii, self).get_variable_days(year)
        days.append(self.get_statehood_day(year))
        return days
