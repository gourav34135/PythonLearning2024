import turtle

# Create a Turtle object
t = turtle.Turtle()

# Move the turtle to starting position for 'T'
t.penup()
t.goto(-200, 0)
t.pendown()

# Draw the letter 'T'
t.lt(90)
t.fd(100)
t.bk(50)
t.rt(90)
t.fd(20)
t.bk(40)

# Move the turtle to starting position for 'A'
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the letter 'A'
t.lt(75)
t.fd(110)
t.bk(55)
t.rt(150)
t.fd(55)
t.bk(55)

# Move the turtle to starting position for 'N'
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw the letter 'N'
t.lt(90)
t.fd(100)
t.rt(135)
t.fd(140)
t.lt(135)
t.fd(100)

# Move the turtle to starting position for 'I'
t.penup()
t.goto(50, 0)
t.pendown()

# Draw the letter 'I'
t.lt(90)
t.fd(100)
t.bk(50)
t.rt(90)
t.fd(20)
t.bk(40)

# Move the turtle to starting position for 'Y'
t.penup()
t.goto(150, 0)
t.pendown()

# Draw the letter 'Y'
t.lt(60)
t.fd(70)
t.rt(120)
t.fd(70)
t.bk(35)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
