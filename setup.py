#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-facebook-reviews",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_facebook_reviews"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-facebook-reviews=tap_facebook_reviews:main
    """,
    packages=["tap_facebook_reviews"],
    package_data = {
        "schemas": ["tap_facebook_reviews/schemas/*.json"]
    },
    include_package_data=True,
)
