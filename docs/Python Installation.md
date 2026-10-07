
## Python and Environment Setup Guide

## 1. Python Installation & Version Control

* Installation: Download and run the official Python installer from python.org.
* Current Version: Python 3.12.10.
* Check Version Command:

python --version


## 2. Python pip (Preferred Installation Program)
pip is automatically installed with Python and is used to manage external libraries and modules.

* Install a package: pip install package
* Install a specific version: pip install package==version
* Upgrade a package: pip install --upgrade package
* Uninstall a package: pip uninstall package
* List all installed libraries: pip list
* Show package details: pip show package

## 3. Virtual Environments

* Create a virtual environment:

py -3.12 -m venv env

* Activate environment (Windows):

env\Scripts\activate

* Deactivate environment:

deactivate


## 4. Package Installation & PyPI

* Definition: Installing third-party modules and packages into a specific project.
* PyPI: The public repository where developers upload their custom build packages and modules.
* pip Function: Downloads and installs these packages directly from PyPI onto your computer.

## 5. Requirements Files
A requirements.txt file contains a list of project packages alongside their specific versions (e.g., pytest==9.1.1).

* Save current packages to file:

pip freeze > requirements.txt

* Install packages from file (on another machine):

pip install -r requirements.txt


## 6. Environment Variables
Settings stored within your operating system that can be accessed securely by software or Python applications.

* Python Usage:

import ossecret_key = os.environ.get('MY_PASSWORD')


## 7. Terminal Usage
Running Python files or installing packages by typing commands directly into the Command Prompt (CMD) or terminal.

* Examples: pip install package or python src/main.py

## 8. Basic Linux Commands
Keyboard commands used to navigate and manage a Linux operating system without a mouse.

* pwd : Print working directory
* ls : List files in a folder
* cd : Change directory
* mkdir : Make a new directory
* touch : Create a new blank file
* mv : Move or rename a file
* rm : Remove/delete a file
* cat : Display all data within a file

## 9. Project Directories, Modules, & Packages

* Project Directories: Organizing large Python projects into separate, dedicated folders for specific tasks instead of bundling all code together.
* Python Modules: Any single file with a .py extension (e.g., main.py).
* Python Packages: A folder containing a collection of modules. To make Python recognize a folder as a package, it traditionally includes an empty file named __init__.py (optional after Python 3.3, but still standard practice).


