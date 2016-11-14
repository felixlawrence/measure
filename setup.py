#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pandas>=0.17.1'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='measure',
    version='0.1.0',
    description="Simple command line tool to collect a time series, one data point at a time.",
    long_description=readme + '\n\n' + history,
    author="Felix Lawrence",
    author_email='felix.lawrence@gmx.com',
    url='https://github.com/felixlawrence/measure',
    packages=[
        'measure',
    ],
    package_dir={'measure':
                 'measure'},
    entry_points={
        'console_scripts': [
            'measure=measure.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='measure',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
