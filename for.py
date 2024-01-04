# Looping through a list of items
bands = ["Sleep Token", "Periphery", "Monuments", "Thornhill"]
for x in bands:
  print(x)

# Looping through a String
for x in "Currents":
  print(x)

# Breaking a loop
for x in bands:
  if x == "Periphery":
    break
  print(x)

# Skipping items in a loop
for x in bands:
  if x == "Periphery":
    continue
  print(x)

# Loops using the range function
# The example below will print the values 0 to 5, as the functionality is index-based.
for x in range(6):
  print(x)