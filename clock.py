import datetime

def now():
    date = datetime.datetime.now()
    return date.strftime("%Y-%m-%d")

def after(date1, date2):
    dateTime1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    dateTime2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return dateTime1 > dateTime2

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False