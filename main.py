import pygame,random,sys
from functions import *
from tab_manager import *

#---Fonts
pygame.font.init()
tabFont = pygame.font.SysFont('arial', 20, True)

pygame.init()
#---Window
window = pygame.display.set_mode((1024,800))
clock = pygame.time.Clock()

#---EVENTS
PRICE_UPDATE = pygame.USEREVENT

#---EVENT TIMER
pygame.time.set_timer(PRICE_UPDATE, 150)


def main():

    maxInitialPrice = 50
    initialPrice = round(maxInitialPrice * random.random(), 2)
    actualPrice = initialPrice

    #..Tabs
    tabManager = TabManager(16,16,window)

    tabManager.addTab("tst", tabFont)
    tabManager.addTab("tst2", tabFont)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PRICE_UPDATE:
                actualPrice = randomSum(actualPrice)
                print(actualPrice)
            tabManager.tabsEvents(event)

        window.fill((0,0,0))

        tabManager.draw(window)

        pygame.display.flip()

if __name__ == "__main__":
    main()