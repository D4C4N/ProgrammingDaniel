print("Enter your salaray in Euros.")
salary = float(input())

if salary > 4000:
  tax = salary * 0.26
elif salary >= 2500:
  tax = salary * 0.22
else:
  tax = salary * 0.18

print(f"The tax is {tax} Euros.")