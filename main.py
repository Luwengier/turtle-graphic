from turtle import Turtle, Screen
from random import randint
import colorgram


colors = colorgram.extract("hirst-spot.jpg", 20)
colorLen = len(colors)

timmy_the_turtle = Turtle()
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pu()
timmy_the_turtle.goto(-315, -315)

screen = Screen()
screen.colormode(255)


def pick_color():
    return colors[randint(2, colorLen - 1)].rgb


for _ in range(100):
    timmy_the_turtle.dot(20, pick_color())

    if _ == 99:
        continue
    elif (_ + 1) % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(70)
        if (_ + 1) % 20 == 0:
            timmy_the_turtle.setheading(0)
        else:
            timmy_the_turtle.setheading(180)
    else:
        timmy_the_turtle.forward(70)

screen.exitonclick()


# TODO: Draw a square

# for i in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# TODO: Draw a dashed line

# for _ in range(8):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# TODO: Draw different shapes

# for i in range(3, 11):
#     timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360 / i)

# TODO: Draw a random walk

# timmy_the_turtle.pensize(15)


# def random_walk():
#     timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     timmy_the_turtle.setheading(90 * randint(0, 3))
#     timmy_the_turtle.forward(30)


# for _ in range(72):
#     random_walk()

# TODO: Draw a spirograph


# def draw_spirograph(num: int):
#     for _ in range(num):
#         timmy_the_turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#         timmy_the_turtle.circle(50)
#         timmy_the_turtle.left(360 / num)


# draw_spirograph(18)
