

import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
marker = turtle.Pen()

turtle.bgcolor('black')

for x in range(90):
    marker.pencolor(colors[x%6])
    marker.width(x//100 + 1)
    marker.forward(x)
    marker.left(59)

turtle.done()


