# Analysis essentials [![Build Status](https://api.travis-ci.org/hsf-training/analysis-essentials.svg?branch=master)](https://travis-ci.org/hsf-training/analysis-essentials)

This is the source material for the [analysis essentials website][website], a 
series of lessons for helping high-energy physics analysts become more 
comfortable working with the shell, version control, and programming.

The lessons introduce the basics of the bash shell, the git version control 
system, and the Python programming language. They are developed for and taught 
during the [Starterkit][starterkit], and aim to teach students enough to be 
able to follow the experiment-specific lessons that are taught afterwards.

Contributions to the lessons are highly encouraged. Please see the 
[contributing guide][contributing] for details on how to participate.

## Prerequisits

This tutorial uses ```Python 3.7``` and requires some packages. It is 
reccommended to use [Conda](https://docs.conda.io/en/latest/) to install the 
correct packages.

To install ```Conda``` you will need to do the following:

 - Install ```Conda``` according to the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-in-silent-mode)
 - You can add ```source /my/path/for/miniconda/etc/profile.d/conda.sh``` to your ```.bashrc``` 
 - Add the channel: 
```bash
conda config --add channels conda-forge
```

Now to use your first ```Conda``` environment:
 - Create an environment with some packages already installed:
```bash
conda create -n my-analysis-env python=3.7 jupyterlab ipython matplotlib uproot numpy pandas scikit-learn scipy tensorflow xgboost hep_ml
```
 - Activate your environment by doing: ```conda activate my-analysis-env```
 - You can install additional packages by doing: ```conda install package_name```

You will also need [Jupyter](https://jupyterlab.readthedocs.io/) to run the examples in this tutorial.
Jupyter was already installed in the previous command and can be ran by following the instructions [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html).
Note: You **will** need Python.

## Usage

You should now be able to use the tutorial.
 - First clone with git:
```bash
git clone https://github.com/hsf-training/analysis-essentials.git
```
 - For more information on getting started with git please see the [Analysis Essentials course](https://lhcb.github.io/analysis-essentials/index.html)
```bash
cd advancedpython
jupyter notebook
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
    git/README.md
    CONTRIBUTING.md
```
