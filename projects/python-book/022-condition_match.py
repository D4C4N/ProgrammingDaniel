import random
random.seed()

x = "Paris"
match x:
  case "Paris":
    print("France")
  case "Rome":
    print("Italy")
  case "Madrid":
    print("Spain")
  case _:
    print("Unknown country")
print()

x = random.randint(1,6)
print("x =", x)
match x:
  case 1 | 3 | 5:
    print("odd")
  case 2 | 4 | 6:
    print("even")
  case _:
    print("No valid dice value.")
print()

x = random.randint(1,10)
print("x * 1.5 =", x * 1.5)
match x * 1.5:
  case x if x < 5:
    print("small value")
  case x if x > 11:
    print("big value")
  case _:
    print("average value")