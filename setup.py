import os
import setuptools
import RushHour4

setuptools.setup(
    name = 'RushHour4',
    version = RushHour4.__version__,
    author = RushHour4.__author__,
    author_email = 'sethkritik@gmail.com',
    description = 'Reinforcement Learning Tools',
    py_modules = [''],
    long_description_content_type = 'text/markdown',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning'
    ],
    packages = setuptools.find_namespace_packages(include=['RushHour4', 'RushHour4.*']),
    install_requires = [
        'contourpy==1.0.7',
        'cycler==0.11.0',
        'fonttools==4.39.3',
        'kiwisolver==1.4.4',
        'matplotlib==3.7.1',
        'numpy==1.24.3',
        'opencv-python==4.7.0.72',
        'pandas==2.0.1',
        'Pillow==9.5.0',
        'pygame==2.3.0',
        'pyparsing==3.0.9',
        'pytz==2023.3',
        'tqdm==4.65.0',
        'tzdata==2023.3'
      ],
    python_requires='>=3.6'
)