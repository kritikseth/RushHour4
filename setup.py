import os
import setuptools
import RushHour4

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'RushHour4',
    version = varya.__version__,
    author = varya.__author__,
    author_email = 'sethkritik@gmail.com',
    description = 'Reinforcement Learning Tools',
    py_modules = [''],
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = varya.__url__,
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning'
    ],
    packages = setuptools.find_namespace_packages(include=['RushHour4', 'RushHour4.*']),
    install_requires = [
    'pandas',
    'numpy',
    'torch',
    'scikit-learn'
      ],
    python_requires='>=3.6'
)