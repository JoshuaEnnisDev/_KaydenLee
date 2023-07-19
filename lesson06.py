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

# Plant attributes
plant = Actor("plant")
p_bullets = []
p_bullets_directions = []
plant_last_direction = None

# Zombie attributes
zombie = Actor("traffic-cone-zombie_0")
z_bullets = []
z_bullets_directions = []
zombie_last_direction = None

def control_zombie():
    """Keyboard control for zombie"""
    if keyboard.w:
        zombie.y -= 15
        return 'up'
    if keyboard.s:
        zombie.y += 15
        return 'down'
    if keyboard.a:
        zombie.x -= 15
        return 'left'
    if keyboard.d:
        zombie.x += 15
        return 'right'
    
def control_plant():
    """Keyboard control for plant"""
    if keyboard.up:
        plant.y -= 15
        return 'up'
    if keyboard.down:
        plant.y += 15
        return 'down'
    if keyboard.left:
        plant.x -= 15
        return 'left'
    if keyboard.right:
        plant.x += 15
        return 'right'
    

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
    """Shoot bullets"""
    global plant_last_direction, zombie_last_direction

    if keyboard.rshift:
        bullet = Actor('tomato_1')
        p_bullets.append(bullet)
        p_bullets_directions.append(plant_last_direction)
        bullet.pos = plant.pos

    if keyboard.space:
        bullet = Actor('target')
        z_bullets.append(bullet)
        z_bullets_directions.append(zombie_last_direction)
        bullet.pos = zombie.pos


def update():
    """Draw the game 60 times every second"""
    global plant_last_direction, zombie_last_direction
    plant_last_direction = control_plant()
    zombie_last_direction = control_zombie()
    boundary_check()

    # Move the bullets
    for bullet, direction in zip(p_bullets, p_bullets_directions):
        if direction == 'up':
            bullet.y -= 25
        elif direction == 'down':
            bullet.y += 25
        elif direction == 'left':
            bullet.x -= 25
        elif direction == 'right':   
            bullet.x += 25
        else:
            bullet.x += 25

    
       
    for bullet, direction in zip(z_bullets, z_bullets_directions):
        if direction == 'up':
            bullet.x -= 25
        elif direction == 'down':
            bullet.y += 25
        elif direction == 'left':
            bullet.x -= 25
        elif direction == 'right':
            bullet.x += 25
        else:
            bullet.x += 25

        
        

def draw():
    screen.fill((128, 255, 128))
    plant.draw()
    zombie.draw()
    for bullet in p_bullets:
        bullet.draw()
        
    for bullet in z_bullets:
        bullet.draw()
       
    


pgzrun.go()  # do not delete this line and the one above
