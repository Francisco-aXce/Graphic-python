import pygame,random,sys
from functions import *

pygame.init()
#---Window
window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

#---EVENTS
PRICE_UPDATE = pygame.USEREVENT

#---EVENT TIMER
pygame.time.set_timer(PRICE_UPDATE, 150)


def main():

    maxInitialPrice = 50
    initialPrice = round(maxInitialPrice * random.random(), 2)
    actualPrice = initialPrice

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PRICE_UPDATE:
                actualPrice = randomSum(actualPrice)
                print(actualPrice)

        window.fill((0,0,0))



        pygame.display.flip()

if __name__ == "__main__":
    main()