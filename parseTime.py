import datetime
import time


def parseDate(dateString):
    dateString = dateString.split()

    day = int(dateString[0])
    month = int(dateString[1])
    year = int(dateString[2])

    try:
        date = datetime.datetime(year, month, day)
    except ValueError:
        # use a default date if failed
        date = datetime.datetime(1985, 1, 1)

    return date

def parseMinutes(minutes):
    seconds = int(minutes) * 60

    date = time.strftime('%H:%M', time.gmtime(seconds))

    return date
