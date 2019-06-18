import turtle

def heart_act():
    for i in range(196):
        turtle.right(1)
        turtle.forward(2)

def move_pen_position(x, y):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.showturtle()

turtle.setup(width=800, height=500)
turtle.color('red', 'pink')
turtle.pensize(3)
turtle.speed(1)
move_pen_position(0, -180)
turtle.left(140)
turtle.begin_fill()
turtle.forward(224)
heart_act()
turtle.left(120)
heart_act()
turtle.forward(224)
turtle.end_fill()

window = turtle.Screen()
window.exitonclick()

