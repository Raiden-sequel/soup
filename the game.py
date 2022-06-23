import pygame, random, time
from chara import Player
from chara import Zombie
from chara import Bullet

global hd, vd

import math
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
grey  = (155, 155, 155)
blue  = (0, 0, 255)
green = (0, 255, 0)
red   = (255, 0, 0)
q     = (100, 100, 0)

mouseX = 0
mouseY = 0
player_x = 0
player_y = 0
speed = 5
zspeed = 3
zspeed2 = 2.5
zspeed3 = 1
zspeed4 = 1.5
zspeed5 = 1
zspeed6 = 2
zspeed7 = 3
Shoot = False
angle = 0
angle2 = 0
direct_x = 0
direct_y = 0
zomb_x = 0
zomb_y = 0
score = 0
keys = pygame.key.get_pressed()
die = False
    
screenWide = 1280
screenHigh = 720
size = (screenWide, screenHigh)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
pygame.display.set_caption("virus.com")

all_sprites_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
zombois = pygame.sprite.Group()

player = Player(blue, 30, 30, 640)
player.rect.x = 610
player.rect.y = 330

zomb = Zombie(green, 30, 30)
zomb.rect.x = 0
zomb.rect.y = 0

zomb2 = Zombie(green, 30, 30)
zomb2.rect.x = 1340
zomb2.rect.y = 750

zomb3 = Zombie(green, 30, 30)
zomb3.rect.x = 0
zomb3.rect.y = 750

zomb4 = Zombie(green, 30, 30)
zomb4.rect.x = 1340
zomb4.rect.y = 0

zomb5 = Zombie(red, 50, 50)
zomb5.rect.x = 200
zomb5.rect.y = 200

zomb6 = Zombie(red, 25, 25)
zomb6.rect.x = 200
zomb6.rect.y = 200

zomb7 = Zombie(q, 30, 30)
zomb7.rect.x = -30
zomb7.rect.y = -30

bullet = Bullet(grey, 10, 10, 0, 13)
bullet.rect.x = 3000
bullet.rect.y = 3000

bullets.add(bullet)
all_sprites_list.add(player)
all_sprites_list.add(zomb)
all_sprites_list.add(zomb2)
all_sprites_list.add(zomb3)
all_sprites_list.add(zomb4)
all_sprites_list.add(zomb5)
all_sprites_list.add(zomb6)
all_sprites_list.add(zomb7)

zombois.add(zomb)
zombois.add(zomb2)
zombois.add(zomb3)
zombois.add(zomb4)
zombois.add(zomb5)
zombois.add(zomb6)
zombois.add(zomb7)

#font = pygame.font.Font('freesansbold.ttf', 32)
#text = font.render(str(score), True, black, white)
#textRect = 4, 5 #text.get_rect()

carryOn = True
clock = pygame.time.Clock()

def rotate():
    global mouseX, player_x, mouseY, player_y, angle, rel_x, rel_y
    rel_x, rel_y = mouseX - player_x, mouseY - player_y
    angle = math.atan2(rel_y, rel_x)

def shoot():
    global Shoot, direct_x, direct_y, angle2
    bullet.rect.x = player_x - 5
    bullet.rect.y = player_y - 5
    angle2 = angle
   # print('test2')
    Shoot = True

