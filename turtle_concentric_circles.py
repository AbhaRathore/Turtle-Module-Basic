import turtle

turtle.showturtle()
turtle.color("red")
turtle.circle(25)
turtle.circle(50)
turtle.circle(75)
turtle.circle(100)

turtle.penup()
turtle.goto(150, -150)
turtle.pendown()
turtle.color("blue")
turtle.circle(25)
turtle.circle(50)
turtle.circle(75)
turtle.circle(100)

turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
turtle.color("green")
turtle.circle(25)
turtle.circle(50)
turtle.circle(75)
turtle.circle(100)

turtle.done()