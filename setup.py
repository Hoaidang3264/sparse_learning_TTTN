import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sparse_learning",
    version = "0.2.4",
    author = "Tim Dettmers",
    author_email = "dettmers@cs.washington.edu",
    description = ("Sparse learning library including sparse momentum algorithm."),
    license = "GNU",
    keywords = "deep learning, sparse learning",
    url = "https://github.com/TimDettmers/sparse_learning",
    packages=['sparse_learning'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
    ],

)

