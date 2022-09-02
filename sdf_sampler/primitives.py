import sdf
import numpy as np

# ---------------------------------------
# primitive instances parameters samplers
# this is used to start with something but
# one should be able to extend it
# ---------------------------------------

# 2D

def circle_parameters():   
    radius = max(.1, np.random.rand()*.75)
    center = (np.random.rand(2) - .5) * 1.5
    return {'radius': radius, 'center': center}

def rectangle_parameters():
    size = np.ones(2)
    for i in range(2):
        size[i] = max(0.1, min(1, np.random.rand()))
    center = (np.random.rand(2) - .5)*1.5
    return {'size': size, 'center': center, 'a': None, 'b': None}

def none_parameters(): return None

def hexagon_parameters():
    return {'r': np.random.rand()*.9 + .1}

def polygon_parameters():
    n = np.random.choice([3, 4, 5, 6])
    points = (np.random.rand(n, 2) - .5) * 1.5
    return {'points': points}

primitives_2d = {
    'l': {'name': 'line', 'creator': sdf.line, 'parameters': none_parameters},
    't': {'name': 'triangle', 'creator': sdf.equilateral_triangle, 'parameters': none_parameters},
    'r': {'name': 'rectangle', 'creator': sdf.rectangle, 'parameters': rectangle_parameters},
    'h': {'name': 'hexagon', 'creator': sdf.hexagon, 'parameters': hexagon_parameters},    
    'p': {'name': 'polygon', 'creator': sdf.polygon, 'parameters': polygon_parameters},
    'c': {'name': 'circle', 'creator': sdf.circle, 'parameters': circle_parameters}
}

# 3D

def sphere_parameters():
    radius = max(.1, np.random.rand())
    center = np.random.rand(3) - .5
    return {'radius': radius, 'center': center}

def box_parameters():
    # size=1, center=ORIGIN, a=None, b=None    
    size = np.maximum(np.ones(3)*.1, np.random.rand(3))
    center = np.random.rand(3) - .5
    return {'size': size, 'center': center, 'a': None, 'b': None}

def wireframe_box_parameters():
    size = np.maximum(np.ones(3)*.1, np.random.rand(3))
    thickness = 0.01 + np.random.rand()*0.05
    return {'size': size, 'thickness': thickness}

def cylinder_parameters():
    radius = max(.1, np.random.rand())
    return {'radius': radius}
    
def torus_parameters():
    r1 = max(.1, np.random.rand()*.5)
    r2 = r1 + 0.02 + np.random.rand()*.2
    return {'r1': r1, 'r2': r2}

primitives_3d = {
    'p':  {'name': 'plane', 'creator': sdf.plane, 'parameters': none_parameters},
    's':  {'name': 'sphere', 'creator': sdf.sphere, 'parameters': sphere_parameters},
    'b':  {'name': 'box', 'creator': sdf.box, 'parameters': box_parameters},
    'wb': {'name': 'wireframe box', 'creator': sdf.wireframe_box, 'parameters': wireframe_box_parameters},
    'c':  {'name': 'cylinder', 'creator': sdf.cylinder, 'parameters': cylinder_parameters},
    't':  {'name': 'torus', 'creator': sdf.torus, 'parameters': torus_parameters}
}