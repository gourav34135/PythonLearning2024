import turtel
t=turtel.Turtel()
s=turtel.Screen()
s.bgcolor('black')
t.speed(10)
col=('yellow','blue','white','green')
c=0
#apran_khunger
for i in range(50):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=]
