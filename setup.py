#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
writebits
===================
A Telegram bot
"""
from setuptools import setup, find_packages

install_requires = [
    'bitarray>=0.8.1',
    'ipdb>=0.9.0'
]


setup(
    name="writebits",
    version='0.1.0',
    author='Luiz Oliveira',
    author_email='ziuloliveira@gmail.com',
    url='https://gitlab.com/Ziul/writebits/',
    entry_points={
        'console_scripts': [
            'main-run = main:main',
            # 'main-test = main:test',
        ]},
    description='A program to write bit into memory or file',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    test_suite="tests.run.runtests",
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)
