# Some exercises to evaluate our understanding of for-loops and the Python syntax.
i=0
while i<5:
  print(i,end=" ")
  i += 1
else:
  print("done")

for i in range(1,10,2):
  if i%3 == 0:
      continue
  print(i,end=" ")
else:
  print("done")

for i in range(1,10):
  if i%2 == 0:
    continue
  print(i,end=" ")
else:
  print("done")

i=0
while i<5:
  print(i,end=" ")
  if i == 3:
    break
  i += 1
else:
  print("done")