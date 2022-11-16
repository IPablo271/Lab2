import math
from gl import *
from Obj import *
from Render import *
from vector import *
from texture import *

r = Render(1024,1024)
background = Texture('space.bmp')
r.framebuffer = background.pixels
r.lookAt(V3(0,0,5), V3(0,0,0), V3(0,1,0))
r.active_shader = r.shader2
r.load_model('Sphere.obj', scale_factorn=(0.0012,0.0012,0.0012),  translate_factor=(0,0,0),rotate=(0,0,0))
r.draw('TRIANGLES')
r.write('Lab2.bmp')