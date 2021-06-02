from distutils.core import setup
from Cython.Build import cythonize

setup(
   name='Hello',
   ext_modules = cythonize([ 'cevolve.pyx',
                            'mathlib.pyx', 'distance.pyx']),
)
