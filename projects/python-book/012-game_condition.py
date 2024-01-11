import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The exercise: {a} + {b}")

print("Please enter your guess:")
number = int(input())

if number == c:
  print(number, "is correct!")
else:
  print(number, "is incorrect!")
  print(f"Result: {c}")