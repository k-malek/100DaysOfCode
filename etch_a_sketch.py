'''Graphics module'''
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=lambda:turtle.forward(10))
screen.onkey(key="s", fun=lambda:turtle.backward(10))
screen.onkey(key="a", fun=lambda:turtle.left(30))
screen.onkey(key="d", fun=lambda:turtle.right(30))
screen.onkey(key="r", fun=turtle.home)
screen.exitonclick()
