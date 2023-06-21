from setuptools import setup, find_packages, Extension
import numpy
from Cython.Build import cythonize

setup(
    name='dtw_flex',
    version='0.1',
    description='',
    url='https://github.com/username/my_package',
    author='Alexander Meire',
    author_email='Alexander.meire@gmail.com',
    license='GPLv3',
    packages=find_packages(),
    ext_modules = cythonize(Extension('dtw_flex.core_cython.dtw_cy',
          ["dtw_flex/core_cython/dtw_cy.pyx"],
          include_dirs=[numpy.get_include()])),
    install_requires=[
        'Cython',
        'matplotlib',
        'numpy',
        'pandas',
        'setuptools'
    ],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
)