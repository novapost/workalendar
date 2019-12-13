from ..registry_tools import iso_register
from .core import UnitedStates


@iso_register('US-DC')
class DistrictOfColumbia(UnitedStates):
    "District of Columbia"
    include_inauguration_day = True
    FIXED_HOLIDAYS = UnitedStates.FIXED_HOLIDAYS + (
        (4, 16, "Emancipation Day"),
    )
