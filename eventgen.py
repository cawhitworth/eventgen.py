from event import Event, RecurringEvent
from recurrence import *
from datetime import date, time

event = Event("My event", time(10,30), time(13,00), "Location")
event.description = "A longer description goes here"

recurrence = every(Thursday).starting(date.today()).until(endOfThisYear()).filteredBy(RangeFilter(date(2015,6,1), date(2015,6,30)))

print(RecurringEvent(event, recurrence).as_csv())
