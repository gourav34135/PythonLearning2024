import turtle

# Create a Turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(2)

# Draw a star
for _ in range(5):
    t.forward(100)  # Move forward by 100 units
    t.right(144)    # Turn right by 144 degrees
    
t.hideturtle()
turtle.done()
