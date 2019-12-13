import warnings

from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-MT')
class Montana(UnitedStates):
    """Montana"""
    include_election_day_even = True

    def get_variable_days(self, year):
        warnings.warn(
            "Montana states is supposed to observe General Election Day on "
            "even years, but for some reason some sources are including it "
            "in 2019. Please use with care."
        )
        return super(Montana, self).get_variable_days(year)
