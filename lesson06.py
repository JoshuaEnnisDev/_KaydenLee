"""
id:            Kayden Lee (mr.kayden.lee@gmail.com)
last_update:   2023-Jul-05 18:08:19
type:          lib
sensitivity:   kiddos@family.net
platform:      any
description:   My first Zombie game

TODO - Homework 2023-07-05
==========================
    - [x] bound horizontally
    - [x] add a zombie actor
    - [x] add control keys WASD
"""
import pgzrun  # do not delete this line
from datetime import datetime, timedelta
import random

WIDTH = 800
HEIGHT = 600
justshotbullet = None

# ai plants
sd = Actor("plant_shoot_0")
s_bullets = []
s_bullets_directions = []
sd_last_direction = None
sd_speed = 15


# Plant attributes
plant = Actor("plant")
p_bullets = []
p_bullets_directions = []
plant_last_direction = None
plant_speed = 15

# Zombie attributes
zombie = Actor("traffic-cone-zombie_0")
z_bullets = []
z_bullets_directions = []
zombie_last_direction = None
zombie_speed = 15


def control_zombie():
    """Keyboard control for zombie"""
    global zombie_last_direction
    if keyboard.w:
        zombie.y -= zombie_speed
        zombie_last_direction = "up"
    if keyboard.s:
        zombie.y += zombie_speed
        zombie_last_direction = "down"
    if keyboard.a:
        zombie.x -= zombie_speed
        zombie_last_direction = "left"
    if keyboard.d:
        zombie.x += zombie_speed
        zombie_last_direction = "right"


def control_plant():
    """Keyboard control for plant"""
    global plant_last_direction
    if keyboard.up:
        plant.y -= plant_speed
        plant_last_direction = "up"
    if keyboard.down:
        plant.y += plant_speed
        plant_last_direction = "down"
    if keyboard.left:
        plant.x -= plant_speed
        plant_last_direction = "left"
    if keyboard.right:
        plant.x += plant_speed
        plant_last_direction = "right"


def boundary_check():
    """Ensure no actors go out of bounds"""
    for actor in [zombie, plant]:
        # Boundaries vertically
        if actor.y < 50:
            actor.y = 50
        if actor.y > HEIGHT - 50:
            actor.y = HEIGHT - 50

        # Boundaries horizontally
        if actor.x < 50:  # left
            actor.x = 50
        if actor.x > WIDTH - 50:  # right
            actor.x = WIDTH - 50


def move_bullets(bullet_list, direction_list):
    for bullet, direction in zip(bullet_list, direction_list):
        if direction == "up":
            bullet.y -= 25
        elif direction == "down":
            bullet.y += 25
        elif direction == "left":
            bullet.x -= 25
        elif direction == "right":
            bullet.x += 25
        else:
            bullet.x += 25


def check_collision(bullet_list, actor):
    for bullet in bullet_list:
        if bullet.colliderect(actor):
            bullet_list.remove(bullet)
            print("lah lah lah")


# functions automatically called by pygame zero
def on_key_down():
    """Shoot bullets"""
    global plant_last_direction, zombie_last_direction
    global justshotbullet

    if keyboard.rshift:
        bullet = Actor("blue_bullet")
        p_bullets.append(bullet)
        p_bullets_directions.append(plant_last_direction)
        bullet.pos = plant.pos

    if keyboard.space:
        bullet = Actor("red_bullet")
        z_bullets.append(bullet)
        z_bullets_directions.append(zombie_last_direction)
        bullet.pos = zombie.pos


def update():
    """Draw the game 60 times every second"""
    control_plant()
    control_zombie()
    boundary_check()

    global justshotbullet
    if random.randint(0, 180) < 3:
        bullet = Actor("yellow_bullet")
        s_bullets.append(bullet)
        s_bullets_directions.append(sd_last_direction)
        bullet.pos = sd.pos
        justshotbullet = datetime.now()

    if justshotbullet is not None:
        if datetime.now() - justshotbullet <= timedelta(seconds=0.3):
            sd.image = "plant_shoot_1"
        else:
            sd.image = "plant_shoot_0"

    move_bullets(p_bullets, p_bullets_directions)
    move_bullets(z_bullets, z_bullets_directions)
    move_bullets(s_bullets, s_bullets_directions)

    check_collision(p_bullets, zombie)
    check_collision(z_bullets, plant)
    # AI check
    check_collision(s_bullets, plant)
    check_collision(s_bullets, zombie)


def draw():
    screen.blit("graveyard3", (0, 0))
    plant.draw()
    zombie.draw()
    sd.draw()
    for bullet in p_bullets:
        bullet.draw()

    for bullet in z_bullets:
        bullet.draw()

    for bullet in s_bullets:
        bullet.draw()


pgzrun.go()  # do not delete this line and the one above
