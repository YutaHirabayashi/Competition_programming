"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='algorhms',
    version='0.1.0',
    license='proprietary',
    description='algorishms for competition programming',

    author='Yuta Hirabayashi',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['collections-extended'],
)
