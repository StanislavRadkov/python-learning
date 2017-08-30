import calendar

user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

print(calendar.day_name[c].upper())