import pygame

class Tab:

    def __init__(self,name,xPos,yPos, tittleFont, w = 130, h=24,):

        #..Visual
        self.rect = pygame.Rect(xPos,yPos,w,h)
        self.activeColor = (29, 209, 161)
        self.inactiveColor = (16, 172, 132)
        self.tittleFont = tittleFont

        self.active = False
        self.name = name
    
    def draw(self, window):
        pygame.draw.rect(window, self.activeColor if self.active else self.inactiveColor, self.rect)
        window.blit(self.tittleFont.render(self.name, True, (240,240,240)), (self.rect.left + 5, self.rect.top))

        #CONTENT
        if self.active:
            window.blit(self.tittleFont.render(self.name, True, (240,240,240)), (self.rect.left + 5, self.rect.top+50))

class TabManager:

    def __init__(self, xPadding, yPadding, window):
        
        #..Visual
        self.backgroundRect = pygame.Rect(xPadding,yPadding,
            window.get_size()[0] - (xPadding*2), window.get_size()[1] - (yPadding*2))
        self.contentRect = pygame.Rect(xPadding,yPadding+30,
            window.get_size()[0] - (xPadding*2), window.get_size()[1] - (yPadding*2) - 30)

        self.backgroundColor = (34, 47, 62)
        self.contentColor = (87, 101, 116)

        self.tabs = []
        self.padding=(xPadding,yPadding)

    def addTab(self,name,tabFont):
        if len(self.tabs) == 0:
            self.tabs.append(Tab(name, self.padding[0]+3,self.padding[1]+3, tabFont))
        else:
            self.tabs.append(Tab(name,
            (self.tabs[len(self.tabs)-1].rect.right)+3,
            self.padding[1]+3, tabFont))

    def draw(self, window):
        pygame.draw.rect(window, self.backgroundColor, self.backgroundRect)
        pygame.draw.rect(window, self.contentColor, self.contentRect)
        for tab in self.tabs:
            tab.draw(window)
    
    def tabsEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(self.tabs) > 0:
            pos = pygame.mouse.get_pos()
            for tab in self.tabs:
                if tab.rect.collidepoint(pos):
                    for tab2 in self.tabs:
                        tab2.active = False
                    tab.active = True
