#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs, os
from setuptools import setup


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

def get_packages(package):
    return [
        dirpath for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, '__init__.py'))
    ]

def _strip_comments(l):
    return l.split('#', 1)[0].strip()

def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]

def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            _strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]

def reqs(*f):
    return [req for subreq in _reqs(*f) for req in subreq]
    
def install_requires():
    return reqs('requirements.txt')

package = 'opm_saltstack'
    
setup(
    name='opm_saltstack',
    version='0.1.0',
    author='Leon',
    author_email='leon.limiao@gmail.com',
    description='Plug and play continuous integration with Django REST framework and SaltStack',
    platforms=['Any'],
    url='https://github.com/leonlm/opm_saltstack',
    install_requires=install_requires(),
    packages=get_packages(package),
    zip_safe=False,
    include_package_data=True
)
