# Draw a Sierpinski Triangle
# Timothy Batchelder

from turtle import Screen, Turtle
import math
import random

screen = Screen()
t = Turtle()

t.shape("turtle")
t.speed(0)

t.color("black")
t.pensize(2)

t.hideturtle()

# Variable creation
base = 400
originPt1 = [0,0]
originPt2 = [base / 2,math.sqrt((base / 2) ** 2 + base ** 2)] # x = 1/2 length; y = sqrt(x*x+2x*2x)
originPt3 = [base,0] # length of base

newPoint = [25,50]

halfwayPoint = []

originList = [originPt1, originPt2, originPt3]

# Draw the first points
for p in originList:
  t.penup()
  t.goto(p[0], p[1])
  t.pendown()
  t.forward(1)
  t.goto(p[0], p[1])

t.penup()
t.goto(newPoint[0],newPoint[1])
t.pendown()
t.forward(1)

for i in range(25000):
  rand = random.randrange(0,3)
  randPoint = originList[rand]

  halfwayPoint = [(randPoint[0] + newPoint[0])/2, (randPoint[1] + newPoint[1])/2]

  t.penup()
  t.goto(halfwayPoint[0],halfwayPoint[1])
  t.pendown()
  t.forward(1)

  newPoint = halfwayPoint
  print(i, newPoint)


screen.exitonclick()
