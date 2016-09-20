#!/usr/bin/env python3

from setuptools import setup


setup(
    name='emojencode',
    version='1.2',
    description='Encode binary data as emoji! 😄',
    author='Frederick "doctaphred" Wagner',
    author_email='yo@doctaph.red',
    url='https://github.com/doctaphred/emojencode',
    py_modules=['emojencode'],
    entry_points={
        'console_scripts': [
            'emojencode = emojencode:main',
        ]
    },
)
