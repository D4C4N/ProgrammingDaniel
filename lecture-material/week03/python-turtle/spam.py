import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

length = 1
h = 0
n = 36

for i in range(350):
  c = colorsys.hsv_to_rgb(h,1,0.9) 
  h+=1/n 
  t.color(c)
  t.forward(length)
  t.right(90)
  t.forward(length)
  length+=1

turtle.done()