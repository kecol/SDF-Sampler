import numpy as np
import sdf

def transforms_2d(s):
    # rotate
    theta = np.random.rand() * 2 * np.pi
    s = s.rotate(theta)
    # translate
    pos = (np.random.rand(2) - .5)
    s = s.translate(pos)
    # scale
    scale_factor = np.random.rand(2)*.8 + 0.2
    s = s.scale(scale_factor)    
    return s

def transforms_3d(s):
    # rotate
    theta = np.random.rand() * 2 * np.pi
    vector = [sdf.d3.X, sdf.d3.Y, sdf.d3.Z][np.random.randint(3)]
    s = s.rotate(theta, vector)
    # translate
    pos = (np.random.rand(3) - .5)
    s = s.translate(pos)
    # scale
    scale_factor = np.random.rand(3)*.8 + 0.2
    s = s.scale(scale_factor)    
    return s
