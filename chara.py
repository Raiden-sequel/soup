import pygame
import math

class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height, position):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.color = color
        self.position = 640, 370
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()


    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels
        
    def moveForward(self, pixels):
        self.rect.y += pixels
        
    def rotate(self):
        global rotatedRect
        rotatedRect = pygame.transform.rotate(self.image, int(45))
 #       screen.blit(rotatedRect)

#        self.image = pygame.transform.rotate(self.image, int(45))
  #      self.rect = self.image.get_rect(center=self.position)
        



class Zombie(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()

    def moveH(self, pixels):
        self.rect.x -= pixels

    def moveV(self, pixels):
        self.rect.y -= pixels

        



class Bullet(pygame.sprite.Sprite):

    def __init__(self, color, width, height, direction, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        self.direction=math.radians(direction)
        self.speed = speed

    def move(self, angle2):
        self.rect.x += self.speed * math.cos(angle2)
        self.rect.y += self.speed * math.sin(angle2)




        
