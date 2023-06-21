## Introduction
This folder contains the following code files that produce output .csv files and .png figures found in [`20230404/results`](https://github.com/sarahfi2her/variability/tree/main/20230404/results)


## [`bin_selection.ipynb`](https://github.com/sarahfi2her/variability/blob/main/codebase/bin_selection.ipynb)
Calculation of optimal number of bins and their edge configuration for features of interest
- Finds bin configurations for discretizing the continuous distributions of features of interest suggested by unsupervised `matplotlib.pyplot` methods
  - Methods include `sqrt`, `rice`, `sturges`, `doane`, `fd`, `scott`, and `stone` (each detailed [here](https://github.com/sarahfi2her/variability/wiki/Notebook#binning))
- Uses the minimum and maximum numbers of bins suggested by these methods as the range in bin numbers over which a feature's distribution is discretized and its entropy is calculated
- Finds the knee-point in the graph of entropy of the distribution as a function of the number of bins it is discretized across  
   - Utilizes `kneed.KneeLocator.knee`
   - This is the point in which an increase in number of bins provides no significant increase in detail (the optimal number of bins)

Corresponding plots of entropy for the visualization of this supervised, entropy-based optimized binning method are produced by [`bin_selection_plot.ipynb`](https://github.com/sarahfi2her/variability/blob/main/codebase/bin_selection_plot.ipynb)

## [`bin_validation.ipynb`](https://github.com/sarahfi2her/variability/blob/main/codebase/bin_validation.ipynb)
Calculation of inter-well mutual information that validates the selection of bin configuration
- ...

Corresponding plots of inter-well mutual information that validates the selection of bin configuration are produced by [`bin_validation_plot.ipynb`](https://github.com/sarahfi2her/variability/blob/main/codebase/bin_validation_plot.ipynb)


## ...
