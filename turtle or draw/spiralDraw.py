# BENTUK SPIRAL 
def Cppsecrets (python , cplusplus):
    if python >0:
        turtle.forward(python)
        turtle.right(cplusplus)
        Cppsecrets(python-5,cplusplus)
import turtle
turtle.shape('turtle')
turtle.reset()
turtle.pen(speed =1)
turtle.delay(0)
length =400
turn_by =121
turtle.penup()
turtle.setpos(-length/2,length/2)
turtle.pendown()
Cppsecrets(length,turn_by)

# BENTUK CIRCLE RING
import turtle
turtle.bgcolor("black")
painter = turtle.Turtle()
painter.speed(0)
painter.penup()
painter.left(90)
painter.goto(0,0)
painter.forward(100)
painter.left(180)
painter.pendown()
j=0
for Cppsecrets in range(2):
    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #################################################################
    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    ###################################################################
    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    ###################################################################
    painter.pencolor("red")
    for i in range(150):
        painter.forward(100)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #################################################################
    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    ###################################################################
    painter.pencolor("dark violet")
    for i in range(150):
        painter.forward(104)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark red")
    for i in range(150):
        painter.forward(106)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark orange")
    for i in range(150):
        painter.forward(104)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark blue")
    for i in range(150):
        painter.forward(102)
        painter.right(111) 
    painter.penup()
    painter.right(180*j)
    painter.pendown()
    #####################################################################
    painter.pencolor("dark grey")
    for i in range(150):
        painter.forward(100)
        painter.left(111) 
    painter.penup()
    painter.right(90*j)
    painter.pendown()

# BENTUK PATERN 
import turtle
t = turtle.Turtle()
list1 = ["purple","red","orange","blue","green"]
turtle.bgcolor("black") 
for i in range(200):
  t.color(list1[i%5])
  t.pensize(i/10+1)
  t.forward(i)
  t.left(59)