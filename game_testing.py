import pygame as pg
pg.init()
vec = pg.math.Vector2  # 2 for two dimensional
HEIGHT = 850
WIDTH = 800
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
myfont = pg.font.SysFont("monospace", 35)
number_of_moves = 0


pg.display.set_caption("Game")
currx = 50
curry = 50
pg.draw.circle(screen, (255, 0, 0), (currx, curry), 50)
pg.display.update()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            # draw background first (however)
            screen.fill((255, 255, 255))
            m = pg.mouse.get_pos()
            currx = m[0]
            curry = m[1]
            number_of_moves = number_of_moves + 1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                currx = currx + 10
            if event.key == pg.K_LEFT:
                currx = currx - 10
            if event.key == pg.K_UP:
                curry = curry - 10
            if event.key == pg.K_DOWN:
                curry = curry + 10
            number_of_moves = number_of_moves + 1

    screen.fill((255, 255, 255))
    pg.draw.circle(screen, (65, 127, 25), (currx, curry), 35)
    pg.draw.circle(screen, (65, 127, 25), (currx*1.5, curry*1.5), 10)

    label = myfont.render(str(number_of_moves), 1, (0, 0, 0))
    screen.blit(label, (350, 350))

    pg.display.update()


def clearscreen():
    global screen
    screen.fill((255, 255, 255))
