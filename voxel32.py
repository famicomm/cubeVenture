from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread

window.title = 'VoxelTest'
window.borderless = False

block_pick = 1

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    #if held_keys['1']: print("You chose: Grass")
    #if held_keys['2']: print("You chose: Cobblestone")
    #if held_keys['3']: print("You chose: Bricks")
    #if held_keys['4']: print("You chose: Glass block")

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = 'assets/texture/grass.png'):
        super().__init__(

        parent = scene,
        position = position,
        model = 'cube',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(1,1)),
        scale = 1)




    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = 'assets/texture/grass.png')
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = 'assets/texture/cobblestone.png')
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = 'assets/texture/bricks.png')
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = 'assets/texture/glass.png')

            if key == 'left mouse down':
                destroy(self)




class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = 'assets/environment/skyentity.png',
			scale = 150,
			double_sided = True)



app = Ursina()
sky = Sky()
for z in range(32):
    for x in range(32):
        for y in range(2):
            voxel = Voxel(position = (x,y,z))

player = FirstPersonController()
app.run()
