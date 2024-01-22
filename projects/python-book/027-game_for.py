import random
random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print(f"The exercise: {a} + {b}")

for i in 1, 2, 3, 4:
  print("Please enter your guess:")
  number = int(input())
  if number == c:
    print(number, "is correct!")
    break
  else:
    print(number, "is incorrect!")