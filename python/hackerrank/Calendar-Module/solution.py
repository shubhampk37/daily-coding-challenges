# HackerRank: Calendar Module
# Problem Link: https://www.hackerrank.com/challenges/calendar-module/problem

from collections import defaultdict

import calendar

# Read month, day and year from the input
month, day, year = map(int, input().split())

# find the weekday according to the input provided
day_index = calendar.weekday(year, month, day)

print(calendar.day_name[day_index].upper())
