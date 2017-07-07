#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from freedscovery_s3_connector._version import __version__

setup(name='freedscovery_s3_connector',
      version=__version__,
      description='',
      author='FreeDiscovery Developpers',
      packages=find_packages(),
      include_package_data=True)
