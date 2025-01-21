# Python Simian workshop

## Learning goals

* Introduction into Simian
* Build a Simian web app
  * Add controls to a web app with code and Simian Builder.
  * Make the web app functional: Use the settings selected in the app to modify the app or perform a calculation.
  * Present results in tables and graphs.
  * (Optional) Hide controls based on settings in the front-end.
  * (Optional) Validate settings in the front-end.
* Test and debug web app locally
* (Optional) Deploy web app
* (Optional) Make deployed web app accessible from portal


## Prerequisites

Installed programs and basic knowledge of:

* Python 3.8 - 3.12

    Local development mode uses `pywebview` installed with Simian Local.

* An Editor that supports Python

* Git

    (Optional) For cloning the workshop files from a Git repo and for pushing Simian GUI web apps to a deployment server.

    If interaction with the repository is not possible, the workshop files are provided in a .zip file.

* (Optional) Python code deployment environment

    <https://doc.simiansuite.com/simian-gui/deployment/python.html>

    Access rights and knowledge of how to deploy Python code to the preferred deployment environment.


## Preparations

* Install Simian GUI, Simian Local, Simian Examples, and Simian Builder as documented in <https://doc.simiansuite.com/simian-gui/setup/python.html> and <https://doc.simiansuite.com/simian-gui/builder.html>
* Unzip or Git clone the workshop files to a location where they can be run with Python.
  * Details are communicated separately.
* Run the `workshop_application.py` file. An app with only the text "Intentionally left empty" should appear in a `pywebview` window.
  * If you get Python import errors, ensure that the Python path contains the folder with the workshop files and that Simian is installed correctly.
* (Optional) deployment environment for Python code setup and rights granted.
* (Optional) Simian portal installed and admin rights granted.


## Folder contents

* This `readme.md` file
* `Workshop_exercises.md` file describing the workshop.
* `workshop_application.py`- blank Simian web app to work in.
* `workshop_application.json` - blank Simian web app .json definition.
* `runWorkshopExampleLocally.py` script to run the `simian.examples.workshop_example` web app.
