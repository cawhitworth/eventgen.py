class Event(object):
    def __init__(self, name, start, end, location, description = ""):
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.description = description

class RecurringEvent(object):
    def __init__(self, event, recurrence):
        self.event = event
        self.recurrence = recurrence

    def as_csv(self):
        line = '"{0}","{1}","{2}","{3}","{4}","{5}","{6}"\n'
        output = '"Event title","Start time","Start date","End time","End date","Location","Description"\n'
        for date in self.recurrence.dates():
            output += line.format(self.event.name, self.event.start, date, self.event.end, date, self.event.location, self.event.description)
        return output
