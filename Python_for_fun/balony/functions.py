import turtle
import math
import random
# https://minilogia.oeiizk.waw.pl/zadania/tresci/08_1.pdf
# balony
pointer = turtle.Turtle()
turtle.Screen().bgcolor("orange")
turtle.colormode(255)
turtle.speed(13)
def balon():
    color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pointer.forward(100)
    pointer.left(90)
    pointer.up()
    pointer.forward(10*math.sqrt(2))
    pointer.right(135)
    pointer.down()
    pointer.fillcolor(color)
    pointer.begin_fill()
    for bok in range(0,2):
        pointer.forward(20)
        pointer.right(90)
    pointer.right(45)
    pointer.forward(20*math.sqrt(2))
    pointer.right(135)
    pointer.end_fill()
    pointer.up()
    pointer.forward(20)
    pointer.left(45)
    pointer.forward(40)
    pointer.right(90)
    pointer.forward(40)
    pointer.down()
    pointer.left(90)
    pointer.begin_fill()
    pointer.circle(40)
    pointer.end_fill()
    pointer.left(90)
    pointer.up()
    pointer.forward(40)
    pointer.right(90)
    pointer.back(40+10*math.sqrt(2)+100)
    pointer.down()
def baloons(n):
    pointer.left(90)
    pointer.up()
    pointer.back(220)
    pointer.down()
    pointer.write("Numbers of ballons:"+str(n),font=("Verdana",15,"bold"))
    pointer.up()
    pointer.forward(220)
    pointer.down()
    for i in range(0,n):
        balon()
        pointer.right(360/n)
