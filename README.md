<p align="center">
  <a title="Project Logo">
    <img height="150" style="margin-top:15px" src="https://raw.githubusercontent.com/Advanced-Systems/vector-assets/master/advanced-systems-logo-annotated.svg">
  </a>
</p>

<h1 align="center">Advanced Systems CLI Template</h1>

<p align="center">
    <a href="https://github.com/Advanced-Systems/cli-template" title="Release Version">
        <img src="https://img.shields.io/badge/Release-1.0.0%20-blue">
    </a>
    <a href="https://github.com/Advanced-Systems/cli-template/actions/workflows/python-app.yml" title="Unit Tests">
        <img src="https://github.com/Advanced-Systems/cli-template/actions/workflows/python-app.yml/badge.svg">
    </a>
    <a title="Supported Python Versions">
        <img src="https://img.shields.io/badge/Python-3.8%20%7C%203.9%20-blue">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" title="License Information" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/badge/License-GPLv3-blue.svg">
    </a>
    <a href="https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/Advanced-Systems/cli-template" title="Software Heritage Archive" target="_blank" rel="noopener noreferrer">
        <img src="https://archive.softwareheritage.org/badge/origin/https://github.com/Advanced-Systems/cli-template.git/">
    </a>
</p>

This is the starter code for lightweight CLI scripts that implements some common
features you might want to have in your application:

- organized project structure
- GitHub Action scripts
- unit tests
- exemplary command line interface
- logging
- static resource access in-code
- helper functions for basic terminal formatting
- pre-configured for deployment to [PyPI](https://pypi.org/)

This repository can also be easily installed with [pipx](https://pypa.github.io/pipx/)
in a virtual environment following modern best practices:

```bash
pipx install git+https://github.com/Advanced-Systems/cli-template.git
```

## Setup

<details>
<summary>Installation</summary>

Although this package is ready to go live on PyPI, you can still serve this locally
by running

```cli
# create virtual environment and install dependencies
python -m venv venv/
source venv/bin/activate
pip install -e . && pip install -r requirements/dev.txt
# run unit tests and read the log file
pytest --verbose
clitemplate log --list
```

</details>

## Project Architecture

<details>
<summary>Description</summary>

Using this template requires you to understand the project hierarchy, so here's
a quick rundown on the most important points:

1. `src/clitemplate` contains all code not directly related to packaging
2. `__init__.py` defines package meta data such as the version number
   in accordance with [semantic versioning](https://semver.org/)
3. `__main__.py` is the entry point of your application, you shouldn't need
   to change anything here
4. `cli.py` defines your CLI, but the business logic of your application should
   be placed in a separate file; for the sake of simplicity it's called `core.py`
5. `utils.py` contains auxillary methods for pretty terminal output and I/O operations
6. `core.py` defines your custom methods and serves as the backbone of your
   application
7. Dependencies are defined in `requirements/`. Use `release.txt` for production,
   and `dev.txt` for developer tool dependencies; workflow files should use `dev.txt`
   to install this application

</details>

## User-Customization

<details>
<summary>Checklist</summary>

Use the checklist below to customize this template for your project's need:

- [ ] Rename `src/clitemplate` to `src/{new_project_name}`
- [ ] Configure your package name and version number in `__init__.py`
- [ ] Update all meta data in `setup.py` (see also <https://pypi.org/classifiers/>
      for a full list of classifiers) and rename `src/clitemplate/__init__.py` to
      `src/{new_project_name}/__init__.py` on line 8
- [ ] Define new dependencies in `requirements/release.txt` and `requirements/dev.txt` as you see fit
- [ ] Edit `MANIFEST.in` if necessary (see also `src/{new_project_name}/data` for static resources)
- [ ] Configure `.gitignore`
- [ ] Customize GitHub Actions workflow
- [ ] Update `CHANGELOG.md`
- [ ] Rewrite this readme file

</details>

## Dev Notes

<details>
<summary>Commands</summary>

Check manifest. Make sure that you've setup your development environment to run
this command.

```cli
check-manifest --create
```

</details>

## Report an Issue

Did something went wrong? Copy and paste the information from

```cli
clitemplate log --list
```

to file a new bug report.
