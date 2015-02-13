eventgen.py
-----------

This is some simple Python code for generating and printing recurring events.
It's primarily designed for use with
[The Events Calendar](https://wordpress.org/plugins/the-events-calendar/)
WordPress plugin, the free version of which doesn't support recurring events
but does support CSV import.

It supports a moderately literate syntax for describing recurrences:

    recurrence = every(Saturday).from(date.today()).until(endOfThisYear())

The ```eventgen.py``` file shows an example usage.
