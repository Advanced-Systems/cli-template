#!/usr/bin/env python3

import re
import sys

from setuptools import find_packages, setup

print("[1/5] Reading meta data . . .")

with open("src/clitemplate/__init__.py", encoding='utf-8') as file_handler:
    lines = file_handler.read()
    version = re.search(r'__version__ = "(.*?)"', lines).group(1)
    package_name = re.search(r'package_name = "(.*?)"', lines).group(1)
    python_major = int(re.search(r'python_major = "(.*?)"', lines).group(1))
    python_minor = int(re.search(r'python_minor = "(.*?)"', lines).group(1))

if package_name == 'clitemplate':
    print("WARNING: You should rename the default package name.")

try:
    assert sys.version_info >= (int(python_major), int(python_minor))
except AssertionError:
    raise RuntimeError("%s requires Python %s.%s+ (You have Python %s)" % (package_name, python_major, python_minor, sys.version))

print("[2/5] reading dependency file . . .")

with open("requirements/release.txt", mode='r', encoding='utf-8') as release_requirements:
    packages = release_requirements.read().splitlines()

with open("requirements/dev.txt", mode='r', encoding='utf-8') as dev_requirements:
    dev_packages = dev_requirements.read().splitlines()

print("[3/5] Reading readme file . . .")

with open("README.md", mode='r', encoding='utf-8') as readme:
    long_description = readme.read()

print("[4/5] Running %s's setup routine . . ." % package_name)

setup(
    author='Stefan Greve',
    author_email="greve.stefan@outlook.jp",
    name=package_name,
    version=version,
    description="A modern CLI template for python scripts.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Advanced-Systems/cli-template",
    project_urls={
        'Documentation': "https://github.com/Advanced-Systems/cli-template/blob/master/README.md",
        'Source Code': "https://github.com/Advanced-Systems/cli-template",
        'Bug Reports': "https://github.com/Advanced-Systems/cli-template/issues",
        'Changelog': "https://github.com/Advanced-Systems/cli-template/blob/master/CHANGELOG.md"
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
    entry_points={
        'console_scripts': ['%s=%s.__main__:cli' % (package_name, package_name)]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    keywords="utils, terminal, application, template",
)

wheel_name = package_name.replace('-', '_') if '-' in package_name else package_name
print("[5/5] Setup is complete. Run 'python -m pip install dist/%s-%s-py%d-none-any.whl' to install this wheel." % (wheel_name, version, python_major))
