import turtle

conn=turtle.Turtle()

rad=20
repeat= int(input("Enter the number4 of concentric circles you wanna print: "))

for i in range(repeat):
    conn.circle(rad*i)
    conn.up()
    conn.sety((rad * i)*(-1))
    conn.down()

turtle.done()