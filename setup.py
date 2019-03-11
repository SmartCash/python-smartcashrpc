#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-smartcashrpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with smartcash',
    long_description=open('README.rst').read(),
    author='Leandro Reinaux',
    author_email='<leoreinaux@gmail.com>',
    maintainer='Leandro Reinaux',
    maintainer_email='<leoreinaux@gmail.com>',
    url='http://www.github.com/leoreinaux/python-smartcashrpc',
    packages=['smartcashrpc','jsonrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
