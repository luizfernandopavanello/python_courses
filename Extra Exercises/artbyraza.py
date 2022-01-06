import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
def triangle():
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
t.speed(0)
t.pencolor('red')
t.penup()
t.goto(-350,250)
t.pendown()
for numbers in range(7):
    x = 250 - (86*numbers)
    t.penup()
    t.goto(-350,x)
    t.pendown()
    for number in range(7):
        triangle()
turtle.done()