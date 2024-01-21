print("Enter the day:")
day = int(input())
print("Enter the month:")
month = int(input())
print("Enter the year:")
year = int(input())

if (year % 4 == 0):
  if (year % 100 != 0):
    leapYear = True
  else:
    leapYear = False
elif (year % 400 == 0):
  leapYear = True
else:
  leapYear = False

if (12 >= month >= 1):
  if (month == 2):
    if (leapYear == True):
      if (29 >= day >= 1):
        print("Correct date.")
      else:
        print("Incorrect date.")
    else:
      if (28 >= day >= 1):
        print("Correct date.")
      else:
        print("Incorrect date.")
  elif (month == 4 or month == 6 or month == 9 or month == 11):
    if (30 >= day >= 1):
      print("Correct date.")
    else:
      print("Incorrect date.")
  else:
    if (31 >= day >= 1):
      print("Correct date.")
    else:
      print("Incorrect date.")
else:
  print("Incorrect date.")