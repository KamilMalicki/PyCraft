from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
import os 

app = Ursina()

player = FirstPersonController()
player.y = 0.5  
player.jump_height = 1  
player.position = (10, 3, 10)  
Sky()

obecny_block = 'grass.png'

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j, 0, i),
                     texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def generate_map():
    for kamien in range(6):
        for i in range(20):
            for j in range(20):
                if random.choice([True, False]):
                    box = Button(color=color.white, model='cube', position=(j, -1 - kamien, i),
                                 texture='stone.png', parent=scene, origin_y=0.5)
                    boxes.append(box)

def save_map():
    with open('saved_map.txt', 'w') as file:
        for box in boxes:
            file.write(f"{box.position.x} {box.position.y} {box.position.z} {box.texture}\n")

def load_map():
    if os.path.exists('saved_map.txt'):
        with open('saved_map.txt', 'r') as file:
            for line in file:
                x, y, z, texture = line.strip().split()
                box = Button(color=color.white, model='cube', position=(float(x), float(y), float(z)),
                             texture=texture, parent=scene, origin_y=0.5)
                boxes.append(box)
    else:
        generate_map()

load_map()
def input(key):
    global obecny_block 

    for box in boxes:
        if key == 'escape':
            save_map()
            application.quit()
        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                             texture=obecny_block, parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)
                
            if key == '1':
                obecny_block = 'grass.png'
            if key == '2':
                obecny_block = 'stone.png'
            if key == '3':
                obecny_block = 'brick'

app.run()
