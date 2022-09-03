# %load ../../SDF-Sampler/sdf_sampler/primitives.py
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
    radius = max(.1, np.random.rand()*.75)
    center = np.random.rand(3) - .5
    return {'radius': radius, 'center': center}

def box_parameters():
    # size=1, center=ORIGIN, a=None, b=None    
    size = np.maximum(np.ones(3)*.1, np.random.rand(3)*.75)
    center = np.random.rand(3) - .5
    return {'size': size, 'center': center, 'a': None, 'b': None}

def wireframe_box_parameters():
    size = np.maximum(np.ones(3)*.1, np.random.rand(3)*.8)
    thickness = 0.0001 + np.random.rand()*0.05
    return {'size': size, 'thickness': thickness}

def cylinder_parameters():
    radius = 0.01 + np.random.rand()*.2
    return {'radius': radius}
   
def torus_parameters_0():
    # fat torus
    r1 = max(.1, np.random.rand()*.5)
    r2 = r1 + 0.02 + np.random.rand()*.2
    return {'r1': r1, 'r2': r2}

def torus_parameters():
    r1 = 0.1 + np.random.rand()*.8
    r2 = np.random.rand()*.5
    return {'r1': r1, 'r2': r2}

def capped_cylinder_parameters():
    a = (np.random.rand(3)-.5)*1.5
    b = (np.random.rand(3)-.5)*1.5
    radius = 0.01 + np.random.rand()*.2
    return {'a': a, 'b': b, 'radius': radius}

def capped_cone_parameters():
    a = (np.random.rand(3)-.5)
    b = (np.random.rand(3)-.5)
    ra = np.random.rand()*.02
    rb = 0.02 + np.random.rand()*.5
    return {'a': a, 'b': b, 'ra': ra, 'rb': rb}

def ellipsoid_parameters():
    size = np.maximum(np.ones(3)*.15, np.random.rand(3)*.75)
    return {'size': size}

def pyramid_parameters():
    h = 0.2 + np.random.rand()*.8
    return {'h': h}

def r_parameters(): return {'r': 0.1 + np.random.rand()*.9}

def rounded_cylinder_parameters():
    ra = np.random.rand()*.25
    rb = np.random.rand()*.25
    h = 0.4 + np.random.rand()*.6
    return {'ra': ra, 'rb': rb, 'h': h}

primitives_3d = {
    'pl':  {'name': 'plane', 'creator': sdf.plane, 'parameters': none_parameters},
    'sp':  {'name': 'sphere', 'creator': sdf.sphere, 'parameters': sphere_parameters},
    'el':  {'name': 'ellipsoid', 'creator': sdf.ellipsoid, 'parameters': ellipsoid_parameters},
    'bo':  {'name': 'box', 'creator': sdf.box, 'parameters': box_parameters},
    'wbo': {'name': 'wireframe box', 'creator': sdf.wireframe_box, 'parameters': wireframe_box_parameters},
    'cy':  {'name': 'cylinder', 'creator': sdf.cylinder, 'parameters': cylinder_parameters},
    'ccy': {'name': 'capped cylinder', 'creator': sdf.capped_cylinder, 'parameters': capped_cylinder_parameters},
    'rcy': {'name': 'rounded cylinder', 'creator': sdf.rounded_cylinder, 'parameters': rounded_cylinder_parameters},
    'cco': {'name': 'capped cone', 'creator': sdf.capped_cone, 'parameters': capped_cone_parameters},
    'ca':  {'name': 'capsule', 'creator': sdf.capsule, 'parameters': capped_cylinder_parameters},    
    'to':  {'name': 'torus', 'creator': sdf.torus, 'parameters': torus_parameters},
    'py':  {'name': 'pyramid', 'creator': sdf.pyramid, 'parameters': pyramid_parameters},
    'te':  {'name': 'tetrahedron', 'creator': sdf.tetrahedron, 'parameters': r_parameters},
    'oc':  {'name': 'octahedron', 'creator': sdf.octahedron, 'parameters': r_parameters},
    'do':  {'name': 'dodecahedron', 'creator': sdf.dodecahedron, 'parameters': r_parameters},
    'ic':  {'name': 'icosahedron', 'creator': sdf.icosahedron, 'parameters': r_parameters},
    
}