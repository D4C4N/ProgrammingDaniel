import turtle
import time
import random

ws = turtle.Turtle()
ws.speed(0)
ws.color("red")

for i in range (1,100):
  for j in range (1,6):
    ws.left(100)
    ws.forward(100)
  ws.left(5)
turtle.done()