from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_back():
    timmy.back(10)


def anti_clockwise():
    timmy.left(10)


def clockwise():
    timmy.right(10)


def clear():
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
