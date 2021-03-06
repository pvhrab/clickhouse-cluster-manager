#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="clickhouse-manager",

    # version should comply with PEP440
    version='0.0.201801091',

    description='ClickHouse Manager',
    long_description='ClickHouse Manager',

    # homepage
    url="https://github.com/altinity/clickhouse-cluster-manager",

    author="Vladislav Klimenko",
    author_email="sunsingerus@gmail.com",

    license="MIT",

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Database',

        # should match license above
        'License :: OSI Approved :: MIT License',

        # supported Python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # what does the project relate to?
    keywords='clickhouse manager',

    # list of packages to be included into project
    packages=find_packages(exclude=[
        'contrib',
        'docs',
        'tests',
    ]),

    # list of additional package data to be attached to packages
    package_data={
    },

    # run-time dependencies
    # these will be installed by pip
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'paramiko',
        'lxml',
    ],

    # cross-platform support for pip to create the appropriate form of executable
    entry_points={
        'console_scripts': [
            # executable name=what to call
            'clickhouse-manager=clickhouse_manager:main',
        ],
    },

#    python_requires='>=3.3',
)
