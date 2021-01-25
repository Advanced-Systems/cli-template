#!/usr/bin/env python3

import sys

from setuptools import setup, find_packages

from src.__init__ import __version__, package_name, python_major, python_minor

if package_name == 'cli-template':
    print("\033[93mWARNING: You should rename the default package name.\033[0m")

try:
    assert (sys.version_info.major == python_major and sys.version_info.minor <= python_minor)
except AssertionError:
    raise RuntimeError("\033[91mPython Version %d.%d+ is required!\033[0m" % (python_major, python_minor))

print("reading dependency file")

with open("requirements/release.txt", mode='r', encoding='utf-8') as requirements:
    packages = requirements.read().splitlines()

with open("requirements/dev.txt", mode='r', encoding='utf-8') as requirements:
    dev_packages = requirements.read().splitlines()

with open("README.md", mode='r', encoding='utf-8') as readme:
    long_description = readme.read()

print("running %s's setup routine" % package_name)

setup(
    author='hentai-chan',
    author_email="dev.hentai-chan@outlook.com",
    name=package_name,
    version=__version__,
    description="A modern CLI template for python scripts.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Advanced-Systems/cli-template",
    project_urls={
        'Source Code': "https://github.com/Advanced-Systems/cli-template",
        'Bug Reports': "https://github.com/Advanced-Systems/cli-template/issues",
    },
    python_requires=">=%d.%d" % (python_major, python_minor),
    install_requires=packages,
    extra_requires={
        'dev': dev_packages[1:],
        'test': ['pytest']
    },
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points='''
        [console_scripts]
        %s=src.__main__:cli
    ''' % package_name,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    keywords="utils, terminal, application, template",
)

wheel_name = package_name.replace('-', '_') if '-' in package_name else package_name
print("\033[92mSetup is complete. Run 'python -m pip install dist/%s-%s-py%d-none-any.whl' to install this wheel.\033[0m" % (wheel_name, __version__, python_major))
