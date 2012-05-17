#!/usr/bin/env python

from distutils.core import setup

setup(name='webkit_remote_debugger',
      version='0.1',
      url='https://github.com/jfly/webkit_remote_debugger',
      packages=['webkit_remote_debugger'],

      install_requires=["httplib2>=0.7.4", "ws4py>=0.2.1"]
     )
