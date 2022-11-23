import pygame as pg
import os

pg.display.set_caption("First Game")
WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (255, 255, 255)

FPS = 60
VEL = 10
BOOST_VEL = 15

PROJECTILE_SPEED = 15

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BULLET_WIDTH, BULLET_HEIGHT = 45, 30


YELLOW_SPACESHIP_IMAGE = pg.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pg.transform.rotate(pg.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

BULLET_IMAGE = pg.image.load(os.path.join('Assets', 'bullet.png'))
BULLET = pg.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))


def draw_window(yellow, bullet):
    WIN.fill(BACKGROUND)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(BULLET, (bullet.x, bullet.y))
    pg.display.update()


def yellow_handle_movement(keys_pressed, yellow):
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
    if keys_pressed[pg.K_SPACE]:
        bullet.x += PROJECTILE_SPEED


def main():
    yellow = pg.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    bullet = pg.Rect(100, 350, BULLET_WIDTH, BULLET_HEIGHT)

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys_pressed = pg.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        projectile_movement(keys_pressed, bullet)
        draw_window(yellow, bullet)

    pg.quit()


if __name__ == "__main__":
    main()
