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
HEIGHT = 800

plant = Actor("plant")
zombie = Actor("traffic-cone-zombie_0")

p_bullets = []
z_bullets = []


def control_zombie():
    """Keyboard control for zombie"""
    if keyboard.w:
        zombie.y -= 15
    if keyboard.s:
        zombie.y += 15
    if keyboard.a:
        zombie.x -= 15
    if keyboard.d:
        zombie.x += 15
    
def control_plant():
    """Keyboard control for plant"""
    if keyboard.up:
        plant.y -= 15
    if keyboard.down:
        plant.y += 15
    if keyboard.left:
        plant.x -= 15
    if keyboard.right:
        plant.x += 15
    

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


def on_key_down():
    if keyboard.rshift:
        bullet = Actor('tomato_1')
        p_bullets.append(bullet)
        bullet.pos = plant.pos
    if keyboard.space:
        bullet = Actor('target')
        z_bullets.append(bullet)
        bullet.pos = zombie.pos


def update():
    """Draw the game 60 times every second"""
    control_plant()
    control_zombie()
    boundary_check()

    for bullet in p_bullets:
        bullet.x += 10
    for bullet in z_bullets:
        bullet.x += 10


def draw():
    screen.fill((128, 255, 128))
    plant.draw()
    zombie.draw()
    for bullet in p_bullets:
        bullet.draw()
        
    for bullet in z_bullets:
        bullet.draw()
       
    


pgzrun.go()  # do not delete this line and the one above
