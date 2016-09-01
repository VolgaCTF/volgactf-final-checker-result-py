# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'themis', 'finals', 'checker', 'result', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='themis.finals.checker.result',
    version=about['__version__'],
    description='Themis Finals checker result constants',
    author='Alexander Pyatkin',
    author_email='aspyatkin@gmail.com',
    url='https://github.com/aspyatkin/themis-finals-checker-result-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools>=0.8',
        'enum34>=1.1.6'
    ],
    namespace_packages=[
        'themis',
        'themis.finals',
        'themis.finals.checker'
    ]
)
