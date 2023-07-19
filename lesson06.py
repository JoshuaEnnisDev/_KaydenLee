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

from pgzero.builtins import Actor, keyboard

WIDTH = 800
HEIGHT = 600

plant = Actor("pc")
zombie = Actor("target")


def control_zombie():
    """Keyboard control for zombie"""
    if keyboard.w:
        zombie.y -= 1
    if keyboard.s:
        zombie.y += 1
    if keyboard.a:
        zombie.x -= 1
    if keyboard.d:
        zombie.x += 1


def control_plant():
    """Keyboard control for plant"""
    if keyboard.up:
        plant.y -= 1
    if keyboard.down:
        plant.y += 1
    if keyboard.left:
        plant.x -= 1
    if keyboard.right:
        plant.x += 1


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


def update():
    """Draw the game 60 times every second"""
    control_plant()
    control_zombie()
    boundary_check()


def draw():
    screen.fill((128, 255, 128))
    plant.draw()
    zombie.draw()


pgzrun.go()  # do not delete this line and the one above
