from datetime import time,date,timedelta
from functools import reduce
from utils import SymbolicConstant
import copy

Monday = SymbolicConstant()
Tuesday = SymbolicConstant()
Wednesday = SymbolicConstant()
Thursday = SymbolicConstant()
Friday = SymbolicConstant()
Saturday = SymbolicConstant()
Sunday = SymbolicConstant()

DOTW = [ Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ]

class Recurrence(object):
    def __init__(self):
        self.startDate = None
        self.endDate = None
        self.occurrencesCount = None
        self.filters = []

    def starting(self, startDate):
        newRecurrence = copy.copy(self)
        newRecurrence.startDate = startDate
        return newRecurrence

    def until(self, endDate):
        newRecurrence = copy.copy(self)
        newRecurrence.endDate = endDate
        return newRecurrence

    def filteredBy(self, filterObject):
        newRecurrence = copy.copy(self)
        newRecurrence.filters.append(filterObject)
        return newRecurrence

    def occurrences(self, count):
        newRecurrence = copy.copy(self)
        newRecurrence.occurrencesCount = count
        return newRecurrence

    def dates(self):
        date = self.startDate
        count = 0
        while True:
            ok = reduce(lambda x,y : x and y,
                    map(lambda x: x.filter(date), self.filters) )
            if ok:
                count += 1
                yield date
            date += timedelta(1)
            if self.endDate != None:
                if date > self.endDate:
                    break
            if self.occurrencesCount != None:
                if count == self.occurrencesCount:
                    break

class DayOfTheWeekFilter(object):
    def __init__(self, day):
        self.day = day

    def filter(self, date):
        return date.weekday() == DOTW.index(self.day)

class ExceptFilter(object):
    def __init__(self, dates):
        self.dates = dates

    def filter(self, date):
        return date not in self.dates

class RangeFilter(object):
    def __init__(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate

    def filter(self, date):
        return date < self.startDate or date > self.endDate

def every(what):
    if what in DOTW:
        return Recurrence().filteredBy(DayOfTheWeekFilter(what))


def endOfThisYear():
    return date(date.today().year, 12, 31)
