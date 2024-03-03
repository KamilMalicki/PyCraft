from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

obecny_block = 'grass.png'

boxes = []
for i in range(20):
    for j in range(20):
        box = Button(color=color.white, model='cube', position=(j, 0, i),
                     texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

for kamien in range(3):
    for i in range(20):
        for j in range(20):
            box = Button(color=color.white, model='cube', position=(j, -1 - kamien, i),
                         texture='stone.png', parent=scene, origin_y=0.5)
            boxes.append(box)

def input(key):
    global obecny_block 

    for box in boxes:
        if key == 'escape':
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
