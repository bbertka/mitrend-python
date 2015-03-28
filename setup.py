#!/usr/bin/python

from distutils.core import setup
setup(name='mitrend',
      version='1.0.0',
      py_modules=['mitrend'],
      description='A Python implementation of the MiTrend REST API',
      long_description='This is a python module for the MiTrend performance analysis tool that submits assessments on behalf of an authenticated user. It exposes the REST API made publicly available by MiTrend.',
      url = 'https://github.com/bbertka/mitrend-python',
      author='Ben Bertka',
      author_email='bbertka@gmail.com',
      license='APACHE',
      classifiers=[
      	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: Apache Software License',
	'Programming Language :: Python :: 2.7',
      ],
      keywords='mitrend',
      install_requires=['requests'],
      
      )
