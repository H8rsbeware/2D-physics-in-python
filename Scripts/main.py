import sys, pygame, UI

#Initalise pygame window and return the display as a var
def startup():
    pygame.init()
    size = width, height = 1500,1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2D Physics")
    return screen

def main():
    screen = startup()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255,255,255))

        point1 = UI.point(screen,500,500)
        point2 = UI.point(screen,1000,500)
        group1 = UI.pair(screen,point1,point2)

        group1.updateAll()



        pygame.display.update()




if __name__ == "__main__":
    main()