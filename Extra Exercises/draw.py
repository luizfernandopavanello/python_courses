import turtle
import tkinter

pen = turtle.Turtle()

turtle.Screen().bgcolor('black')

turtle.colormode(255)

pen.pencolor("white")

# red = 50, 25, 217, 87
# green = 234, 32, 48, 5
# blue = 250, 168, 255, 230

red = 6
green = 4
blue = 212

pen.pencolor(red, green, blue)

# square
pen.up()
pen.goto(-100, 0)
pen.down()
pen.goto(0, 100)
pen.goto(100, 0)
pen.goto(0, -100)
pen.goto(-100, 0)

# outer shapes rectangles
pen.goto(-120, 20)
pen.goto(-140, 0)
pen.goto(0, -140)
pen.goto(140, 0)
pen.goto(120, 20)
pen.goto(100, 0)

# red = 50, 25, 217, 87
# green = 234, 32, 48, 5
# blue = 250, 168, 255, 230

inner_red = 76
inner_green = 4
inner_blue = 112

pen.pencolor(inner_red, inner_green, inner_blue)
# inner lines
pen.up()
pen.goto(0, -100)
pen.down()

pen.goto(0, 0)
pen.goto(50, 50)
pen.goto(0, -100)
pen.goto(-50, 50)

pen.hideturtle()

turtle.done()
