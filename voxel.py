from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise
import random
app = Ursina()

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
terrain = Entity(model=None,collider=None)
rock = Entity(model=None,collider=None)
chunk = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=2,seed=random.randint(0,696969))
amp = random.randint(2,25)
freq = 69


terrainWidth = 25
for i in range(terrainWidth*terrainWidth):
    voxel = Entity(model='cube',color=color.green)
    voxel.x = floor(i/terrainWidth)
    voxel.z = floor(i%terrainWidth)
    voxel.y = floor((noise([voxel.x/freq,voxel.z/freq]))*amp)
    voxel.parent = terrain
    voxel2 = Entity(model='cube')
    voxel2.x = floor(i/terrainWidth)
    voxel2.z = floor(i%terrainWidth)
    voxel2.y = (voxel.y - 1)
    voxel2.parent = rock
# End World

# Combine
terrain.combine()
rock.combine()
chunk.combine()
# End Combine


terrain.collider = 'mesh'
terrain.texture = grass_block
rock.texture = cobble_block
steve = FirstPersonController()
steve.cursor.visible = False
steve.x = steve.z = 10
steve.y = 12

#Chunk
rock.parent = chunk
terrain.parent = chunk
#Chunk End

#Config
window.title = 'VoxelTesting'
window.color = color.rgb(0,200,211)
window.exit_button.visible = False
application.development_mode = False
window.borderless = False
window.show_ursina_splash = True
window.vsync = True
app.run()
#End Config
