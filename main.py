from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def rotate_clockwise():
    tim.left(10)

def rotate_counterclockwise():
    tim.right(10)

def clear_canvas():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_clockwise)
screen.onkey(key="d", fun=rotate_counterclockwise)
screen.onkey(key="c", fun=clear_canvas)
screen.exitonclick()
