import datetime

def now():
    date = datetime.datetime.now()
    return date.strftime("%Y-%m-%d")