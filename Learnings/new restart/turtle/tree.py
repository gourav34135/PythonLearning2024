import turtle

turtle.speed('fastest')

turtle.right(-90)

angle = 30

def y_tree(size, level):

    if level > 0:
        turtle.colormode(255)
        turtle.pencolor(0, 255//level, 0)
        turtle.forward(size)
        turtle.right(angle)
        y_tree(0.8 * size, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.left( 2 * angle )
        y_tree(0.8 * size, level-1)
        turtle.pencolor(0, 255//level, 0)
        turtle.right(angle)
        turtle.forward(-size)

y_tree(80, 7)

turtle.done()
