import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 50
imageWidth = 50

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

img = pygame.image.load('square.png')


def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: " + str(count), True, black)
    surface.blit(text, [50, 50])

def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, black, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, black, [x_block, y_block + block_height + gap, block_width, surfaceHeight])



def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    return(None)

def makeTextObjs(text, font):
    textSurface = font.render(text, True, black)
    return(textSurface, textSurface.get_rect())

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()



def gameOver():
    msgSurface('You died!')


def flappy_bird(x, y, image):
    surface.blit(img, (x, y))


def main():
    game_over = False
    x = 150 
    y = 200 

    y_move = 5

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0, surfaceWidth / 2)
    gap = imageHeight * 3
    block_move = 4

    current_score = 0

    while not game_over:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.fill(white)
        flappy_bird(x, y, img)
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap)
        x_block -= block_move


        if y > surfaceHeight - 40 or y < 0:
            gameOver()

        if x_block < (-1 * block_width):
            x_block = surfaceWidth
            block_height = randint(0, surfaceWidth / 2)

        if x + imageWidth > x_block:
            if x < x_block + block_width:
                if y < block_height:
                    if x - imageWidth < block_width + x_block:
                        gameOver()

        if x + imageWidth > x_block:
            if y + imageHeight > block_height + gap:
                if x < block_width + x_block:
                    gameOver()

        if x < x_block and x > x_block - block_move:
            current_score += 1

        if current_score % 3 == 0:
            block_move += 0.005


        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
