import turtle

def squarez(x, y, fill):
    turtle.pu()
    move = 4
    turtle.goto(x, y)
    turtle.pd()


    

    if fill == True:

        turtle.begin_fill()
        while move > 0:
            turtle.forward(75)
            turtle.left(90)
            move = move - 1
        turtle.end_fill()
            
    else:
            
        while move > 0:
            turtle.forward(75)
            turtle.left(90)
            move = move - 1
