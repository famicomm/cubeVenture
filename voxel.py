from ursina import *
from numpy import floor
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController
import random
app = Ursina()

camera.aspect_ratio = 1.778

#Load Textures
grass_block = load_texture('assets/texture/grass.png')
block = "assets/models/block.obj"
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
    genTerrain()
    pass


# World
randomseed = random.randint(100000000,2147483647)

terrain = Entity(model=None,collider=None)
chunk = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=2,seed=randomseed)
amp = random.randint(2,25)
freq = 69
print("seed: ", randomseed)
guy = FirstPersonController()

shells = []
shellWidth = 15
for i in range(shellWidth * shellWidth):
    ent = Entity(model=block, texture = grass_block, collider="box")

    shells.append(ent)

def genTerrain():
    for i in range(len(shells)):
        x = shells[i].x = floor((i/shellWidth) + guy.x - 0.5*shellWidth)
        z = shells[i].z = floor((i%shellWidth) + guy.z - 0.5*shellWidth)
        y = shells[i].y = floor((noise([x/freq,z/freq]))*amp)


# End World

#Config
window.title = "CubeVenture"
window.color = color.rgb(0,200,211)
window.exit_button.visible = False
application.development_mode = False
window.borderless = False
window.show_ursina_splash = True
window.vsync = True

app.run()
#End Config
