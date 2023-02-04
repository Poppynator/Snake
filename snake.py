import pygame
import sys
import random

#init Pygame
pygame.init()

#window size
window_size = (800, 600)
#create screen
screen = pygame.display.set_mode(window_size)

#set title
pygame.display.set_caption("Snake Game")

# colors for snakegame
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# size of snake
block_size = 10

# FPS
clock = pygame.time.Clock()
fps = 30

# snake list
snakelist = []
snake_length = 1

# food new position
def food():
    foodx = random.randrange(0, window_size[0], block_size)
    foody = random.randrange(0, window_size[1], block_size)

# draw snake
def snake():
    for x,y in snakelist:
        pygame.draw.rect(screen, black, [x, y, block_size, block_size])

# Game loop
def gameloop():
    running = True

    # init snake Position
    x1 = 300
    y2 = 300
    snakelist.append((x, y))

    #init food Position
    food()

    # game loop
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update screen
        pygame.display.update()

        food()

        # draw snake
        snake()
    
    pygame.quit()
    sys.exit()

def main():
    gameloop()

main()
