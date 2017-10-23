#!/usr/bin/env python
from matplotlib import pyplot as plt
import numpy as np


data = np.random.normal(4, 2, 1000)
bins = np.linspace(0, 10, 50)

plt.hist(data, bins=bins, histtype='stepfilled')
plt.savefig('plots/first_plot.pdf')
