import pygame as pg
import os
COLOR = (255, 100, 98)
SURFACE_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 800
IMAGESIZE = 64


class Sprite(pg.sprite.Sprite):
    InMotion = False
    Speed = 10

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pg.Surface([IMAGESIZE, IMAGESIZE])
        self.image.fill(SURFACE_COLOR)
        self.image = pg.image.load(os.path.join("Assets", "sprite.png"))
        self.rect = pg.Rect(x, y, IMAGESIZE, IMAGESIZE)

    def update(self, *args):
        super().update(self, *args)
        if self.InMotion == True:
            self.rect.x += self.Speed
            if self.rect.x > (WIDTH-IMAGESIZE) or self.rect.x < 0:
                self.Speed *= -1


class Bullet(pg.sprite.Sprite):
    InMotion = False
    Speed = 10

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pg.Surface([5, 10])
        self.image.fill((255, 100, 100))
        self.rect = pg.Rect(0, 0, 5, 10)

    def update(self, *args):
        super().update(self, *args)
        if self.InMotion == True:
            self.rect.y -= self.Speed
            if self.rect.y < 0:
                self.InMotion = False


class Score:
    Score = 0

    def render(self):
        myfont = pg.font.SysFont("monospace", 35)
        label = myfont.render(str(self.Score), 1, (0, 0, 0))
        screen.blit(label, (350, 350))


def shootBullet():
    global all_sprites_list
    bullet = Bullet((128, 128, 128), 50, 50)
    bullet.InMotion = not bullet.InMotion
    bullet.rect.x = player.rect.x
    bullet.rect.y = player.rect.y
    all_sprites_list.add(bullet)


pg.init()
all_sprites_list = pg.sprite.Group()
player = Sprite((255, 0, 0), 32, 700)
player.InMotion = True
all_sprites_list.add(player)
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Cody's Really Awesome Game")
running = True
while running:
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                shootBullet()
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pg.display.flip()
    clock.tick(60)
