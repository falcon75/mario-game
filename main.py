# Dependencies
import logic
import time
import pygame

# Function for iterating through game object list and drawing all

def redraw(objects):
    ob = game.target
    x = ob.dimensions[0]
    y = ob.defaultPosition[0]
    offset = x - y
    if  offset < 0:
        offset = 0
    elif offset >= game.mb[0] - 2 * y - ob.dimensions[2]:
        offset = game.mb[0] - 2 * y - ob.dimensions[2]
    screen.fill((0xFF,0xFF,0xFF))
    screen.blit(background,(0 - offset,0))
    for item in objects:
        if item.id == 'player':
            if item.xVelocity < 0:
                screen.blit(mario2,(item.dimensions[0] - offset,item.dimensions[1]))
            else:
                screen.blit(mario, (item.dimensions[0] - offset, item.dimensions[1]))
        elif (item.id == 'goomba'):
            if picset == True:
                screen.blit(goomba1, (item.dimensions[0] - offset, item.dimensions[1]))
            else:
                screen.blit(goomba2, (item.dimensions[0] - offset, item.dimensions[1]))
        elif item.id == 'block':
            screen.blit(block1, (item.dimensions[0] - offset, item.dimensions[1]))
        else:
            pygame.draw.rect(screen, (0, 0, 0), item.dimensions)
    pygame.display.flip()

# Game Setup
pygame.init()
screen_size = [700,500]
screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
pygame.key.set_repeat(2,2)

# Loads images for use in graphics
'''
mario = pygame.image.load('mario.png')
mario2 = pygame.image.load('mario2.png')
marioBig = pygame.image.load('mario_big.png')
goomba1 = pygame.image.load('goomba.png')
goomba2 = pygame.image.load('goomba2.png')
background = pygame.image.load('background.png')
block1 = pygame.image.load('block.png')
'''

# Initialisation of game

game = logic.PlatformGame(screen_size, [2000,500])
game.createFloor()
redraw(game.objects)
t1 = time.time()
picset = False
t2 = time.time()

# Main Loop

while not game.fail:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == 275:
                game.target.xVelocity = 10

            elif event.key == 276:
                game.target.xVelocity = -10

            elif event.key == 273:
                game.target.changeSize([40,60])
                game.target.shrunk = False

            elif event.key == 274:
                game.target.changeSize([40,40])
                game.target.shrunk = True

            elif (event.key == 32) and (game.target.contact == True):
                game.target.jump()

            elif event.key == 307:
                game.RandomEnemy()

        elif event.type == pygame.KEYUP:

            if event.key in [275,276]:
                game.target.xVelocity = 0

    # Runs (x axis) all dynamic objects
    game.run()

    # Falls (y axis) all dynamic objects
    game.fall(t1)

    # Stores last time for use in the fall function
    t1 = time.time()

    # Creates alternating boolean every 0.25s to animate images
    if (time.time() - t2) > 0.25:
        t2 = time.time()
        picset = not picset

    # Draws all changes to the environment
    redraw(game.objects)

    # Makes the refresh rate occur at a maximum of 60 times per second
    clock.tick(30)

input()
