#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap_facebook",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_facebook"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap_facebook=tap_facebook:main
    """,
    packages=["tap_facebook"],
    package_data = {
        "schemas": ["tap_facebook/schemas/*.json"]
    },
    include_package_data=True,
)
