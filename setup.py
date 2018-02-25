#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install

from lib import configure_directories


class install_photobooth(install):
      def run(self):
            configure_directories.run()
            install.run(self)

setup(name='gitPhotobooth',
      version='0.1',
      description='Git Hook to capture that beautiful smile on each commit.',
      author='Kevin Horan',
      author_email='kevin.michael.horan@gmail.com',
      url='https://github.com/kmhoran',
      packages=['lib', 'lib/photos'],
      cmdclass={
            'install': install_photobooth
      },
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          ('License :: OSI Approved :: GNU Library or Lesser '
          'General Public License (LGPL)'),
          'Operating System :: Unix',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
)