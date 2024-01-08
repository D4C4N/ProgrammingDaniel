a = 200
b = 33
c = 500
if a > b and a > c:
  print("At least one of the conditions is True")
  
if c < a and (a > b or b < c):
  print("At least one of the conditions is True")