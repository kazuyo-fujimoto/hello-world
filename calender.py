
"""カレンダーをコンソールに表示してみる."""
import calendar
my_calendar = calendar.TextCalendar()
my_calendar_string = my_calendar.formatmonth(2020, 2)
print(my_calendar_string)