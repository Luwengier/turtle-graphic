from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkSeaGreen3")

# TODO: Draw a square

# for i in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

# TODO: Draw a dashed line

for _ in range(8):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


screen = Screen()
screen.exitonclick()
