from turtle import *  # type: ignore


def normal():
    pensize(5)
    screensize(500, 500, bg="black")
    begin_fill()
    circle(120, color("Yellow"))
    end_fill()
    lt(90)
    penup()
    fd(100)
    rt(90)
    fd(50)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    bk(100)
    pendown()
    begin_fill()
    circle(35, color("black"))
    end_fill()
    penup()
    fd(25)
    rt(90)
    fd(15)
    lt(90)
    pendown()
    fd(40)
    screensize(500, 500, bg="black")
    hideturtle()
    exitonclick()
