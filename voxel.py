from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = 'assets/texture/cobblestone.png'):
        super().__init__(
        parent = scene,
        position = position,
        model = 'cube',
        origin_y = 1,
        texture = texture,
        color = color.color(0,0,random.uniform(1,1)),
        scale = 1)




    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal, texture = 'assets/texture/brick.png')

            if key == 'left mouse down':
                destroy(self)








app = Ursina()
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
app.run()
