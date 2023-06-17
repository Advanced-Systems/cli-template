#!/usr/bin/env python3

import re
import sys

from setuptools import find_packages, setup

print("[1/5] Reading meta data . . .")

with open("src/clitemplate/__init__.py", encoding="utf-8") as file_handler:
    lines = file_handler.read()
    version = re.search(r'__version__ = "(.*?)"', lines).group(1)
    author_name = re.search(r'author_name = "(.*?)"', lines).group(1)
    author_email = re.search(r'author_email = "(.*?)"', lines).group(1)
    package_name = re.search(r'package_name = "(.*?)"', lines).group(1)
    description = re.search(r'description = "(.*?)"', lines).group(1)
    url = re.search(r'url = "(.*?)"', lines).group(1)
    url_documentation = re.search(r'url_documentation = "(.*?)"', lines).group(1)
    url_source_code = re.search(r'url_source_code = "(.*?)"', lines).group(1)
    url_bug_reports = re.search(r'url_bug_reports = "(.*?)"', lines).group(1)
    url_changelog = re.search(r'url_changelog = "(.*?)"', lines).group(1)
    python_major = int(re.search(r'python_major = "(.*?)"', lines).group(1))
    python_minor = int(re.search(r'python_minor = "(.*?)"', lines).group(1))

if package_name == "clitemplate":
    print("WARNING: You should rename the default package name.")

try:
    assert sys.version_info >= (int(python_major), int(python_minor))
except AssertionError:
    raise RuntimeError(f"{package_name} requires Python {python_major}.{python_minor}+ (You have Python {sys.version})")

print("[2/5] reading dependency file . . .")

with open("requirements/release.txt", mode='r', encoding="utf-8") as release_requirements:
    packages = release_requirements.read().splitlines()

with open("requirements/dev.txt", mode='r', encoding="utf-8") as dev_requirements:
    dev_packages = dev_requirements.read().splitlines()

print("[3/5] Reading readme file . . .")

with open("README.md", mode='r', encoding="utf-8") as readme:
    long_description = readme.read()

print(f"[4/5] Running {package_name}'s setup routine . . .")

setup(
    author=author_name,
    author_email=author_email,
    name=package_name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    project_urls={
        "Documentation": url_documentation,
        "Source Code": url_source_code,
        "Bug Reports": url_bug_reports,
        "Changelog": url_changelog
    },
    python_requires=">=%d.%d" % (python_major, python_minor),
    install_requires=packages,
    extra_requires={
        "dev": dev_packages[1:],
        "test": ["pytest"]
    },
    include_package_data=True,
    package_dir={'': "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [f"{package_name}={package_name}.__main__:cli"]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    keywords="utils, terminal, application, template",
)

wheel_name = package_name.replace('-', '_') if '-' in package_name else package_name
print(f"[5/5] Setup is complete. Run 'python -m pip install dist/{wheel_name}-{version}-py{python_major}-none-any.whl' to install this wheel.")
