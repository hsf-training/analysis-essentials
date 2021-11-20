# Advanced Python Tutorial

Welcome to the advanced Python tutorials  of the starterkit. This lecture covers multiple topics
and the notebooks available may fill more than the scheduled lesson. However, they also serve as
a knowledge base that one can always come back to lock up things.

```eval_rst
.. toctree::
    :maxdepth: 3
    :includehidden:
    :caption: Contents:

    10Basics.ipynb
    11AdvancedPython.ipynb
    12AdvancedClasses.ipynb
    20DataAndPlotting.ipynb
    30Classification.ipynb
    31ClassificationExtension.ipynb
    32BoostingToUniformity.ipynb
    33OLDDemoNeuralNetworks.ipynb
    40DemoReweighting.ipynb
    50LikelihoodInference.ipynb
    60sPlot.ipynb
    70ScikitHEPUniverse
```


## Lesson overview 

### Pure Python, advanced

 - Notebook 10 starts out with a repetition of the basics of Python.
 - In notebook 11, advanced concepts like
exceptions, context manager and the factory-pattern together with decorators is introduced.
- 12 is a tutorial about classes, especially on the focus of dunder (`__meth__`) methods and
covers from simpler `__len__` and add up to the advanced `__getattr__`.

### Data loading and plotting

Notebook 20 introduced data loading with uproot, Pandas DataFrames as the default container for columnar data
that can apply cuts and the plotting libraries.

More on pandas can be found in their 
[excellent documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) 
or by searching the web

### Multivariate Analysis and Machine Learning

These notebooks provide an introduction to more sophisticated cuts using machine learning techniques.
- 30 starts out with the basics of using a BDT and the scikit-learn standard library for this kind
of problems and algorithms.
- 31 demonstrates another BDT, XGBoost, which is the state-of-the-art algorithm of a BDT
- 32 contains a tutorial about a special kind of BDTs which actively de-correlate the BDT response from
 variables. This is often required in physics analysis in order not to bias the inference.
 
- 33 is a currently outdated intro to Neural Networks

More tutorials for general machine learning algorithms can be found in the 
[scikit-learn tutorial section](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)


### Reweighting

Reweighting a distribution can be a useful technique to apply corrections.
- 40 demonstrates two methods of non-parametric reweighting of two distributions in order
to correct for MC and data differences. Histogram-based as well as the more powerful, yet
harder to control GradientBoostingReweighter are introduced

### Statistical Inference

The last step in most analysis is the inference through a likelihood based method. This involves
to fit a model to data or toy datasets repeatedly in order to infer the physical parameters that
we are interested in but also it's uncertainty.
- 50 introduces the likelihood model fitting with the `zfit` library. While the main introduction
is pointed towards an actual zfit tutorial, it provides a guide to implement the fit to the data
obtained in previous tutorials. `hepstats` is also introduced as it works with zfit models and
is used to estimate the significance of the discovery.

More tutorials on [zfit](https://github.com/zfit/zfit-tutorials) as well as 
[hepstats](https://github.com/scikit-hep/hepstats/tree/master/notebooks) are available.

### sPlot technique

The sPlot - or sWeights - technique is introduced; a technique to statistically subtract the background
events in a variable. The technique as well as the library to obtain the weights is demonstrated.

### Scikit-HEP

Many libraries that are seen in this tutorial are part of 
[Scikit-HEP, the HEP Python ecosystem](https://scikit-hep.org/).
Not all packages have been used though and in tutorial 70, a few smaller, yet useful packages are presented to give
an idea of what is available.
