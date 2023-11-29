import time

def timeConversion(s):
    time, period = s[:-2], s[-2:]
    hours, mins, secs = [int(each) for each in time.split(":", 2)]
    if period.upper() == "AM" and hours == 12:
        hours_in_24clock = 0 
    elif hours < 12 and period.upper() == "PM":
        hours_in_24clock = hours + 12
    else:
        hours_in_24clock = hours
    return f"{hours_in_24clock:0>2d}:{mins:0>2d}:{secs:0>2d}"

def test_timeConversion():
    times = ["12:10:01AM", "12:2:10PM", "3:0:20PM", "2:2:2AM"]
    time_format_12hour = "%I:%M:%S%p"
    time_format_24hour = "%H:%M:%S"
    for each in times:
        assert timeConversion(each) == time.strftime(time_format_24hour, time.strptime(each, time_format_12hour))