def colide_check():
    global score

    if zomb.rect.x < bullet.rect.x:
        if zomb.rect.x + 30 > bullet.rect.x:
            if zomb.rect.y < bullet.rect.y:
                if zomb.rect.y + 30 > bullet.rect.y:
                    print('hit')
                    zomb.rect.x = random.randint(0, 1280)
                    zomb.rect.y = -40
                    score += 100
                    
    if zomb2.rect.x < bullet.rect.x:
        if zomb2.rect.x + 30 > bullet.rect.x:
            if zomb2.rect.y < bullet.rect.y:
                if zomb2.rect.y + 30 > bullet.rect.y:
                    print('hit')
                    zomb2.rect.x = random.randint(0, 1280)
                    zomb2.rect.y = 760
                    score += 100

    if zomb3.rect.x < bullet.rect.x:
        if zomb3.rect.x + 30 > bullet.rect.x:
            if zomb3.rect.y < bullet.rect.y:
                if zomb3.rect.y + 30 > bullet.rect.y:
                    print('hit')
                    zomb3.rect.y = random.randint(0, 720)
                    zomb3.rect.x = -40
                    score += 100
                    
    if zomb4.rect.x < bullet.rect.x:
        if zomb4.rect.x + 30 > bullet.rect.x:
            if zomb4.rect.y < bullet.rect.y:
                if zomb4.rect.y + 30 > bullet.rect.y:
                    print('hit')
                    zomb4.rect.y = random.randint(0, 720)
                    zomb4.rect.x = 1320
                    score +=100

    if zomb6.rect.x < bullet.rect.x:
        if zomb6.rect.x + 25 > bullet.rect.x:
            if zomb6.rect.y < bullet.rect.y:
                if zomb6.rect.y + 25 > bullet.rect.y:
                    print('hit')
                    zomb6.rect.y = zomb5.rect.y
                    zomb6.rect.x = zomb5.rect.x
                    score +=10

    if zomb7.rect.x < bullet.rect.x:
        if zomb7.rect.x + 30 > bullet.rect.x:
            if zomb7.rect.y < bullet.rect.y:
                if zomb7.rect.y + 30 > bullet.rect.y:
                    print('hit')
                    score +=10
                    
def game_over():
    keys = pygame.key.get_pressed()
    font = pygame.font.Font('freesansbold.ttf', 90)
    textRect = 300, 200 #text.get_rect()
    text = font.render(str('you lost'), True, black, white)
    screen.blit(text, textRect)

    all_sprites_list.update()
    pygame.display.flip()
    time.sleep(100)
    clock.tick(60)

   #     if keys[pygame.K_o]:
    #        pygame.quit()
      #      carryOn = False
                
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True
    screen.fill(white)
    largeText = pygame.font.SysFont("comicsansms",25)
    TextSurf, TextRect = text_objects("left5dead6: there are zombies in las vegas and you are there also", largeText)
    TextRect.center = ((screenWide/2),(screenHigh/2))
    screen.blit(TextSurf, TextRect)
    largeText = pygame.font.SysFont("comicsansms",35)
    TextSurf, TextRect = text_objects("press Enter to enter", largeText)
    TextRect.center = ((screenWide/2),(screenHigh/2 + 50))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)
    
    while intro:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_o]:
            pygame.quit()
            carryOn = False

        if keys[pygame.K_RETURN]:
            intro = False



def game_loop():
    
    global mouseX, player_x, mouseY, player_y, hd, vd, carryOn
    pygame.init(), Shoot, angle, direct_x, direct_y, angle2
    
    playa = player
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, black, white)
    textRect = 4, 5 #text.get_rect(
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill(white)
    screen.blit(text, textRect)
    all_sprites_list.draw(screen)
    if Shoot == True:
     #   print('test3')
        bullets.draw(screen)
        bullet.move(angle2)
    player_x = player.rect.x + 15
    player_y = player.rect.y + 15
    player_pos = player.rect.center
    
    zomb_x = zomb.rect.x + 15
    zomb_y = zomb.rect.y + 15
    zomb_pos = zomb.rect.center
    
    zomb2_x = zomb2.rect.x + 15
    zomb2_y = zomb2.rect.y + 15
    zomb2_pos = zomb2.rect.center
    
    zomb3_x = zomb3.rect.x + 15
    zomb3_y = zomb3.rect.y + 15
    zomb3_pos = zomb3.rect.center
    
    zomb4_x = zomb4.rect.x + 15
    zomb4_y = zomb4.rect.y + 15
    zomb4_pos = zomb4.rect.center

    zomb5_x = zomb5.rect.x + 25
    zomb5_y = zomb5.rect.y + 25
    zomb5_pos = zomb5.rect.center
    
    zomb6_x = zomb6.rect.x + 12.5
    zomb6_y = zomb6.rect.y + 12.5
    zomb6_pos = zomb6.rect.center

    zomb7_x = zomb7.rect.x + 15
    zomb7_y = zomb7.rect.y + 15
    zomb7_pos = zomb7.rect.center
    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              carryOn = False
        if event.type == pygame.MOUSEMOTION:
               mousex, mousey = event.pos
