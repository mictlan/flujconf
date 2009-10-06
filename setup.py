#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='flujconf',
version='0.4',
description='Simple configurator for darkice',
author='Kevin Brown',
author_email='kev@flujos.org',
license='GPL v2 or later',
data_files=[('share/man/man1',['flujconf.1']), ('/usr/share/applications',['flujconf.desktop'])],
#packages=['flujconf'],
py_modules = ['flujconf.shout', 'flujconf.data','flujconf.file', 'flujconf.app', 'flujconf.interface'],
scripts=['bin/flujconf'],
)
