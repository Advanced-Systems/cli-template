#!/usr/bin/env python3

import sys

from setuptools import setup

from src.__init__ import __version__, package_name, python_major, python_minor

if package_name == 'cli-template':
    print("\033[93mWARNING: You should rename the default package name.\033[0m")

try:
    assert (sys.version_info.major == python_major and sys.version_info.minor <= python_minor)
except AssertionError:
    raise RuntimeError("\033[91mPython Version %d.%d+ is required!\033[0m" % (python_major, python_minor))

print("reading dependency file")

with open("requirements/release.txt", encoding='utf-8') as file_handler:
    packages = file_handler.read().splitlines()

print("intitializing %s's setup routine" % package_name)

setup(
    name=package_name,
    version=__version__,
    python_requires=">=%d.%d" % (python_major, python_minor),
    install_requires=packages,
    include_package_data=True,
    entry_points='''
        [console_scripts]
        %s=src.__main__:cli
    ''' % package_name,
)

wheel_name = package_name.replace('-', '_') if '-' in package_name else package_name
print("\033[92mSetup is complete. Run 'python -m pip install dist/%s-%s-py%d-none-any.whl' to install this wheel.\033[0m" % (wheel_name, __version__, python_major))
