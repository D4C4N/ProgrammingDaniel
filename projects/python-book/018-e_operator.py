print("Enter your salaray in Euros.")
salary = float(input())
print("Are you married (Y/N)?")
married = input()

if salary > 4000:
  if married == "N":
    tax = salary * 0.26
  if married == "Y":
    tax = salary * 0.22
else:
  if married == "N":
    tax = salary * 0.22
  if married == "Y":
    tax = salary * 0.18

print(f"The tax is {tax} Euros.")