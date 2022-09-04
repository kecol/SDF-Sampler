# SDF-Sampler

Generates 2D and 3D Signed Distance Field samples based on the paper "Primitive3D: 3D Object Dataset Synthesis from Randomly Assembled Primitives". We extend the idea to the SDF world resulting into a simple library that might open/simplify new ML explorations.

## How to install
```
git clone https://github.com/kecol/SDF-Sampler.git
pip install -e .
```

## How to use it


### 2D Sampler

```python
import numpy as np
from sdf_sampler.sampler import SDF_2DSampler

# create sampler with default primitives and operations
tree_depth = 10
sampler = SDF_2DSampler(N=tree_depth)

# generate random sdf sample
sample = sampler()

# display sample composition (sdf primitives and operations used)
print(sample.root)

# define space's coordinates we are courious about in range (-1,-1) to (1, 1)
n_points = 100
points = (np.random.rand(n_points, 2)-.5)*2

# query sdf values for defined points
sdf_values = sample().f(points)
```

[SDF 2D Sampler notebook](SDF_Sampler_2D.ipynb)


### 3D Sampler

```python
import numpy as np
from sdf_sampler.sampler import SDF_3DSampler

# create sampler with default primitives and operations
tree_depth = 6
sampler = SDF_3DSampler(N=tree_depth)

# generate random sdf sample
sample = sampler()

# display sample composition (sdf primitives and operations used)
print(sample.root)

# define space's coordinates we are courious about in range (-1,-1,-1) to (1, 1, 1)
n_points = 100
points = (np.random.rand(n_points, 3)-.5)*2

# query sdf values for defined points
sdf_values = sample().f(points)
```

[SDF 3D Sampler notebook](SDF_Sampler_3D.ipynb)


## TODOs
- ~~Implement rotations, translation and scaling in 2D (sampler.sample_primitive)~~
- Add more primitives (primitives.primitives_2D)
- Add more operations (operations.operations_2D)
- ~~Replicate the whole sampling idea for 3D~~
- ~~Add alternative 3D plots (utils)~~
- ~~Add more primitives (primitives.primitives_3D)~~
- Add more operations (operations.operations_3D)
- Simplify video generation for 3D
- Add animated/video 3D slice exploration
- Add STL plotting
