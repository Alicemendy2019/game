import sys
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("game")

# p = sys.path
# print(p)
t = turtle.Turtle()
# t.circle(100)
t.shape("circle")
t.color("blue")
t.penup()
t.speed(0)
t.goto(0,100)
t.dy = -2

gravity = 0.1
while True:
    t.dy -= gravity
    t.sety(t.ycor() + t.dy)

    if t.ycor() < -300:
        t.dy *= -1

wn.mainloop()
