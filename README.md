<p align="center">
  <a title="Project Logo">
    <img height="150" style="margin-top:15px" src="https://raw.githubusercontent.com/Advanced-Systems/vector-assets/master/advanced-systems-logo-annotated.svg">
  </a>
</p>

<h1 align="center">Advanced Systems CLI Template</h1>

<p align="center">
    <a href="https://github.com/Advanced-Systems/cli-template" title="Release Version">
        <img src="https://img.shields.io/badge/Release-2.0.0%20-blue">
    </a>
    <a href="https://github.com/Advanced-Systems/cli-template/actions/workflows/python-app.yml" title="Unit Tests">
        <img src="https://github.com/Advanced-Systems/cli-template/actions/workflows/python-app.yml/badge.svg">
    </a>
    <a title="Supported Python Versions">
        <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20-blue">
    </a>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" title="License Information" target="_blank" rel="noopener noreferrer">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</p>

This template repository was developed to bootstrap the initial creation process
of CLIs and provides the following features out of the box:

- GitHub Action workflows for unit tests, static code analyses and deployment to
  PyPI
- a `Logger` helper class as a thin wrapper around the standard
  [`logging`](https://docs.python.org/3/howto/logging.html) module
- provides some starter code for handling configuration files by using the standard
  [`configparser`](https://docs.python.org/3/library/configparser.html) module
- some starter code for advanced command line applications using
  [`click`](https://click.palletsprojects.com/en/8.1.x/api/)
- also integrates very well with [`rich`](https://github.com/Textualize/rich)

## Installation

Click on the [`Use this template`](https://github.com/Advanced-Systems/cli-template/generate)
button to create a new repository and install the project in a virtual environment:

```powershell
python -m venv venv/
.\venv\Scripts\Activate.ps1
pip install -e .
pip install -r requirements/dev.txt
```

You can use the `configure.ps1` script in the `scripts` directory to help you
customize this application:

```powershell
.\scripts\configure.ps1
```

Alternatively, you can make these changes yourself by editing the
`src/clitemplate/__init__.py` file. Note that you should also rename the `clitemplate`
folder in the `src` directory to match your `package_name`. For terminal applications
specifically, take into account the following recommendations:

- _use_ short and concise names for CLI programs
- _avoid_ generic names that could cause a conflict with established standard tools
- _avoid_ special characters such as `-` or `_` in your application name

## Basic Usage

The starter code implements a standard interface to help you get started with writing
your own commands:

```powershell
# the package name also declares the entry point of the application
# remember: you should always implement the help and version flag
clitemplate --help
clitemplate --version

# the square function is implemented as a subcommand here
# it is considered good practice to provide an optional verbose flag
clitemplate --verbose square --xmin <int> --xmax <int>
```

## Dev Notes

You can also install this project with [`pipx`](https://pypa.github.io/pipx/)
if you don't want to deploy this project on PyPI:

```powershell
python -m pip install pipx
pipx install git+https://github.com/Advanced-Systems/cli-template.git
```
