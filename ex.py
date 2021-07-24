import turtle

d=turtle.Turtle()


turtle.bgcolor("white")
d.pensize(5)
d.pencolor("black")
col = "white"
col1 = "blue"
col2 = "orange"


d.fillcolor(col1)
d.begin_fill()
d.circle(150,360)
d.end_fill()

# mouth part
d.fillcolor(col)
d.begin_fill()
d.circle(110,360)
d.end_fill()

# left chin to eye
d.circle(110,150)

# eyes
d.fillcolor(col)
d.begin_fill()
d.right(90)
d.circle(25,360)
d.circle(25,190)

d.right(130)
d.circle(25,360)
d.circle(25,155)
d.end_fill()

#right chin to center
d.right(75)
d.circle(110,170)

# left chin to mustoch
d.circle(110,50)

#left mustuch
d.right(90)
d.forward(90)
d.backward(130)
d.forward(40)

d.left(90)
d.circle(40,30)
d.right(110)
d.forward(90)
d.backward(130)
d.forward(40)

d.left(80)
d.circle(40,30)
d.right(110)
d.forward(90)
d.backward(130)
d.forward(40)

#left to right mustuch
d.right(75)
d.circle(-108,150)
d.left(90)
d.forward(90)
d.backward(130)
d.forward(40)

d.right(119)
d.circle(62,30)
d.left(80)
d.forward(90)
d.backward(130)
d.forward(40)

d.right(100)
d.circle(58,30)
d.left(50)
d.forward(90)
d.backward(130)
d.forward(40)

#back to center
d.left(98)
d.circle(135,80)

#MOUTH

d.left(98)
d.forward(60)
d.left(90)
d.circle(-130,20)
d.right(180)
d.circle(130,40)
d.left(180)
d.circle(-130,20)
d.left(90)
d.forward(60)
d.right(90)
d.fillcolor(col2)
d.begin_fill()
d.circle(30,360)
d.end_fill()

d.circle(30,360,130)

