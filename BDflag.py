import turtle
t = turtle.Turtle()

#Fuction for rectangle
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

#Fuction for circle 
def circle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(-30)
    t.end_fill()

t.up()
t.goto(0,-200)
t.down()
t.goto(0,200)
rectangle("green") #call rectangle 

t.color("black")
t.goto(0,180)
t.color("green")
t.forward(100)
circle("red") #call circle 