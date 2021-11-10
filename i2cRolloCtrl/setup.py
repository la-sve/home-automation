from setuptools import setup

setup(name='I2C Rollo Controller',
   version='0.1',
   author='Sven Lange',
   packages=['rolloctl'],
   install_requires=[
        'flask',
        'smbus',
    ])