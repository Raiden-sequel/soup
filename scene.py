import random
import shapez
import turtle

turtle.color('black','blue')
turtle.speed(1000000000000000)
turtle.fillcolor('black')
turtle.colormode(255)
blue  = (150, 200, 255)
brown = (150, 100, 100)
lgreen = (130, 255, 25)
baige = (225, 180, 170)
lbaige =(210, 180, 220)
turtle.bgcolor(blue)

draw_c = shapez.circlez
draw_s = shapez.squarez
draw_t = shapez.trianglez
draw_f1 = shapez.flowa_stem
draw_f2 = shapez.flowa_top

row = 0
count = 0
x = 0
y = 0
size = 50 / 100
fill = False

def fl_check():
    global fill 
    if fill == False :
        fill = True
    else:
        fill = False

turtle.fillcolor('green')
draw_s(-750, -2150, 2000, True)
turtle.fillcolor('yellow')
draw_c(-250, 150, 600, True)
turtle.fillcolor(baige)
draw_s(-100, -150, 200, True)
turtle.fillcolor(brown)
draw_s(-25, -150, 50, True)
draw_t(-125, 50, 250, True)
turtle.fillcolor(lbaige)
draw_s(-70, -50, 40, True)
draw_s(30, -50, 40, True)

while True:
    x = random.randint(-300, 300)
    y = random.randint(-250, -130)
    colorN = random.randint(1, 3)
    turtle.fillcolor(lgreen)
    draw_f1(x, y, 20)
    if colorN == 1:
        turtle.fillcolor('blue')
    if colorN == 2:
        turtle.fillcolor('yellow')
    if colorN == 3:
        turtle.fillcolor('red')
    draw_f2(5)


