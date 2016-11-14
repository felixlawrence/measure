=====
Usage
=====

To record a measurement, use the command-line program::

    $ measure 3.14

To access past measurements as a `pandas.Series` ::

    import measure
    data = measure.get_data()
