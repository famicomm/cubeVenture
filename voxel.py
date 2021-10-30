from ursina import *
from numpy import floor
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController
import random
app = Ursina()

camera.aspect_ratio = 1.778

#Load Textures
grass_block = load_texture('assets/texture/grass.png')
glass_block = load_texture('assets/texture/glass.png')
cobble_block = load_texture('assets/texture/cobblestone.png')
brick_block = load_texture('assets/texture/bricks.png')
#End Load Textures

#Audio
music = Audio('assets/audio/calm1.ogg',loop = True, autoplay = True)
#End Audio

#Fog
scene.fog_color = color.rgb(255,255,255)
scene.fog_density = 0.01
#End Fog


def input(key):
    if key == 'escape':
        quit()

def update():


    pass


# World
randomseed = random.randint(100000000,2147483647)
terrain = Entity(model=None,collider=None)
chunk = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=2,seed=randomseed)
amp = random.randint(2,25)
freq = 69
print("seed: ", randomseed)

terrainWidth = 70
for i in range(terrainWidth*terrainWidth):
    voxel = Entity(model='cube',color=color.green)
    voxel.x = floor(i/terrainWidth)
    voxel.z = floor(i%terrainWidth)
    voxel.y = floor((noise([voxel.x/freq,voxel.z/freq]))*amp)
    voxel.parent = terrain

# End World

# Combine
terrain.combine()
chunk.combine()
# End Combine


terrain.collider = 'mesh'
terrain.texture = grass_block

#Chunk
terrain.parent = chunk
#Chunk End

#Config
window.title = "ripoff minecraft"
window.color = color.rgb(0,200,211)
window.exit_button.visible = False
application.development_mode = False
window.borderless = False
window.show_ursina_splash = True
window.vsync = True
guy = FirstPersonController()
app.run()
#End Config
