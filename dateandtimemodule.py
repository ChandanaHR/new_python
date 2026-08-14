import date,time,datetime
| Class       | Purpose                                    |
| ----------- | ------------------------------------------ |
| `date`      | Work only with dates                       |
| `time`      | Work only with time                        |
| `datetime`  | Work with date + time                      |
| `timedelta` | Represent a difference between dates/times |

a) date Class
The date class represents:
Year + Month + Day
It does not contain hours, minutes or seconds.
from datetime import date
d = date(2026, 8, 14)
print(d)

b) date.today()
Returns today's date.
from datetime import date
today = date.today()
print(today)

Get individual components
print(today.year)
print(today.month)
print(today.day)

c) date Properties
Suppose:
from datetime import date
d = date(2026, 8, 14)
You can access:
print(d.year)
print(d.month)
print(d.day)

d) date.weekday()
Returns the weekday as a number.
from datetime import date
d = date(2026, 8, 14)
print(d.weekday())
The numbering is:

Monday    → 0
Tuesday   → 1
Wednesday → 2
Thursday  → 3
Friday    → 4
Saturday  → 5
Sunday    → 6

e) date.isoweekday()
Similar to weekday(), but numbering starts from 1.
d = date(2026, 8, 14)
print(d.isoweekday())
Mapping:
Monday    → 1
Tuesday   → 2
Wednesday → 3
Thursday  → 4
Friday    → 5
Saturday  → 6
Sunday    → 7

f) date.isoformat()
Converts a date to ISO format:
YYYY-MM-DD
Example:
from datetime import date
d = date(2026, 8, 14)
print(d.isoformat())
Output:
2026-08-14

g) date.fromisoformat()
Converts an ISO-formatted string into a date.
from datetime import date
d = date.fromisoformat("2026-08-14")
print(d)
print(type(d))

h) time Class
The time class represents:
Hour + Minute + Second + Microsecond
It does not contain a date.
Example
from datetime import time
t = time(10, 30, 45)
print(t)

i) Access time Components
from datetime import time
t = time(10, 30, 45)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

j) Microseconds
You can specify microseconds:
from datetime import time
t = time(10, 30, 45, 500000)
print(t)

k) datetime Class
This is one of the most important classes.
It represents:
Date + Time
Example:
from datetime import datetime
dt = datetime(2026, 8, 14, 10, 30, 45)
print(dt)

l) datetime.now()
Returns the current local date and time.
from datetime import datetime
now = datetime.now()
print(now)

m) datetime.today()
Also returns the current local date and time.
from datetime import datetime
print(datetime.today())
For normal use, datetime.now() is generally more flexible because it can also accept a timezone.

n) Get Only the Date
From a datetime object:
from datetime import datetime
now = datetime.now()
d = now.date()
print(d)

o) Get Only the Time
from datetime import datetime
now = datetime.now()
t = now.time()
print(t)

p) datetime.combine()
Combines a date and time.
from datetime import date, time, datetime
d = date(2026, 8, 14)
t = time(10, 30, 45)
dt = datetime.combine(d, t)
print(dt)

q) datetime.strptime()
This is extremely important.
It converts:
String → datetime
Example:
from datetime import datetime
date_string = "14-08-2026"
dt = datetime.strptime(date_string, "%d-%m-%Y")
print(dt)

r) strftime()
This does the opposite:
datetime → string
Example:
from datetime import datetime
now = datetime.now()
result = now.strftime("%d-%m-%Y")
print(result)

Important strftime Formatting Codes
%Y	4-digit year	2026
%y	2-digit year	26
%m	Month	08
%B	Full month name	August
%b	Short month name	Aug
%d	Day	14
%A	Full weekday	Friday
%a	Short weekday	Fri
%H	Hour (24-hour)	14
%I	Hour (12-hour)	02
%M	Minute	30
%S	Second	45
%f	Microsecond	123456
%p	AM/PM	PM

from datetime import datetime
dt = datetime(2026, 8, 14, 14, 30, 45)
print(dt.strftime("%d/%m/%Y"))
print(dt.strftime("%A"))
print(dt.strftime("%B"))
print(dt.strftime("%I:%M:%S %p"))

s) timedelta
timedelta represents a difference or duration between dates/times.
from datetime import timedelta
td = timedelta(days=5)
print(td)
sa) Add Days to a Date
from datetime import date, timedelta
today = date.today()
future = today + timedelta(days=10)
print(today)
print(future)

sb) Add Weeks
from datetime import date, timedelta
today = date.today()
future = today + timedelta(weeks=2)
print(future)

Add Hours, Minutes and Seconds
from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(
    days=2,
    hours=3,
    minutes=20,
    seconds=30
)
print(future)

timedelta supports:
days
seconds
microseconds
milliseconds
minutes
hours
weeks

Practical: Find Age

A simple example:

from datetime import date
birth_date = date(2000, 5, 10)
today = date.today()
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
print(age)

t) replace()
replace() creates a new date/datetime with selected components changed.
from datetime import date
d = date(2026, 8, 14)
new_date = d.replace(year=2030)
print(d)
print(new_date)

u) datetime.replace()
from datetime import datetime
dt = datetime(2026, 8, 14, 10, 30)
new_dt = dt.replace(hour=18)
print(new_dt)
Output:
2026-08-14 18:30:00
You can change multiple components:
new_dt = dt.replace(
    year=2030,
    month=12,
    day=25,
    hour=20
)

