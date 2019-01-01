#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import sys
from io import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(f):
    return open(f, "r", encoding="utf-8").read()


about = {}
exec(read(os.path.join(here, "kindeditor", "__version__.py")), about)

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    if os.system("which twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(about["__version__"]))
    print("  git push --tags")
    shutil.rmtree("dist")
    shutil.rmtree("build")
    shutil.rmtree("django_kindeditor.egg-info")
    sys.exit()

packages = ["kindeditor"]

requires = ["django>=2.0", "pillow>=5.3"]


readme = read("README.md")

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    packages=packages,
    include_package_data=True,
    install_requires=requires,
    python_requires=">=3.6",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