#               print(mousex, mousey)
        if event.type == pygame.MOUSEBUTTONDOWN:
         #   print('test1')
            shoot()
    
    if keys[pygame.K_a] and player.rect.left > 0:
        player.moveLeft(speed)
    if keys[pygame.K_d] and player.rect.right < screenWide:
        player.moveRight(speed)
    if keys[pygame.K_w] and player.rect.top > 0:
        player.moveUp(speed)
    if keys[pygame.K_s] and player.rect.bottom < screenHigh:
        player.moveDown(speed)
    
    if keys[pygame.K_o]:
        pygame.quit()
        carryOn = False
    
    if zomb_x > player_x:
        zomb.moveH(zspeed)
    if zomb_x < player_x:
        zomb.moveH(-zspeed)
    if zomb_y > player_y:
        zomb.moveV(zspeed)
    if zomb_y < player_y:
        zomb.moveV(-zspeed)
    
    if zomb2_x > player_x:
        zomb2.moveH(zspeed2)
    if zomb2_x < player_x:
        zomb2.moveH(-zspeed2)
    if zomb2_y > player_y:
        zomb2.moveV(zspeed2)
    if zomb2_y < player_y:
        zomb2.moveV(-zspeed2)

    if zomb3_x > player_x:
        zomb3.moveH(zspeed3)
    if zomb3_x < player_x:
        zomb3.moveH(-zspeed3)
    if zomb3_y > player_y:
        zomb3.moveV(zspeed3)
    if zomb3_y < player_y:
        zomb3.moveV(-zspeed3)

    if zomb4_x > player_x:
        zomb4.moveH(zspeed4)
    if zomb4_x < player_x:
        zomb4.moveH(-zspeed4)
    if zomb4_y > player_y:
        zomb4.moveV(zspeed4)
    if zomb4_y < player_y:
        zomb4.moveV(-zspeed4)

    if zomb5_x > player_x:
        zomb5.moveH(zspeed5)
    if zomb5_x < player_x:
        zomb5.moveH(-zspeed5)
    if zomb5_y > player_y:
        zomb5.moveV(zspeed5)
    if zomb5_y < player_y:
        zomb5.moveV(-zspeed5)

    if zomb6_x > player_x:
        zomb6.moveH(zspeed6)
    if zomb6_x < player_x:
        zomb6.moveH(-zspeed6)
    if zomb6_y > player_y:
        zomb6.moveV(zspeed6)
    if zomb6_y < player_y:
        zomb6.moveV(-zspeed6)

    if zomb7_x <= 15:
        hd = 'right'
    if zomb7_x >= screenWide - 15:
        hd = 'left'
    if zomb7_y <= 15:
        vd = 'down'
    if zomb7_y >= screenHigh - 15:
        vd = 'up'

    if hd == 'right':
        zomb7.moveH(-zspeed7)
    elif hd == 'left':
        zomb7.moveH(zspeed7)
    if vd == 'up':
        zomb7.moveV(zspeed7)
    elif vd == 'down':
        zomb7.moveV(-zspeed7)
    
    colide_check()
    #print(zomb.rect.x, zomb.rect.y, bullet.rect.x, bullet.rect.y)
    
    z_collision_list = pygame.sprite.spritecollide(playa,zombois,False)
    for playa in z_collision_list:
        print("you got", score, "points")

        die = True
        carryOn = False

    all_sprites_list.update()
    bullets.update()
    
    rotate()
  #  print(angle)
    dest = player_pos
    pygame.transform.rotate(player.image, angle)
   # player.rotate()
  #  screen.blit(player.rotatedRect)
    pygame.display.flip()
    clock.tick(60)

game_intro()
while carryOn == True:
    game_loop()
    
if carryOn == False:
    game_over()

#while True:
   # clock.tick(60)
    
pygame.quit()


#610 330 620 340

