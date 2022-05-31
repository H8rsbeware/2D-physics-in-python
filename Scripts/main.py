import sys, pygame, env, UI, maths
import rigidbody as rb


# Initalise pygame window and return the display as a var
def startup():
    pygame.init()
    global width, height
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("2D Physics")
    return screen





def main():
    mouseDown = False
    mouseDownFor = 0
    play = False
    screen = startup()
    clock = pygame.time.Clock()

    renderGroup = env.renderGroup()
    playBtn = UI.btn(screen, 25, 25, 50, 50, '../images/play-outline.png',
                     '../images/play-solid.png', '../images/pause-outline.png', '../images/pause-solid.png')

    # Object creation
    point1 = env.point(screen, 80, 130)
    point25 = env.point(screen, 150, 80)
    point2 = env.point(screen, 220, 130)
    point3 = env.point(screen, 200, 200)
    point4 = env.point(screen, 100, 200)
    rgb = rb.rigidbody(screen, [point1, point25, point2, point3, point4], 3)
    renderGroup.rbs.append(rgb)
    rgb.showColliders(True, True)
    renderGroup.btns.append(playBtn)

    fl1 = env.point(screen, 0, 970)
    fl2 = env.point(screen, 1500, 970)
    fl3 = env.point(screen, 1500, 1000)
    fl4 = env.point(screen, 0, 1000)
    flb = rb.rigidbody(screen, [fl1, fl2, fl3, fl4], 0)
    renderGroup.rbs.append(flb)

    while 1:
        mousex, mousey = pygame.mouse.get_pos()
        c = maths.checkColliders(renderGroup)
        if c is not None:
            print(maths.getColliderAdjustments(screen, c[0], c[1]))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
                if playBtn.hover:
                    mouseDownFor = 41
                    if playBtn.face == 1:
                        playBtn.face = 0
                        play = True
                    else:
                        playBtn.face = 1
                        play = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseDown = False
                if mouseDownFor < 80:
                    z = env.point(screen, mousex, mousey)
                    renderGroup.points.append(z)
                mouseDownFor = 0

        if pygame.mouse.get_pressed(num_buttons=3):
            mouseDownFor += 1

        screen.fill((255, 255, 255))

        if not play:
            rgb.acceleration = (0, 0)
        else:
            rgb.acceleration = (rgb.acceleration[0], -9.81)

        renderGroup.update()
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
