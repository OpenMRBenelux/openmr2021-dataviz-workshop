# Repository for OpenMR Virtual 2021 data visualisation workshop - Python

To open the Jupyter Notebook in a Binder environment, click the following link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OpenMRBenelux/openmr2021-dataviz-workshop-python/HEAD?filepath=.%2Fcode%2F)

By doing so, everything will be set up for you, without having to worry about
things such as package dependencies. You can start working on the tutorial
notebook right away! :smile:


# How to contribute

## Set up

### Create virtual environment

#### With virtualenv

```bash
# create a virtual environment and "activate" it
virtualenv -p /usr/bin/python3.8 envs/dataviz_python
source envs/dataviz_python/bin/activate

# install in this environment all the Python packages
# listed in the requirements.txt file
pip install -r requirements.txt
```

#### With conda

The first time

```
conda env create -n dataviz_python -f ./binder/environment.yml
```

To update the environment after changes were made to `./binder/environment.yml`

```
conda env update -n dataviz_pythonv -f ./binder/environment.yml
```

## Download the required data

<!-- TODO improve datalad install instruction -->

We are using the fact that the openneuro datasets can be accessed through their
siblings on github:

https://github.com/OpenNeuroDatasets

For more info see the handbook:
http://handbook.datalad.org/en/latest/basics/101-180-FAQ.html#how-does-datalad-interface-with-openneuro

```bash
datalad clone https://github.com/OpenNeuroDatasets/ds003542.git inputs/ds003542/
datalad get inputs/ds003542/sub-01/func/sub-01_task-compL1_run-1*
datalad get inputs/ds003542/sub-01/anat/
```
