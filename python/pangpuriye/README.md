# **pangpuriye in PyPi**

## **Contributing**
### **Installation**

In console (terminal or cmd) :

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

output:

```bash
Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

$HOME/.poetry/bin

This path will then be added to your `PATH` environment variable by
modifying the profile files located at:

$HOME/.profile
$HOME/.zshrc

You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing version: 1.1.4
  - Downloading poetry-1.1.4-darwin.tar.gz (38.00MB)

Poetry (1.1.4) is installed now. Great!

To get started you need Poetry's bin directory ($HOME/.poetry/bin) in your `PATH`
environment variable. Next time you log in this will be done
automatically.

To configure your current shell run `source $HOME/.poetry/env`
```

Activate `poetry` :

```bash
$ source $HOME/.poetry/env
```

testing :

```bash
$ poetry --version

Python 2.7 will no longer be supported in the next feature release of Poetry (1.2).
You should consider updating your Python version to a supported one.

Note that you will still be able to manage Python 2.7 projects by using the env command.
See https://python-poetry.org/docs/managing-environments/ for more information.

Poetry version 1.1.4

```

## **Add Dependencies in existing project**

```bash
$ poetry init
```

output:

```bash
Python 2.7 will no longer be supported in the next feature release of Poetry (1.2).
You should consider updating your Python version to a supported one.

Note that you will still be able to manage Python 2.7 projects by using the env command.
See https://python-poetry.org/docs/managing-environments/ for more information.


This command will guide you through creating your pyproject.toml config.

Package name [pangpuriye]:
Version [0.1.0]:
Description []:
Author [-------------------- <-----------@gmail.com>, n to skip]:
License []:  MIT
Compatible Python versions [^2.7]:

Would you like to define your main dependencies interactively? (yes/no) [yes]
You can specify a package in the following forms:
  - A single name (requests)
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Search for package to add (or leave blank to continue): opencv-python
Found 20 packages matching opencv-python

Enter package # to add, or the complete package name if it is not listed:
 [0] opencv-python
 [1] opencv-python-aarch64
 [2] opencv-contrib-python
 [3] opencv-python-headless
 [4] opencv-openvino-contrib-python
 [5] opencv-python-inference-engine
 [6] opencv-contrib-python-headless
 [7] streamz-opencv
 [8] opencv-pg
 [9] opencv_cffi
 > 0
Enter the version constraint to require (or leave blank to use the latest version):
Using version ^4.5.1 for opencv-python

Add a package: numpy==1.19.0
Adding numpy==1.19.0

Add a package: pdf2image==1.14.0
Adding pdf2image==1.14.0

Add a package: detecto
Found 20 packages matching detecto

Enter package # to add, or the complete package name if it is not listed:
 [0] detecto
 [1] rmotr-b7-c1-g1-jobs-detectorr
 [2] aime-detector-sdk
 [3] noise-detector
 [4] arm-float-detector
 [5] detector-worker
 [6] also-anomaly-detector
 [7] log-anomaly-detector
 [8] sensor-outlier-detector
 [9] qxbranch.quantum-feature-detector
 > 0
Enter the version constraint to require (or leave blank to use the latest version):
Using version ^1.2.0 for detecto

Add a package: torch==1.4
Adding torch==1.4

Add a package: torchvision==0.5.0
Adding torchvision==0.5.0

Add a package: tqdm==4.54.1
Adding tqdm==4.54.1

Add a package: easyocr==1.2.1
Adding easyocr==1.2.1

Add a package: pyyaml
Found 20 packages matching pyyaml

.
.
.

Add a package:

Would you like to define your development dependencies interactively? (yes/no) [yes]
Search for package to add (or leave blank to continue):

Generated file

[tool.poetry]
name = "pangpuriye"
version = "0.1.0"
description = ""
authors = ["Pathara Norasethasopon <patharanor@gmail.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.6"
tqdm = "4.54.1"
PyYAML = "^5.3.1"
opencv-python = "^4.5.1"
torchvision = "0.5.0"
detecto = "^1.2.0"
torch = "1.4"
easyocr = "1.2.1"
matplotlib = "^3.3.3"
pytesseract = "^0.3.7"
pythainlp = "^2.2.6"
python-Levenshtein = "0.12.0"
pdf2image = "1.14.0"
strsimpy = "^0.2.0"
numpy = "1.19.0"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes]
```

## **Switch environment from Python2.7 to Python3.X**

In case you found an error when `poetry install` dependencies of your project, you should switch Python environment by :

```bash
$ poetry env use python3.7
```

## **Testing before build**

You need to do unit test first, to ensure your library works fine.

```bash
$ python3 -m unittest ./tests
```

## **Build/Packing**

```bash
$ poetry build
```

## **Publish**

By default publish to PyPi

### **Dry run**

Before publish you should dry run first, perform all actions except upload the package :

```bash
$ poetry publish --username PYPI_USER_NAME --password PYPI_PASSWORD --dry-run
```

If it has any error, now you can publish it :

```bash
$ poetry publish --username PYPI_USER_NAME --password PYPI_PASSWORD
```

## **License**

MIT