#! /usr/bin/env python
#
# Copyright (C) 2012 Mathieu Blondel

import os

import numpy as np
from setuptools import Extension, find_packages, setup
from Cython.Build import cythonize

DISTNAME = 'sklearn-contrib-lightning'


# Cython modules of the implementations and the pure Python modules they rely
# on live in lightning/impl. Generated C++ files are never shipped: they are
# rebuilt from the .pyx sources for the target Python and NumPy.
IMPL = os.path.join('lightning', 'impl')
RANDOMKIT = os.path.join(IMPL, 'randomkit')

EXTENSION_NAMES = [
    'adagrad_fast',
    'dataset_fast',
    'dual_cd_fast',
    'loss_fast',
    'prank_fast',
    'primal_cd_fast',
    'prox_fast',
    'sag_fast',
    'sdca_fast',
    'sgd_fast',
    'svrg_fast',
]


def extensions():
    exts = [
        Extension(name=f'lightning.impl.{name}',
                  sources=[os.path.join(IMPL, f'{name}.pyx')],
                  language='c++',
                  include_dirs=[RANDOMKIT])
        for name in EXTENSION_NAMES
    ]

    libraries = ['Advapi32'] if os.name == 'nt' else []
    exts.append(
        Extension(name='lightning.impl.randomkit.random_fast',
                  sources=[os.path.join(RANDOMKIT, 'random_fast.pyx'),
                           os.path.join(RANDOMKIT, 'randomkit.c')],
                  language='c++',
                  libraries=libraries,
                  include_dirs=[RANDOMKIT])
    )

    for ext in exts:
        ext.include_dirs.insert(0, np.get_include())

    return exts


setup(
    packages=find_packages(include=['lightning', 'lightning.*']),
    ext_modules=cythonize(extensions(),
                          compiler_directives={'language_level': 3}),
)
