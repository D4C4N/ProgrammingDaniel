print("Enter the day:")
day = int(input())
print("Enter the month:")
month = int(input())
print("Enter the year:")
year = int(input())

if month == 2:
  print("Last day: 28")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
  print("Last day: 31")
else:
  print("Last day: 30")

if 31 >= day >= 1:
  if 12 >= month >= 1:
    print("Correct date.")
  else:
    print("Incorrect date.")  
else:
  print("Incorrect date.")