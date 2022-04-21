# BENTUK BINTANG
# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.speed(10)
# col=["yellow", "blue", "white", "green"]
# c=0

# for i in range(50):
#   t.forward(i*10)
#   t.right(144)
#   t.color(col[c])
#   if c==3:
#     c=0
#   else:
#     c+=1
# BENTUK BINTANG

# BENTUK BULAT MELINGKAR
# from turtle import *

# bgcolor("black")
# speed(11)
# hideturtle()
# for i in range(120):
#   color("cyan")
#   circle(i)
#   color("yellow")
#   circle(i*0.8)
#   right(3)
#   forward(3)
# done()
# BENTUK BULAT MELINGKAR

# BENTUK BOLA BINTANG
# import turtle
# import random
# turtle.bgcolor("black")
# turtle= turtle.Turtle()
# turtle.speed(0)
# colors= ('white', 'pink', 'magenta', 'red', 'orange', 'yellow', 'green', 'blue', 'purple')

# for i in range(360):
#   turtle.pencolor(colors[i%5])
#   turtle.width(i/100+1)
#   turtle.goto(0, 0)
#   turtle.pendown
#   turtle.forward(100)
#   turtle.right(59)
#   turtle.forward(200)
  
# turtle.done
# BENTUK BOLA BINTANG

# BENTUK HEART
import turtle
turtle.bgcolor("black")
t=turtle.Turtle()
turtle.speed(-5)
t.color("red")
t.begin_fill()
t.fillcolor("purple")
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.write("Love u",'false','center',font=('Showcard gothic',20))