import turtle

screen = turtle.Screen()

turtle.speed("fastest")

turtle.up()
turtle.goto(0, -100)  # center circle around origin
turtle.down()

turtle.begin_fill()
turtle.fillcolor("yellow")  # draw head
turtle.circle(100)
turtle.end_fill()

turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.circle(80, 120)  # draw smile

turtle.fillcolor("black")

for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)  # draw eyes
    turtle.end_fill()

turtle.hideturtle()
turtle.done()

screen.exitonclick()