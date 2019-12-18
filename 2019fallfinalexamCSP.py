#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Christopher Brinkley
#Date
#12/18/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl 


#create turtle
sketch = trtl.Turtle()


#movement functions
def up():
    sketch.seth(90)
    sketch.forward(10)

def down():
    sketch.seth(270)
    sketch.forward(10)

def left():
    sketch.seth(180)
    sketch.forward(10)

def right():
    sketch.seth(0)
    sketch.forward(10)

# def o():


#def p(): 


def u():if


#def space():



#color/drawing functions



#create screen
sn = trtl.Screen()

#bind to keypresses
sn.onkeypress(up, "Up")
sn.onkeypress(down, "Down")
sn.onkeypress(left, "Left")
sn.onkeypress(right, "Right")

#listen
sn.listen()

#mainloop
sn.mainloop()