<p align="center">
  <a title="Project Logo">
    <img height="150" style="margin-top:15px" src="https://raw.githubusercontent.com/Advanced-Systems/vector-assets/master/advanced-systems-logo-annotated.svg">
  </a>
</p>

<h1 align="center">Advanced Systems CLI Template</h1>

<p align="center">
    <a href="https://github.com/Advanced-Systems/cli-template" title="Release Version">
        <img src="https://img.shields.io/badge/Release-0.0.4%20-blue">
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

This is a template repository for CLI scripts written in python. We recommend
using `click` for parsing command line arguments, but any other library (like
`argparse`) could be used instead as well.

## Setup

<details>
<summary>Installation</summary>

Although this package is ready to go live on PyPI, you can still serve this locally
by running

```cli
# create virtual env and install dependencies
python -m venv venv/
source venv/bin/activate
pip install -e .
# test this script
cli-template --version
```

If you're a project contributor, use

```powershell
install.ps1
```

to setup your development environment.

</details>

## Project Architecture

<details>
<summary>Description</summary>

Using this template requires you to understand the project hierarchy, so here's
a quick rundown on the most important points:

1. `src/clitemplate` contains all code not directly related to packaging
2. `__init__.py` holds your version number, new releases should bump this value
   in accordance with [semantic versioning](https://semver.org/)
3. `__main__.py` is the entry point of your application, you shouldn't need
   to change anything here
4. `cli.py` defines your command line interface (CLI), but the business logic
   of your application should be placed in a separate file
5. `utils.py` contains auxillary methods for pretty terminal output and I/O operations
6. `core.py` defines your custom methods and serves as the backbone of your
   application
7. Dependencies are defined in `requirements/`. Use `release.txt` for production,
   and `dev.txt` for developer tool dependencies

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
- [ ] Choose a different license (uses GPLv3 by default)
- [ ] Configure `requirements/release.txt` and `requirements/dev.txt`
- [ ] Edit `MANIFEST.in` if necessary (see also `src/{new_project_name}/data` for static resource)
- [ ] Open `.gitignore` and add/remove items from this list (e.g. name of your
      virtual environment)
- [ ] Update `.gitattributes` (the default configuration here should be fine as is)
- [ ] Update (or remove) `.markdownlint.json`
- [ ] Add custom `yaml` files for CI/CD in `.github` and edit the issues templates
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
clitemplate log --read
```

to file a new bug report.
