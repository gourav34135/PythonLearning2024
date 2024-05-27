import turtle

shape=turtle.Turtle()

sides=6
length=60
angle=360.0/sides
for j in range(4):

    for i in range(sides):
        shape.forward(length)
        shape.right(angle)


turtle.done()