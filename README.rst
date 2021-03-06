===============================
Measure
===============================

Simple command line tool to collect a time series, one data point at a time.


Faster and more reliable than a spreadsheet - if you have a Terminal handy. I use it to record my weight, because I'm a huge nerd (and trying not to become a massive nerd). When it comes time to analyse the time series - plot it, calculate rolling averages, or whatever - just crack open IPython and `import measure`.


This is not a well-supported project! Also, the tests are blank and probably don't work. Accordingly, I haven't uploaded this to pypi or anywhere other than github!

This tool saves its database in `~/Documents/measurements.db` - if this doesn't suit you, you can change it by editing `DB_PATH` in `measure/measure.py`.

There are a few easy directions that this program could be extended, e.g. supporting the recording of more than one time series. I haven't done so because it didn't scratch my itch, and would make my use-case harder (if I had to specify at the CLI which specific time series the measurement should go into).


* Free software: GNU General Public License v3
* Documentation: https://measure.readthedocs.io.


Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

