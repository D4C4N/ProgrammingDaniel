import random
random.seed()
x = random.randint(-3,3)
print("x:", x)

output = "positive" if x > 0 else "negative"
print(f"This number is {output}.")

print("This number is", "positive." if x > 0 else "negative.")

print("This number is", "positive." if x > 0 else "negative." if x < 0 else "0.")