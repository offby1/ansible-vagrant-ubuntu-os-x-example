import datetime
from datetime import timedelta

# I have objects with 2 dates:
# Start Date and End Date
# So i can have pairs like (datetime.date(2014, 1, 1), datetime.date(2014, 1, 31))
# This pairs are ranges.

# I could make a list with this pairs for my intention

example_a = [
    (datetime.date(2014, 1, 1), datetime.date(2014, 1, 31)),
    (datetime.date(2014, 2, 1), datetime.date(2014, 2, 28)),
    (datetime.date(2014, 3, 1), datetime.date(2014, 3, 31))
]

example_b = [
    (datetime.date(2014, 1, 1), datetime.date(2014, 1, 31)),
    (datetime.date(2014, 2, 10), datetime.date(2014, 2, 20)),
    (datetime.date(2014, 3, 10), datetime.date(2014, 3, 31))
]

# In the end i want to be sure there is not days left between
# (datetime.date(2014, 1, 1) and datetime.date(2014, 3, 31)

# If the list is example_a there wil not be left days but if list is example_b there will be left days.

# My first idea was make a new list with all days and other with this days and then search differences.

all = []
auxStart = example_a[0][0]
auxEnd = example_a[-1][1]

while auxStart <= auxEnd:
    all.append(auxStart)
    auxStart = auxStart + timedelta(days=1)

print("ALL:")
for x in all:
    print(x)

all_a = []
for x, y in example_a:
    aux = x
    while(aux <= y):
        all_a.append(aux)
        aux = aux + timedelta(days=1)

print("\nALL A:")
for x in all_a:
    print(x)

s = set(all_a)
result_a = [x for x in all if x not in s]

print("\nResult A:")
for x in result_a:
    print(x)
