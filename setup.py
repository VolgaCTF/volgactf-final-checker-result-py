# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'volgactf', 'final', 'checker', 'result', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='volgactf.final.checker.result',
    version=about['__version__'],
    description='VolgaCTF Final checker result constants',
    author='Alexander Pyatkin',
    author_email='aspyatkin@gmail.com',
    url='https://github.com/VolgaCTF/volgactf-final-checker-result-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools>=35.0.0'
    ],
    extras_require={
        ':python_version<"3.4"': [
            'enum34>=1.1.6'
        ]
    },
    namespace_packages=[
        'volgactf',
        'volgactf.final',
        'volgactf.final.checker'
    ]
)
