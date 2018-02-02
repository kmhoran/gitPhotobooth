#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install
from lib import post_install

class install_photobooth(install):
      def run(self):
            post_install.run_post_install()
            install.run(self)

setup(name='gitPhotobooth',
      version='0.1',
      description='Git Hook to capture that beautiful smile on each commit.',
      author='Kevin Horan',
      author_email='kevin.michael.horan@gmail.com',
      license="MIT",
      url='https://github.com/kmhoran',
      packages=['lib', 'lib/photobooth'],
      cmdclass={
            'install': install_photobooth
      }
     )