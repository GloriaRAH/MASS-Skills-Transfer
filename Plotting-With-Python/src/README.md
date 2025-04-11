## IDE

Visual Studio Code is preferred. The workspace settings are already included in the repository.
If you want to use plain notebook, that is still fine. Just make sure to install the required extensions.

## Create an environment

To create a conda environment called `skilltransfer` with Python 3.11, run:

```
conda create -n skilltransfer python=3.11
conda activate skilltransfer
```

## How to install dependencies

Declare any dependencies in `requirements.in` for `pip` installation. You need to work around the equivalence for `conda`.

To install them, you need to upgrade your pip and install the pip-tools first:

```
pip install --upgrade pip pip-tools
```

Then, run:

```
pip-compile --output-file requirements.txt requirements.in
pip-sync requirements.txt
