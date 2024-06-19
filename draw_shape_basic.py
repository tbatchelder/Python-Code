# Draw basic shapes
# Timothy Batchelder

import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.speed(0)

t.color("blue")
t.pensize(3)

#def Square(len):
#    for i in range(4):
#        t.forward(len)
#        t.left(90)

def Rectangle(len, width = 0):
    if width == 0:
        width = len
    for i in range(2):
        t.forward(len)
        t.left(90)
        t.forward(width)
        t.left(90)

def Triangle(len1, len2, len3):
    # Ok, seems we need to do some prep work first
    sum1and2 = len1 + len2
    sum2and3 = len2 + len3
    sum1and3 = len1 + len3

    # Check to make sure the sume of two sides is greater than the third
    if len1 > sum2and3 or len2 > sum1and3 or len3 > sum1and2:
        print("The sum of two sides is greater than the third.")
        return False
    
    angleA = 180 - math.degrees( math.acos( (len2**2 + len3**2 - len1**2) / (2 * len2 * len3) ) )
    angleB = 180 - math.degrees( math.acos( (len1**2 + len3**2 - len2**2) / (2 * len1 * len3) ) )
    angleC = 180 - math.degrees( math.acos( (len1**2 + len2**2 - len3**2) / (2 * len1 * len2) ) )

    if (angleA + angleB + angleC) > 180:
        print("Angles are more than 180 degrees.")
        return False

    t.forward(len1)
    t.left(angleC)
    t.forward(len2)
    t.left(angleA)
    t.forward(len3)
    t.left(angleB)

def House(len):
    Rectangle(len)
    t.penup()
    t.goto(0, len)
    t.pendown()
    Triangle(len, len, len)

def Polygon(len, sides):
    angle = 360 / sides
    for i in range(sides):
        t.forward(len)
        t.right(angle)

def Stopsign(len):
    # Find the medium diagonal
    m = len * ( 1 + math.sqrt(2) )

    # Find the length and width of the pole
    poleWidth = round(len / 4, 0)
    poleLength = round(len * 2, 0)

    Polygon(len, 8)
    
    t.penup()
    # Find where to place the pole
    poleHorizontalPosition = len / 2 - poleWidth / 2
    poleVerticalPosition = -1 * m - poleLength
    t.goto(poleHorizontalPosition, poleVerticalPosition)
    t.pendown()

    Rectangle(poleWidth, poleLength)
    

# Square(20)
# Rectangle(50,100)
# Triangle(50, 100, 100)
# House(50)
Stopsign (30)

screen.exitonclick()