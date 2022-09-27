import turtle

def squarez(x, y, size, fill):
    turtle.pu()
    move = 4
    turtle.goto(x, y)
    turtle.pd()

    if fill == True:

        turtle.begin_fill()
        while move > 0:
            turtle.forward(size)
            turtle.left(90)
            move = move - 1
        turtle.end_fill()
            
    else:
            
        while move > 0:
            turtle.forward(size)
            turtle.left(90)
            move = move - 1

def circlez(x, y, size, fill):
    turtle.pu()
    move = 50
    turtle.goto(x, y)
    turtle.pd()

    if fill == True:

        turtle.begin_fill()
        while move > 0:
            turtle.forward(size/ 100)
            turtle.left(7.2)
            move = move - 1
        turtle.end_fill()
            
    else:
            
        while move > 0:
            turtle.forward(size/ 100)
            turtle.left(7.2)
            move = move - 1

def trianglez(x, y, size, fill):
    turtle.pu()
    move = 1
    turtle.goto(x, y)
    turtle.pd()

    if fill == True:

        turtle.begin_fill()
        while move > 0:
            turtle.forward(size)
            turtle.left(150)
            turtle.forward(size/ 1.75)
            turtle.left(60)
            turtle.forward(size/ 1.75)
            turtle.left(150)
            move = move - 1
        turtle.end_fill()
            
    else:
            
        while move > 0:
            turtle.forward(size)
            turtle.left(120)
            move = move - 1

def flowa_stem(x, y, size):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()

    turtle.begin_fill()
   
    turtle.left(180)
    turtle.forward(size / 5)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 5)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 5)
    turtle.left(180)

    turtle.end_fill()

def flowa_top(size):
    turtle.begin_fill()
    move = 8

    while move > 0:
        turtle.forward(size)
        turtle.left(45)
        move = move - 1
        
    turtle.end_fill()
    
    
    
    



