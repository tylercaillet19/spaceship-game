import pygame as pg
import os

pg.display.set_caption("Spaceship Game")
WIDTH, HEIGHT = 1500, 800
WIN = pg.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (255, 255, 255)
BG_HEIGHT, BG_WIDTH = 1500, 800
BG_IMAGE = pg.image.load(os.path.join('Assets', '5379387.webp'))
BG = pg.transform.scale(BG_IMAGE, (BG_HEIGHT, BG_WIDTH))


FPS = 60
VEL = 10
BOOST_VEL = 15

PROJECTILE_SPEED = 15

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 120, 95
BULLET_WIDTH, BULLET_HEIGHT = 50, 40


SPACESHIP_IMAGE = pg.image.load(os.path.join('Assets', 'ufo.png'))
SPACESHIP = pg.transform.scale(
    SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

BULLET_IMAGE = pg.image.load(os.path.join('Assets', 'bullet.png'))
BULLET = pg.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))


def draw_window(yellow, bullet):
    WIN.blit(BG, (0, 0))
    WIN.blit(SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(BULLET, (bullet.x, bullet.y))
    pg.display.update()


def spaceship_movement(keys_pressed, yellow):
    global SPACESHIP, ROTATION
    if keys_pressed[pg.K_a]:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pg.K_d]:
        yellow.x += VEL
    if keys_pressed[pg.K_w]:
        yellow.y -= VEL
    if keys_pressed[pg.K_s]:
        yellow.y += VEL
    if keys_pressed[pg.K_LSHIFT] and keys_pressed[pg.K_a]:
        yellow.x -= BOOST_VEL
    if keys_pressed[pg.K_LSHIFT] and keys_pressed[pg.K_d]:
        yellow.x += BOOST_VEL
    if keys_pressed[pg.K_LSHIFT] and keys_pressed[pg.K_s]:
        yellow.y += BOOST_VEL
    if keys_pressed[pg.K_LSHIFT] and keys_pressed[pg.K_w]:
        yellow.y -= BOOST_VEL


def projectile_movement(keys_pressed, bullet):
    global BULLET
    if keys_pressed[pg.K_RIGHT]:
        bullet.x += PROJECTILE_SPEED
    if keys_pressed[pg.K_LEFT]:
        bullet.x -= PROJECTILE_SPEED
    if keys_pressed[pg.K_UP]:
        bullet.y -= PROJECTILE_SPEED
    if keys_pressed[pg.K_DOWN]:
        bullet.y += PROJECTILE_SPEED


def main():
    yellow = pg.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    bullet = pg.Rect(100, 350, BULLET_WIDTH, BULLET_HEIGHT)

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys_pressed = pg.key.get_pressed()
        spaceship_movement(keys_pressed, yellow)
        projectile_movement(keys_pressed, bullet)
        draw_window(yellow, bullet)

    pg.quit()


if __name__ == "__main__":
    main()
