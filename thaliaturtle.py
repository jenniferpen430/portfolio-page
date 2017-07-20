from turtle import *
import math

# Variables boi.
t = Turtle()


#User inputs
num_side = int(input("How many sides do you want? "))
side_len = int(input("How long should the shape be?"))
color = input("What color do you want? ")
thicc = input("How thicc do you want it? (10-50 pls) ")

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.pu()
t.setposition(x_pos - (side_len - 50) , y_pos - (side_len - 50 ))

### pensize:
t.pd()
t.pencolor(color)
t.pensize(thicc)

##filling shae
t.color(color)
t.begin_fill()

#making the shape
for i in range(num_side):
    t.fd(side_len)
    t.rt(360/num_side)

#filling the shape
t.end_fill()

# Close window on click.
exitonclick()
