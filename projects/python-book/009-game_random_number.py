import random
random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print(f"The exercise: {a} + {b}")

print("Please enter your guess.")
number = int(input())
print(f"Your input: {number}")
print(f"The solution: {c}")