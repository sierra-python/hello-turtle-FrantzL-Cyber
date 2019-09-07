import turtle

tango = turtle.Turtle()
tango.begin_fill() #to color in the shape that is that is made after 
if tango.filling():
    tango.color('red')
else:
    tango.color('blue')
    
tango.forward(50) #starting a rectangle
tango.degrees(360) #spinning the cursor
tango.right(1000) #continuing to spin cursor by making it spin right 1000 degrees
tango.setheading(90) #sets tango facing north
tango.forward(200) #drawing the right line of the rectangle
tango.left(90) #rotate left 90 degrees
tango.forward(50) #drawing the top of the rectangle 
tango.left(90) #rotate left 90 degrees
tango.forward(200) #completing the rectangle
tango.end_fill() #finishing the instruction to fill the rectangle red

tango.penup() #lifting the pen off the drawing surface
tango.right(45) #shifting the left in preperation of the circle
tango.forward(30)
tango.pendown() #putting the pen back down to start drawing again

tango.color("blue", "orange") #changing the color of tango to blue with the interior orange
tango.begin_fill()
tango.circle(50) #drawing the circle
tango.end_fill()

tango.penup()
tango.goto(60, 50) #telling tango to go to position x=60 y=50
tango.pendown()

tango.turtlesize(5)
tango.setheading(90) #tango is now facing north
tango.color("black") #changing the color to black
tango.forward(50) #moving up to start the F
tango.right(90) #rotates tango right 90 degrees
tango.forward(15) #writes the smaller line of the F
tango.backward(15) #returns to the leftmost line on the F
tango.left(90) #rotates left 90 degrees
tango.forward(40) #writes the portion connecting the middle to the top of the letter
tango.right(90) #rotates right 90 degrees
tango.forward(40) #draws the top part of the letter

tango.penup() #lifts tango off
tango.goto(0,0) #returns tango to the point of origin at x=0 y=0
tango.pendown() #puts tango back on the drawing surface
