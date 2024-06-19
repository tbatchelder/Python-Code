import turtle

screen = turtle.Screen()

f = 50
a1 = 120
a2 = 60
c = ['red', 'green', 'blue','purple']

def triangle(l, color):
  num = len(color)
  for i in range(num):
    turtle.forward(l)
    turtle.right(a1)
    turtle.forward(l)
    turtle.right(a1)
    turtle.forward(l)
    turtle.color(c[i])
    turtle.right(a2)
    turtle.forward(l)
    turtle.right(a1)
    turtle.forward(l)
    turtle.left(a2)
    turtle.color(c[i])

triangle(50,c)

#input("Hit Enter")
screen.exitonclick()