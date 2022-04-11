import turtle

turtle.bgcolor('pink')
turtle.title("Ramadan Mubarak")

def star(color):
    t = turtle.Turtle()
    t.color('yellow')
    t.fillcolor(color)
    t.begin_fill()
    t.up()
    t.goto(-280,250)
    t.down()
    for i in range(0,5):
        t.fd(150)
        t.right(144)
    t.end_fill()
    t.hideturtle()

def moonwithstar():
    turtle.up()
    turtle.goto(-200,30)
    turtle.color('orange')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()

    turtle.up()
    turtle.goto(-150,80)
    turtle.color('pink')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.hideturtle()
    star("yellow")
    


moonwithstar()

def R():
    t=turtle.Turtle()
    t.penup()
    t.goto(-350,-50) #position
    t.pendown()
    t.pensize(10)
    t.pencolor("red")
    t.right(90)
    t.forward(150)
    t.goto(-350,-50)
    t.right(-90)
    t.circle(-50,180,100)
    t.penup()
    t.goto(-350,-150)
    t.left(135)
    t.pendown()
    t.forward(70)
    t.hideturtle()
    amadan() 

def amadan():
    t=turtle.Turtle()
    t.penup()
    t.goto(-60,-220) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("navy")
    t.write("amadan", font=("Courier", 50, "normal"), align="right")
    t.hideturtle()

def M():
    t=turtle.Turtle()
    t.penup()
    #draw straight line
    t.goto(-10,-50) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("maroon")
    
    t.right(90)
    t.forward(150)
    
    t.goto(-10,-50)
    t.goto(40,-120)
    t.goto(85,-50)
    t.goto(85,-200)
    t.hideturtle()
    ubarak()

def ubarak():
    t=turtle.Turtle()
    t.penup()
    t.goto(330,-220) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("violet")
    t.write("ubarak", font=("Courier", 50, "normal"), align="right")
    t.hideturtle()


def Hijri():
    t=turtle.Turtle()
    t.penup()
    t.goto(100,-350) #centering in the screen
    t.pendown()
    t.pensize(10)
    t.pencolor("chocolate")
    t.write("1443 H", font=("turquoise", 50, "normal"), align="right")
    t.hideturtle()

R()
M()
Hijri()


turtle.done()