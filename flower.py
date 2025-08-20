import turtle
import math

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("One Flower from a Bouquet")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)
flower.pensize(2)

# Draw a petal
def draw_petal():
    flower.color("red")
    flower.begin_fill()
    flower.circle(60, 60)
    flower.left(120)
    flower.circle(60, 60)
    flower.left(120)
    flower.end_fill()

# Draw the flower
def draw_flower():
    for _ in range(6):  # 6 petals
        draw_petal()
        flower.right(60)

# Draw the center
def draw_center():
    flower.penup()
    flower.goto(0, -10)
    flower.pendown()
    flower.color("yellow")
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

# Draw the stem
def draw_stem():
    flower.penup()
    flower.goto(0, -30)
    flower.setheading(-90)
    flower.pendown()
    flower.color("green")
    flower.pensize(5)
    flower.forward(100)

# Move to starting position
flower.penup()
flower.goto(0, 0)
flower.setheading(0)
flower.pendown()

draw_flower()
draw_center()
draw_stem()

flower.hideturtle()
screen.mainloop()
