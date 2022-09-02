from setuptools import setup

setup(
    name='SDF Sampler',
    version='0.1',
    description='Generates 2D/3D SDF samples based on the paper "Primitive3D: 3D Object Dataset Synthesis from Randomly Assembled Primitives"',
    author='Ezequiel Bidart',
    author_email='ezequiel.bidart@gmail.com',
    packages=['sdf_sampler'],
    install_requires=[
        'sdf',
        'binarytree',
        'numpy',
        'matplotlib',
        'imageio',
        'ffmpeg',
        'imageio-ffmpeg'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
