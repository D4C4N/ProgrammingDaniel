# This is absolutely scuffed, will fix later. Surely ;)

def prime(number):
  for i in range(number +1):
    if (i == 0):
      pass
    elif (number % i == 0):
      return "False"
      break
    return "True"

print(prime(int(input())))  