from ursina import *
from numpy import floor
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader
from assets.trees import Trees
import traceback
import logging
import random
app = Ursina()
life = Trees()
camera.aspect_ratio = 1.778
guy = FirstPersonController()
#Load Textures
grass_block = load_texture('assets/texture/grass.png')
block = "assets/models/block.obj"
glass_block = load_texture('assets/texture/glass.png')
cobble_block = load_texture('assets/texture/cobblestone.png')
brick_block = load_texture('assets/texture/bricks.png')
log_block = load_texture('assets/texture/logs.png')

#End Load Textures

# Build Frame
buildFrameTex = 'assets/texture/frame.png'
buildFrame = Entity(model = block, texture = grass_block)
buildFrame.color = color.rgba(255, 255, 255, 128)

#Audio
music = Audio('assets/audio/calm1.ogg',loop = True, autoplay = True)
#End Audio

#Fog
scene.fog_color = color.rgba(255,255,255, 0)
scene.fog_density = 0.05
#End Fog

blocksPlaced = []
def input(key):
    if key == 'escape':
        quit()
    if key == 'right mouse up':
        try:
            e = duplicate(buildFrame)
            e.collider = 'mesh'
            e.color = color.rgba(255, 255, 255, 255)
            e.shader = basic_lighting_shader
            blocksPlaced.append(e)

            print("Placed a block")
        except Exception as e:
            print("Couldn't place the block.")
        
    if key == 'left mouse down':
        try:
            e = mouse.hovered_entity
            e.y -= 200
            e.visibility = False
            print("Destroyed a block.")
        except Exception as e:
            print("No blocks found. \n Maybe you're pointing at the sky or a non-rendered point.")

        
        
    # Materials
        
    if key == '1':
        buildFrame.texture = grass_block
        # buildFrame.model = block
        
    if key == '2':
        buildFrame.texture = cobble_block
        # buildFrame.model = block
        
    if key == '3':
        buildFrame.texture = brick_block
        # buildFrame.model = block
        
    if key == '4':
        buildFrame.texture = log_block
        # buildFrame.model = block
        

def genTrees(_x, _z, plantTree=False):
    y = shellsCobble[i].y
    freq = 32
    amp = 21
    y += ((noise([_x/freq,_z/freq]))*amp)
    if plantTree==True:
        life.checkTree(_x,y,_z)




def update():
    genTrees(random.randrange(-100, 100), random.randrange(-100, 100))
    genTerrain()
    buildFrame.position = floor(guy.position + camera.forward * 4)
    buildFrame.y = buildFrame.y + 2
    pass


# World
randomseed = random.randint(100000000,2147483647)

terrain = Entity(model=None,collider=None)
chunk = Entity(model=None,collider=None)
noise = PerlinNoise(octaves=5,seed=randomseed)
amp = random.randint(2,25)
freq = 100
print("seed: ", randomseed)


shells = []
shellsCobble = []
shellWidth = 15
for i in range(shellWidth * shellWidth):
    grass = Entity(model=block, texture = grass_block, collider="box", shader=basic_lighting_shader)
    stone = Entity(model=block, texture = cobble_block, collider="box", shader=basic_lighting_shader)
    shells.append(grass)
    shellsCobble.append(stone)
    
def genTerrain():
    for i in range(len(shells)):
        x = shells[i].x = floor((i/shellWidth) + guy.x - 0.5*shellWidth)
        z = shells[i].z = floor((i%shellWidth) + guy.z - 0.5*shellWidth)
        y = shells[i].y = floor((noise([x/freq,z/freq]))*amp)
        
    for i in range(len(shells)):
        x = shellsCobble[i].x = floor((i/shellWidth) + guy.x - 0.5*shellWidth)
        z = shellsCobble[i].z = floor((i%shellWidth) + guy.z - 0.5*shellWidth)
        y = shellsCobble[i].y = floor((noise([x/freq,z/freq]))*amp) -1
        


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
#End Confi