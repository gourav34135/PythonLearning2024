import turtle

win=turtle.Screen()
turtle.speed(7)

for i in range(30):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

turtle.done()
