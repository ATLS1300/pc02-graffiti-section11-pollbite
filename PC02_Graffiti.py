#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lily Battin
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("PaleVioletRed2")
panel.bgpic(image)

#=======Add your code here======

#jeff bezos bangs
turtle.up()
turtle.color("cyan4")
turtle.fillcolor("cyan3")
turtle.begin_fill() 
centerForehead = (5,185)
turtle.goto(centerForehead)
turtle.down()
turtle.goto(-20,125)
turtle.goto(-30,140)
turtle.goto(-50,90)
turtle.goto(-50,60)
turtle.goto(-100,120)
turtle.goto(-100,170)
turtle.left(65)
turtle.forward(70)
turtle.setheading(0)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(80,84)
turtle.goto(33,150)
turtle.goto(14,94)
turtle.goto(centerForehead)
turtle.end_fill()

#jeff bezos twintail right
turtle.up()
leftForehead = (53,210)
turtle.color("cyan4")
turtle.fillcolor("cyan4")
turtle.begin_fill()
turtle.goto(leftForehead)
turtle.down()
turtle.left(80)
turtle.forward(130)
turtle.right(130)
turtle.forward(340)
turtle.goto(35,0)
turtle.goto(45,10)
turtle.goto(45,20)
turtle.goto(60,50)
turtle.right(180)
turtle.forward(60)
turtle.goto(80,84)
turtle.goto(100,165)
turtle.goto(leftForehead)
turtle.end_fill()

#jeff bezos twintail left
turtle.up()
rightForehead = ( -83,210)
turtle.color("cyan4")
turtle.fillcolor("cyan4")
turtle.goto(rightForehead)
turtle.down()
turtle.begin_fill()
turtle.left(45)
turtle.forward(130)
turtle.left(135)
turtle.forward(340)
turtle.left(118)
turtle.forward(130)
turtle.left(60)
turtle.forward(30)
turtle.left(40)
turtle.forward(60)
turtle.setheading(90)
turtle.goto(-100,120)
turtle.goto(-100,170)
turtle.goto(rightForehead)
turtle.end_fill()

#jeff bezos magical circles
particleOrigin = (151,-90)
turtle.color("DarkOrchid4")
turtle.fillcolor("DarkOrchid3")
turtle.pensize(3)
turtle.up()
turtle.goto(particleOrigin)
turtle.down()
turtle.begin_fill()
turtle.setheading(270)
turtle.circle(20)
turtle.end_fill()
fingertip = (111,-90)
turtle.up()
turtle.color("aquamarine")
turtle.goto(fingertip)
turtle.down()
turtle.circle(10)

#jeff bezos magic particle effects
turtle.pensize(5)
turtle.up()
turtle.color(245,162,61)
turtle.goto(141,-60)
turtle.down()
turtle.setheading(90)
turtle.forward(20)
turtle.up()
turtle.goto(161,-40)
turtle.right(30)
turtle.down()
turtle.forward(20)
turtle.up()
turtle.goto(141,-130)
turtle.setheading(270)
turtle.down()
turtle.forward(20)
turtle.up()
turtle.goto(161,-150)
turtle.left(30)
turtle.down()
turtle.forward(20)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
