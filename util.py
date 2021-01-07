from datetime import datetime


class DateTimeParser:
    @staticmethod
    def fromRFC3339(rfcString): #1970-01-01T00:00:00Z
        separated = rfcString.replace('Z','').split('T')
        date = separated[0].split('-')
        time = separated[1].split(':')

        return datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]), 0)
