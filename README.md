# Analysis essentials [![Build Status](https://api.travis-ci.org/hsf-training/analysis-essentials.svg?branch=master)](https://travis-ci.org/hsf-training/analysis-essentials) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hsf-training/analysis-essentials/master)


This is the source material for the [analysis essentials website][website], a
series of lessons for helping high-energy physics analysts become more
comfortable working with the shell, version control, and programming.

The lessons introduce the basics of the bash shell, the git version control
system, and the Python programming language. They are developed for and taught
during the [Starterkit][starterkit], and aim to teach students enough to be
able to follow the experiment-specific lessons that are taught afterwards.

Contributions to the lessons are highly encouraged. Please see the
[contributing guide][contributing] for details on how to participate.

## Prerequisites

There are two options for running these lessons. Running locally should be prefered on Linux and macOS as it is faster and makes it easier to save you work. On Windows it is likely easier to use Binder however care is needed to prevent notebooks being lost when the server is shut down.

### Local

This tutorial uses `Python 3.11` and requires some packages.
It is recommended to use [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) to install the correct packages.
**Note:** `mamba` is like `conda` and can be used interchangeably. "forge" in the name refers to the [conda-forge](https://conda-forge.org/) channel, _the_ open-source maintained channel which contains a lot of packages.

To install `Conda`/`mamba` you will need to do the following:

 - Install `mamba` according to the instructions [here](https://github.com/conda-forge/miniforge#install)
 - To add `mamba`/`conda` to your shell, follow the instructions after the installation and execute
```bash
mamba init
```
 - In order no not use the base environment (which you almost never should), do
```bash
conda config --set auto_activate_base false
```


Now to use your first ```Conda/Mamba``` environment:
 
 - This will install the above packages. In order to make sure that you install all of the packages needed in the tutorial, you can use the `environment.yml` file (make sure that the file `environment.yml` is in the current directory):
```bash
mamba env create -f environment.yml
```
 - Alternatively, you could create an environment with some packages already in this way
```bash
mamba create -n analysis-essentials python=3.11 jupyterlab ipython matplotlib uproot numpy pandas scikit-learn scipy tensorflow xgboost hep_ml wget
```
 - Activate your environment by doing: `mamba activate analysis-essentials`
 - You can install additional packages by doing: `mamba install package_name`


You will also need [Jupyter](https://jupyterlab.readthedocs.io/) to run the examples in this tutorial.
Jupyter was already installed in the previous command and can be ran by following the instructions [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html).
Note: You **will** need Python.

### Binder

Click this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hsf-training/analysis-essentials/master)

## Usage

You should now be able to use the tutorial.
 - First clone with git:
```bash
git clone https://github.com/hsf-training/analysis-essentials.git
```
 - For more information on getting started with git please see the [Analysis Essentials course](https://hsf-training.github.io/analysis-essentials/index.html)
```bash
cd analysis-essentials
jupyter lab
```
This should open a Jupyter webpage with the current directory displayed.
Navigate to one of the lessons to start the tutorial.

If you have any problems or questions, you can [open an issue][issues] on this repository.

[website]: https://hsf-training.github.io/analysis-essentials/
[starterkit]: https://lhcb.github.io/starterkit/
[contributing]: CONTRIBUTING.md
[issues]: https://github.com/hsf-training/analysis-essentials/issues

```eval_rst
.. toctree::
    :maxdepth: 3
    :includehidden:
    :caption: Contents:

    python/README.md
    advanced-python/README.md
    shell/README.md
    shell-extras/README.md
    snakemake/README.md
    git/README.md
    CONTRIBUTING.md
    CONDUCT.md
```
