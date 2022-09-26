import turtle
import random
import squarez

turtle.color('black','blue')
turtle.screensize(canvwidth = 900, canvheight = 900)
turtle.window_height = 900
turtle.window_width = 900
turtle.speed(100)
turtle.fillcolor('black')

row = 1
count = 8
x = -300
y = 225
fill = False

def fl_check():
    global fill 
    if fill == False :
        fill = True
    else:
        fill = False

while row < 9 :
    
    while count > 0:
        squarez.squarez(x, y, fill)
        fl_check()
            
        x += 75
        count -= 1
    y -= 75
    x = -300
    row += 1
    count = 8
    fl_check()
    



turtle.done()
