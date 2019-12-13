from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-AZ')
class Arizona(UnitedStates):
    """Arizona"""
    martin_luther_king_label = "Dr. Martin Luther King Jr./Civil Rights Day"
    presidents_day_label = "Lincoln/Washington Presidents' Day"
