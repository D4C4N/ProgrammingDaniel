import random
random.seed()

x = random.randint(-5,5)
print("x:", x)

if x > 0:
  print("This number is positive.")
else:
  print("This number is 0 or negative.")