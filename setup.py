#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='flujconf',
version='0.5',
description='Simple configurator for darkice',
author='Kevin Brown',
author_email='kev@ki-ai.org',
license='GPL v2 or later',
data_files=[('share/man/man1',['flujconf.1']), ('/usr/share/applications',['flujconf.desktop'])],
#packages=['flujconf'],
py_modules = ['lib.shout', 'lib.data','lib.file', 'lib.app', 'lib.interface'],
scripts=['flujconf'],
)
