class Event(object):
    def __init__(self, name, start, end, location, description = "", category = ""):
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.description = description
        self.category = category

class RecurringEvent(object):
    def __init__(self, event, recurrence):
        self.event = event
        self.recurrence = recurrence

    def as_csv(self):
        line = '"{0}","{1}","{2}","{3}","{4}","{5}","{6}",true,true,"{7}"\n'
        output = '"Event title","Start time","Start date","End time","End date","Location","Category","Maps","Map link","Description"\n'
        count = 1
        for date in self.recurrence.dates():
            name = self.event.name.format(count)

            output += line.format(name, self.event.start, date, self.event.end, date, self.event.location, self.event.category, self.event.description)
            count += 1

        return output
