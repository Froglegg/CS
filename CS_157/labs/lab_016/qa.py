import datetime

print("Today's Date:", datetime.datetime.today())
date_today = datetime.date.today()
print(date_today)
print("Current Year:", date_today.year)
print("Current Month:", date_today.month)
print("Month Name:", date_today.strftime("%B"))
print("Month\'s Day :", date_today.day)
print("Weekday Name:", date_today.strftime("%A"))
