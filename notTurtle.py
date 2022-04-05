import turtle
colour = 0
length = 1
angll   = 0
from turtle import *
begin_fill()
turtle.pensize(2)
while length != '0':
#line draws a line, circle draws a circle, go moves the turtle without drawing, shapeMake stores how to make a shape, shapePaste pastes the stored shape
#the program is just gonna keep asking what you want to do from the list until you make the length of something 0, then it fills and stops
    want = input('what do you want(line, circle, go, shapeMake, shapePaste):')
    if want == 'line' :
      #this makes a line         
       colour = input('pick a colour:')
       length = input('how long is the line:')
       angll  = input('how left is the turn:')
       from turtle import *
       color(colour, colour)
       turtle.left (int(angll))
       turtle.forward (int(length))
    else :
       #this makes a circle
        if want == 'circle' :
            colour = input('pick a colour:')
            
            length = input('how big is the circle:')
            from turtle import *
            color(colour)
            turtle.circle (int(length))
        else :
           #this moves the turtle without drawing
            if want == "go" :
                
                length = input('how far do you want to go:')
                angll  = input('how left is the turn:')
                from turtle import *
                turtle.pu()
                turtle.left (int(angll))
                turtle.forward (int(length))
                turtle.pd()
            else :
               #you make a shape and it stores it
                if want == 'shapeMake' :
                       colourM = input('pick a colour:')
                       lengthM = input('how long is the line:')
                       angllM  = input('how left is the turn:')
                       loopM   = input('how many loop:')
                       def shapePaste():
                         #this stores whatever you input in shapeMake
                          color(colourM, colourM)
                          turtle.left (int(angllM))
                          turtle.forward (int(lengthM))
                          return
                else :
                   #makes shape stored in shapeMake
                    if want == 'shapePaste' :
                        from turtle import *
                        for x in range(int(loopM)):
                            shapePaste()
           
end_fill()
done()
