# Contribute to Workalendar

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [Class options](class-options.md) / [ISO Registry](iso-registry.md) / [iCal Export](ical.md)

## Use it (and test it)

If you are using `workalendar`, you are already contributing to it. As long as you are able to check its result, compare the designated working days and holidays to the reality, and make sure these are right, you're helping.

If any of the computed holidays for the country / area you are using is **wrong**, please report [it using the Github issues](https://github.com/workalendar/workalendar/issues).

## Report an issue

If you think you've found a bug you can report an issue. In order to help us sort this out, please follow the guidelines:

* Tell us which `workalendar` version (master, PyPI release) you are using.
* Tell us which Python version you are using, and your platform.
* Give us extensive details on the country / area Calendar, the exact date(s) that was (were) computed and the one(s) that should have been the correct result.
* If possible, please provide us a reliable source about the designated country / area calendar, where we could effectively check that we were wrong about a date, and giving us a way to patch our code properly so we can fix the bug.

## Adding new calendars

Since `workalendar` is mainly built around configuration variables and generic methods, it's not that difficult to add a calendar to our codebase. A few **mandatory** steps should be observed:

1.  Fork the repository and create a new branch named after the calendar you want to implement,
2.  Add a test class to the workalendar test suite that checks holidays,
3.  Implement the class using the core class APIs as much as possible. Test it until all tests pass.
4.  Make a nice pull-request we'll be glad to review and merge when it's perfect.

Please respect the PEP8 convention, otherwise your PR won't be accepted.

## Maintain Equinoxes and Solar terms

To reduce dependencies and computation time, equinoxes and solar terms are precomputed for the 30 previous and next years.
From time to time and before each release, please run the `create-astronomical-data` data file to update those files.

You also need to regenerate the `.json.gz` files if you plan to add a timezone to the astronomical data.

### Example

Let's assume you want to include the holidays of the magic (fictional) kingdom of *"Zhraa"*, which has a few holidays of different kind.

For the sake of the example, it has the following specs:

* it's a Gregorian-based Calendar (i.e. Western Europe / America),
* even if the King is not versed into religions, the kingdom includes a few Christian holidays,
* even if you never knew about it, it is set in Europe,

Here is a list of the holidays in *Zhraa*:

* January 1st, New year's Day,
* May 1st, Labour day,
* Easter Monday, which is variable (from March to May),
* The first monday in June, to celebrate the birth of the Founder of the Kingdom, Zhraa (nobody knows the exact day he was born, so this day was chosen as a convention),
* The birthday of the King, August 2nd.
* Christmas Day, Dec 25th.

#### Getting ready

You'll need to install `workalendar` dependencies beforehand. What's great is that you'll use virtualenv to set it up. Or even better: `virtualenvwrapper`. Just go in your working copy (cloned from GitHub) of workalendar and type, for example:

```sh
mkvirtualenv WORKALENDAR
pip install -e ./
```

#### Coding standards

When you provide a patch for workalendar, whether it would be a new calendar or a fix to an existing one, or else, you will have to make sure that your contribution follows these basic requirements:

* Your code should pass the `flake8` test ; that is to say that it follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines. You can check using the `tox -e flake8` command. If you can't, our CI jobs will do it, and you'll be able to know where are your mistakes, if any.
* Your code should be compatible with our supported Python version. Currently: Python 3.7, 3.8, 3.9, 3.10 and 3.11. Again, the CI (powered by Github Actions) will check your code against all those versions so you won't have to.
* If you encounter a failure in the `pyupgrade` tox job, you can fix it by running the followinf command: `tox -r pyupgrade`. It'll modify your code so it will pass this test. **Warning:** sometimes, this change can break the `flake8` standards, so you'll have to make sure that both linters will pass.

#### Test-driven start

Let's prepare the `Zhraa` class. Edit the `workalendar/europe/zhraa.py` file and add a class like this:

```python
from ..core import WesternCalendar
# NOTE: You may use absolute imports if your code lives outside of our codebase.

class Zhraa(WesternCalendar):
    "Kingdom of Zhraa"
```

The docstring is not mandatory, but if you omit it, the `name` property of your class will be the name of your class. For example, using upper CamelCase, `KingdomOfZhraa`. For a more human-readable label, use your docstring.

Meanwhile, in the `workalendar/europe/__init__.py` file, add these snippets where needed:

```python
from .zhraa import Zhraa
# ...
__all__ = (
    'Belgium',
    'CzechRepublic',
    # ...
    'Zhraa',
)
```

Now, we're building a test class. Edit the `workalendar/tests/test_europe.py` file and add the following code:

```python
from ..europe import Zhraa
# snip...

class ZhraaTest(GenericCalendarTest):
    cal_class = Zhraa

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # new year
        self.assertIn(date(2014, 5, 1), holidays)  # labour day
        self.assertIn(date(2014, 8, 2), holidays)  # king birthday
        self.assertIn(date(2014, 12, 25), holidays)  # Xmas
        # variable days
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 6, 2), holidays)  # First MON in June
```

of course, if you run the test using the `tox` or `py.test` command, this will fail, since we haven't implemented anything yet.

Install tox using the following command:

```sh
workon WORKALENDAR
pip install tox
```

With the `WesternCalendar` base class you have at least one holiday as a bonus: the New Year's day, which is almost a worldwide holiday.

#### Add fixed days

```python
class Zhraa(WesternCalendar):

    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 2, "King Birthday"),
    )
```

The `include_labour_day` is a flag common to all subclasses of `workalendar.core.Calendar`. Setting it to `True` activates the Labour Day for this calendar. Please note that there's a way to overwrite its label, using the `labour_day_label` class property.

Now we've got 3 holidays out of 6.


#### Add religious holidays

Since we're using `WesternCalendar` (it inherits from `ChristianMixin`) as a base to our `Zhraa` class, it automatically adds Christmas Day as a holiday. Now we can add Easter monday just by switching the correct flag.

```python
from ..core import WesternCalendar

class Zhraa(WesternCalendar):
    include_easter_monday = True
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 2, "King Birthday"),
    )
```
Almost there, 5 holidays out of 6.

#### Add variable "non-usual" holidays

There are many static methods that will grant you a clean access to variable days computation. It's very easy to add days like the "Birthday of the Founder":

```python
class Zhraa(WesternCalendar):
    include_easter_monday = True
    include_labour_day = True
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (8, 2, "King Birthday"),
    )

    def get_variable_days(self, year):
        # usual variable days
        days = super().get_variable_days(year)

        days.append(
            (Zhraa.get_nth_weekday_in_month(year, 6, MON),
            'Day of the Founder'),
        )
        return days
```

Please mind that the returned `days` is a list of tuples. The first item being a date object (in the Python `datetime.date` sense) and the second one is the label string.

#### Add you calendar to the global registry

If you're adding a Country calendar that has an ISO code, you may want to add it to our global registry.

Workalendar is providing a registry that you can use to query and fetch calendar based on their ISO code. For the current example, let's pretend that the Zhraa Kingdom ISO code is `ZK`.

To register, add the following:

```python
from ..registry_tools import iso_register

@iso_register('ZK')
class Zhraa(WesternCalendar):
    # The rest of your code...
```

#### You're done for the code!

There you are. Commit with a nice commit message, test, make sure it works for the other years as well - there might be exceptions to the common rules - and you're almost there.

#### The final steps

Do not forget to:

1. put the appropriate doctring in the Calendar class.
2. add your calendar in the `README.md` file, included in the appropriate continent.
3. add your calendar to the `Changelog.md` file.

**Note** *Please, do NOT change the version number in the changelog or in the ``setup.py`` file. It's the project maintainers' duty to decide when to release and how to increment the version number, according to the impact of the changes.*

We're planning to build a complete documentation for the other cases (special holiday rules, other calendar types, other religions, etc). But with this tutorial you're sorted for a lot of other calendars.

## Other code contributions

There are dozens of calendars all over the world. We'd appreciate you to contribute to the core of the library by adding some new Mixins or Calendars.

Bear in mind that the code you'd provide **must** be tested using unittests before you submit your pull-request.

[Home](index.md) / [Basic usage](basic.md) / [Advanced usage](advanced.md) / [Class options](class-options.md) / [ISO Registry](iso-registry.md) / [iCal Export](ical.md)
