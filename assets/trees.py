from ursina import *
from numpy import floor
from perlin_noise import PerlinNoise
from ursina.prefabs.first_person_controller import FirstPersonController

import random

logTex = 'assets/texture/logs.png'
leavesTex = 'assets/texture/frame.png'
block = 'assets/models/block.obj'

class Trees:
    def __init__(this):
        this.noise = PerlinNoise(seed=4)

    def checkTree(this, _x,_y,_z):
        freq = 2
        amp = 100
        treeChance = ((this.noise([_x/freq,_z/freq]))*amp)
        if treeChance > 20:
            this.plantTree(_x,_y,_z)

    def plantTree(this,_x,_y,_z):
        tree = Entity(  model = None,
                        position=Vec3(_x,(_y + 10),_z))
        global trunk
        trunk = Entity(model=block,texture=logTex,scale_y = 8,collider='mesh')
        crown = Entity(model=block,scale=8,y=trunk.y+trunk.scale_y,texture=leavesTex)
        crown.parent=tree
        trunk.parent=tree
        tree.y = 3