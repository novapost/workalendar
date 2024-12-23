refs #

<!-- if your contribution is a new calendar -->

For information, read and make sure you're okay with the [Contributing guidelines](https://workalendar.github.io/workalendar/contributing.html#adding-new-calendars).

- [ ] Tests with a significant number of years to be tested for your calendar.
- [ ] Docstrings for the Calendar class and specific methods.
- [ ] Use the ``workalendar.registry_tools.iso_register`` decorator to register your new calendar using ISO codes (optional).
- [ ] Calendar country / label added to the README.md file.
- [ ] Changelog amended with a mention like: "Added ``<country>`` by ``@pseudo`` (#)". **Note** *Please do NOT change the version number here. It's the project maintainers' duty.*

<!-- if your contribution is a fix -->

- [ ] Tests with a significant number of years to be tested for your calendar.
- [ ] Changelog amended with a mention describing your changes. **Note** *Please do NOT change the version number here. It's the project maintainers' duty.*

<!-- Release management

- Commit for the tag:
    - [ ] Edit version in setup.cfg
    - [ ] Add version in Changelog.md ; trim things
    - [ ] Push & wait for the tests to be green
    - [ ] tag me.
    - [ ] build sdist + wheel packages (``make package``)
- Back to dev commit:
    - [ ] Edit version in setup.cfg
    - [ ] Add the "master / nothing to see here" in Changelog.md
    - [ ] Push & wait for the tests to be green
- [ ] Merge --ff
- GitHub stuff
    - [ ] Push tag in Github
    - [ ] Edit release on GitHub using the changelog.
    - [ ] Delete branch
- [ ] upload release on PyPI using ``twine``
- [ ] (*optional*) Make feedback on the various PR or issues.

 -->
