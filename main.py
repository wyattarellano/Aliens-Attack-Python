import pygame
from typing import List
pygame.init()

#DATA DEFINITIONS
'''
A World is a (world Rocket Aliens Dir Shots Tics2shoot)
A Rocket is a (rocket X)
An Alien is a (alien Dir Health)
A Shot is a (shot X Y)
Dir is one of: "left" "right"
Health is a natnum between 0 and 3
Aliens(LOA) is a List of Alien
Shots(LOS) is a List of Shot
'''

#Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tick = pygame.time.Clock()
tick_rate = 60  # frames per second

#Color constants
PINK = (255, 192, 203)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

#Rocket Constants
ROCKET_Y = SCREEN_HEIGHT - 60

#Shot Constants
INIT_T2S = 0  # initial tics to shoot
RESET_T2S = 60 #tics to wait between shots

#alien
class alien:
    def __init__(self, x, y, health, dir):
        self.x = x  # x position of alien
        self.y = y  # y position of alien
        self.health = health  # health of alien - natnum between 0 and 3
        self.dir = dir

    def __draw__(self, screen):
        if self.health == 3:
            color = GREEN
        elif self.health == 2:
            color = YELLOW
        else:
            color = RED
        pygame.draw.rect(screen, color, (self.x, self.y, 20, 20))

    def __move__(self, dir):
        if dir == "left":
            self.x -= 1
        elif dir == "right":
            self.x += 1
        else:
            self.y += 20

#To draw a list of aliens on screen
def drawLOA(screen, aliens: List[alien]):
    for a in aliens:
        a.__draw__(screen)

#Rocket
class rocket:
    def __init__(self, x):
        self.x = x  # x position of rocket since rocket does not move vertically

    def __draw__(self, screen):
        pygame.draw.rect(screen, PINK, (self.x, ROCKET_Y, 40, 20))

    def __moveLeft__(self):
        self.x = self.x - 20
    
    def __moveRight__(self):
        self.x = self.x + 20


#shot
class shot:
    def __init__(self, x, y):
        self.x = x  # x position of shot
        self.y = y  # y position of shot

    def __draw__(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 10)

    def __move__(self):
        self.y -= 20

#To draw a list of shots on screen
def drawLOS(screen, shots: List[shot]):
    for s in shots:
        s.__draw__(screen)



#world
class world:
    def __init__(self, rocket: rocket, aliens: List[alien], dir, shots: List[shot], tics2shoot: int):
        self.rocket = rocket  # player rocket
        self.aliens = aliens  # enemy aliens
        self.dir = dir  # direction of aliens
        self.shots = shots  # shots fired by player
        self.tics2shoot = tics2shoot  # tics until player can shoot again

    #draw a world
    def __draw__(self, screen):
        self.rocket.__draw__(screen)
        self.aliens.drawLOA(screen)
        self.shots.drawLOS(screen)

    #process a key for the world
    def __processKey__(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rocket.__moveLeft__()
        elif key[pygame.K_RIGHT]:
            self.rocket.__moveRight__()
        elif key[pygame.K_SPACE]:
            self.shots.insert(0, shot(self.rocket.x, self.rocket.y))
        else:
            self




        




#INITIAL VALUES
INIT_LOA = [alien(50 + i * 30, 50, 3) for i in range(10)]
INIT_ROCKET = rocket(SCREEN_WIDTH // 2)
INIT_LOS = []
INIT_WORLD = world(INIT_ROCKET, INIT_LOA, "right", INIT_LOS, INIT_T2S)






