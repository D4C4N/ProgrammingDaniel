x = 12
y = 15
z = 20
print(f"x:{x}, y:{y}, z:{z}")

if x < y and x < z:
  print("x is the smallest number.")

if y>x or y>z:
  print("y is not the smallest number.")
if not y<x:
  print("y is not smaller than x.")