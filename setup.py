#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='botosh',
    version='0.0.1',
    packages=find_packages(),

    author='Tommi Virtanen',
    author_email='tommi.virtanen@dreamhost.com',
    description='Start a Python shell with Boto connections open',
    license='MIT',
    keywords='s3 programming',

    install_requires=[
        'boto >=2.0b4',
        'argparse >=1.2.1',
        'PyYAML',
        ],

    entry_points={
        'console_scripts': [
            'botosh = botosh:main',
            ],
        },

    )
