import turtle

length = 100

t = turtle.Turtle()

for i in range (10):
  t.forward(length)
  t.right(90)
  t.forward(length)
  t.right(90)
  length += 10

turtle.done()