import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.TextCalendar()

print("\nWelcome to the Calendar application!\n")

cal.prmonth(year, month)
print("\n\nHave a nice day!")
print('\n')