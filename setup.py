#!/usr/bin/env python

from distutils.core import setup

setup(name='Cherimoya',
      version='0.1',
      description='AARTFAAC log to graphite log translator',
      author='Gijs Molenaar',
      author_email='gijs@pythonic.nl',
      url='https://github.com/gijzelaerr/cherimoya',
      packages=['cherimoya'],
      scripts=['cherimoya/bin/aartfaac-translator']
     )