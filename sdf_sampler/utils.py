import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def sample_2D_grid(resolution, low = -1, high = 1):
    idx = np.linspace(low, high, num=resolution)
    x, y = np.meshgrid(idx, idx)
    V = np.concatenate((x.reshape((-1,1)), y.reshape((-1,1))), 1)
    return np.array(V)

def sample_2D_random_grid(grid, resolution):
    random_grid = np.random.rand(*grid.shape)
    random_grid /= resolution*.5
    random_grid += grid
    return random_grid

def plot_sdf(sdf2, resolution=200, grid=None, ax=None, title=None, n_levels=31):
    if grid is None: grid = sample_2D_grid(resolution)
    sdf2_values = sdf2.f(grid)
    sdf_cm = mpl.colors.LinearSegmentedColormap.from_list('SDF', [(0,'#eff3ff'),(0.5,'#3182bd'),(0.5,'#31a354'),(1,'#e5f5e0')], N=256)
    levels = np.linspace(-1.1, 1.1, n_levels)
    if ax is None:
        plt.figure()
        ax = plt.subplot(111)
    ax.axis('equal')
    ax.contourf(sdf2_values.reshape(resolution,resolution), levels = levels, cmap=sdf_cm)
    ax.axis('off')
    if title is not None:
        ax.set_title(title, fontsize=9)
        
def plot_scatter(sdf2, resolution=200, grid=None, eps=0.0, ax=None, title=None):
    if grid is None: grid = sample_2D_grid(resolution)
    sdf_values = sdf2.f(grid)
    if ax is None:
        plt.figure(figsize=(6,6))
        ax = plt.subplot(111)
    ax.scatter(grid[:,0], grid[:,1], s=1, c=sdf_values)
    if eps > 0:
        c = ((sdf_values < eps) & (sdf_values > -eps)).flatten()
        ax.scatter(grid[c,0], grid[c,1], s=5, color='white')
    if title is not None:
        ax.set_title(title, fontsize=9)
    ax.axis('equal')
    ax.axis('off')
    
def plot_scatter_redblue(sdf2, resolution=200, grid=None, ax=None, title=None):
    if grid is None: grid = sample_2D_grid(resolution)
    sdf_values = sdf2.f(grid)
    if ax is None:
        plt.figure(figsize=(6,6))
        ax = plt.subplot(111)
    sdf_values = sdf_values.flatten()
    pos = (sdf_values >= 0)
    neg = (sdf_values < 0)

    size = np.abs(sdf_values*200)
    for marker, cond, cmap in zip(['^','v'], [pos, neg], ['Reds', 'Blues_r']):
        ax.scatter(grid[cond,0], grid[cond,1], s=size[cond], c=sdf_values[cond], cmap=cmap, marker=marker)
    if title is None: title = 'sdf scatter redblue'
    ax.set_title(title)
    ax.axis('equal')
    ax.axis('off')
    
def plot_sdf_values(sdf_values, w=256, h=256, ax=None, title=None, n_levels=31):
    sdf_cm = mpl.colors.LinearSegmentedColormap.from_list('SDF', [(0,'#eff3ff'),(0.5,'#3182bd'),(0.5,'#31a354'),(1,'#e5f5e0')], N=256)
    levels = np.linspace(-1.1, 1.1, n_levels)
    if ax is None:
        plt.figure()
        ax = plt.subplot(111)
    ax.axis('equal')    
    ax.contourf(sdf_values.reshape(w,h), levels = levels, cmap=sdf_cm)
    ax.axis('off')
    if title is not None:
        ax.set_title(title, fontsize=9)
        
def transfer_function(x, rgb_gaussians_loc = (0.1, 0.0, -0.1)):
    
    rc, gc, bc = rgb_gaussians_loc
    r = 1.0*np.exp( -(x - rc)**2/0.01 )   +  0.1*np.exp( -(x - gc)**2/0.01 ) +  0.10*np.exp( -(x - bc)**2/0.01 )
    g = 0.1*np.exp( -(x - rc)**2/0.01 )   +  1.0*np.exp( -(x - gc)**2/0.02 ) +  0.10*np.exp( -(x - bc)**2/0.01 )
    b = 0.1*np.exp( -(x - rc)**2/0.01 )   +  0.1*np.exp( -(x - gc)**2/0.01 ) +  1.00*np.exp( -(x - bc)**2/0.01 )
    a = 0.005*np.exp( -(x - rc)**2/0.01 ) +  0.6*np.exp( -(x - gc)**2/0.01 ) +  0.01*np.exp( -(x - bc)**2/0.01 )

    return r,g,b,a

def volume_rendering(sdf3, N=128, theta=0.0, bound=1.0, transfer_function=transfer_function):
    
    # generate volume grid coordinates
    c = np.linspace(-bound, bound, N)
    qx, qy, qz = np.meshgrid(c,c,c)
    # rotate volume grid coordinates
    qxR = qx
    qyR = qy * np.cos(theta) - qz * np.sin(theta) 
    qzR = qy * np.sin(theta) + qz * np.cos(theta)
    qi = np.array([qxR.ravel(), qyR.ravel(), qzR.ravel()]).T

    # query sdf values for our rotated volume grid coordinates
    camera_grid = sdf3.f(qi).reshape((N,N,N))

    # prepair container for volume rendering
    image = np.zeros((camera_grid.shape[1],camera_grid.shape[2],3))

    # do volume rendering
    for dataslice in camera_grid:
        r,g,b,a = np.array(transfer_function(dataslice))
        
        image[:,:,0] = a*r + (1-a)*image[:,:,0]
        image[:,:,1] = a*g + (1-a)*image[:,:,1]
        image[:,:,2] = a*b + (1-a)*image[:,:,2]
            
    image = np.clip(image,0.0,1.0)
    return image
