#!/usr/bin/env python
# encoding: utf-8
"""
This file handles Cython extension building for madmom.

All project metadata is defined in pyproject.toml (PEP 621).
This setup.py only handles the compilation of Cython extensions.
"""

import glob

import numpy as np
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import Extension, setup

# numpy include directory for Cython extensions
include_dirs = [np.get_include()]

# Cython extensions to compile
extensions = [
    Extension(
        "madmom.audio.comb_filters",
        ["madmom/audio/comb_filters.pyx"],
        include_dirs=include_dirs,
    ),
    Extension(
        "madmom.features.beats_crf",
        ["madmom/features/beats_crf.pyx"],
        include_dirs=include_dirs,
    ),
    Extension(
        "madmom.ml.hmm",
        ["madmom/ml/hmm.pyx"],
        include_dirs=include_dirs,
    ),
    Extension(
        "madmom.ml.nn.layers",
        ["madmom/ml/nn/layers.py"],
        include_dirs=include_dirs,
    ),
]

# CLI scripts to install
scripts = glob.glob("bin/*")

setup(
    ext_modules=cythonize(extensions, language_level="3"),
    scripts=scripts,
    cmdclass={"build_ext": build_ext},
)
