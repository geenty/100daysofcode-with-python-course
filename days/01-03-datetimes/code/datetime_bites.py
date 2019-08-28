from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    """
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    time_raw = line.split(" ")[1].replace("T"," ")
    line_datetime = datetime.strptime(time_raw, '%Y-%m-%d %H:%M:%S')
    return line_datetime


def time_between_shutdowns(loglines):
    """
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    times_to_consider = []
    for line in loglines:
        if "Shutdown initiated" in line:
            print(line)
            times_to_consider.append(convert_to_datetime(line))

    delta = max(times_to_consider) - min(times_to_consider)

    return delta
