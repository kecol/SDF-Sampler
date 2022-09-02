import sys
import os
import numpy as np
import random

# We use the class Node from the library binarytree because it has pretty print
# and display solutions but this should easily work with a simple class Node like:
#
# class Node:
#    def __init__(self, value, left=None, right=None)
#        self.value = value
#        self.left = left
#        self.right = right

from binarytree import Node
# it also has postorder algorithm so let's use it
from binarytree import build # build2, tree

class SDF_2DSample:
    def __init__(self, root=None, sdfs_list=[]):
        """
        params:
        - root: class Node
          root node from resulting from a sampled tree
        - sdfs_list: list
          list of dictionaries containing all sdf shapes that belong to sampled tree
        """
        assert len(sdfs_list) > 0

        self.root = root

        self.left = self.root.left
        self.right = self.root.right

        self.sdfs_list = sdfs_list

    def __call__(self, node=None):
        return self.sdf(node)
    
    def sdf(self, node=None):
        if node is None: node = self.root
        idx = name2idx(node.value)
        return self.sdfs_list[idx]['sdf']
    
    
# ------------------------------------
# Inner sampler for pseudo algorithm 1
# ------------------------------------
    
def sample_primitive(primitives, transforms, sdfs_list):

    # sample primitive
    # triangle, box, circle
    choice = np.random.choice(list(primitives.keys()))
    idx = len(sdfs_list)
    f = primitives[choice]['creator']
    
    # sample shape parameters
    params = primitives[choice]['parameters']()
    if params is not None:
        shape = f(**params)
    else:
        shape = f()
    
    # transform_operations: rotation, translation, scaling    
    shape = transforms(shape)
    
    # create and save the sdf primitive instance
    uid = f'{choice}_{idx}'
    sample = {'idx': idx, 'uid': uid, 'name': choice, 'sdf': shape}
    sdfs_list.append(sample)
    # and return a reference to it
    return uid

def name2idx(name): return int(name.split('_')[-1])
def uid2idx(uid): return int(uid.split('_')[-1])

def sample_operation(operations, s1, s2, sdfs_list):

    op = np.random.choice(list(operations.keys()))
    idx = len(sdfs_list)

    s1_idx = uid2idx(s1)
    s2_idx = uid2idx(s2)
    
    s1 = sdfs_list[s1_idx]
    s2 = sdfs_list[s2_idx]
    
    op_name = operations[op]['name']
    op_func = operations[op]['func']
    s = op_func(s1['sdf'], s2['sdf'])

    s1_name = ''.join(s1['name'].split('_')[:-1]) if '_' in s1['name'] else s1['name']
    s2_name = ''.join(s2['name'].split('_')[:-1]) if '_' in s2['name'] else s2['name']
    name = f"{op}({s1_name},{s2_name})_{idx}"

    uid = f"{op}({s1_idx},{s2_idx})_{idx}"
    sample = {'idx': idx, 'uid': uid, 'name': name, 'sdf': s}
    sdfs_list.append(sample)
    
    return name

# Knuth for easier Remy's algorithm implementation
def knuth_links(N):
    links = [-1 for _ in range(2*N+1)]
    for k in range(1, 2*N, 2):
        x = random.randint(0, k)
        if random.random() < .5:
            links[k] = k+1
            links[k+1] = links[x]
        else:
            links[k] = links[x]
            links[k+1] = k+1
        links[x] = k
    return links

# create a binary tree from knuth links while sampling
# primitives and operations required by algorithm 1
def build_tree_from_knuth(links, primitives, operations, transforms):

    sdfs_list=[]
    
    N = (len(links)-1) // 2
    nodes = [None for _ in range(len(links))]
    
    # this is for Ei in leaves ...
    for k in range(0, len(links), 2):
        nodes[k] = Node(sample_primitive(primitives, transforms, sdfs_list))
    
    for k in range(1, len(links), 2):
        # internals
        nodes[k] = Node(1)
    
    root = nodes[links[0]]
    
    for k in range(1, len(links)-1, 2):
        nodes[k].left = nodes[links[k]]
        nodes[k].right = nodes[links[k+1]]
    
    # this is for Ij in internal nodes 
    t = build(root.values)
    for node in t.postorder:
        if node.value == 1: ## is internal node
            # internal
            if node.left is not None:
                if node.right is not None:
                    node.value = sample_operation(operations, node.left.value, node.right.value, sdfs_list)
                else:
                    node.value = node.left.value
            elif n.left is not None:
                node.value = node.right.value
            else:
                raise Exception('internal without children :S')
                    
    return SDF_2DSample(root=t, sdfs_list=sdfs_list)


# main required class to do SDF sampling
class SDF_2DSampler:
    
    def __init__(self, primitives=None, operations=None, transforms=None, N=5):
        """
        params:
        - primities: list
          list of primitives' samplers
        - operations: list
          list of operations that can be used between sdfs
        - N: int
          max number of levels for the binary tree to be created/sampled
        """
        if primitives is None:
            print('primitives not found, so looking for default ones')
            from .primitives import primitives_2d as primitives

        if operations is None:
            print('operations not found, so looking for default ones')
            from .operations import operations_2d as operations

        if transforms is None:
            print('transform not found, so looking for default ones')
            from .transforms import transforms_2d as transforms
            
        self.primitives = primitives
        self.operations = operations
        self.transforms = transforms
        self.N = N
        
    def algorithm_1(self):
        # Replacing Remy's algorithm with Knuth's algorithm
        links = knuth_links(self.N)
        # Knuth's links as a binary tree
        return build_tree_from_knuth(links, self.primitives, self.operations, self.transforms)
    
    def __call__(self):
        return self.algorithm_1()
    
# main required class to do SDF sampling
class SDF_3DSampler:
    
    def __init__(self, primitives=None, operations=None, transforms=None, N=5):
        """
        params:
        - primities: list
          list of primitives' samplers
        - operations: list
          list of operations that can be used between sdfs
        - N: int
          max number of levels for the binary tree to be created/sampled
        """
        if primitives is None:
            print('primitives not found, so looking for default ones')
            from .primitives import primitives_3d as primitives

        if operations is None:
            print('operations not found, so looking for default ones')
            from .operations import operations_3d as operations

        if transforms is None:
            print('transform not found, so looking for default ones')
            from .transforms import transforms_3d as transforms
            
        self.primitives = primitives
        self.operations = operations
        self.transforms = transforms
        self.N = N
        
    def algorithm_1(self):
        # Replacing Remy's algorithm with Knuth's algorithm
        links = knuth_links(self.N)
        # Knuth's links as a binary tree
        return build_tree_from_knuth(links, self.primitives, self.operations, self.transforms)
    
    def __call__(self):
        return self.algorithm_1()

