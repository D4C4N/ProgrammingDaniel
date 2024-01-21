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
elif number < 0 or number > 100:
  print(number, "is far from correct!")
elif c - 1 <= number <= c + 1:
  print(number, "is very close to correct!")
else:
  print(number, "is incorrect!")

print("Result:", c)