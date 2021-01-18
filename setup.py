#!/usr/bin/env python3

from setuptools import setup

parse = lambda lines, index: lines[index-1].split(' ')[2].replace('"', '').strip('\n')

with open("src/__init__.py", encoding='utf8') as file_handler:
    lines = file_handler.readlines()
    version = parse(lines, 3)
    package_name = parse(lines, 4)

with open("requirements.txt", encoding='utf-8') as file_handler:
    packages = file_handler.read().splitlines()

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name=package_name,
    version=version,
    install_requires=packages,
    include_package_data=True,
    entry_points=f'''
        [console_scripts]
        {package_name}=src.__main__:cli
    ''',
)
