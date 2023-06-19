## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name
-  `area_bin_entropies.png`
-  `gfp_bin_entropies.png`
-  `rfp_bin_entropies.png`

## Figure descriptions
**Axes** 

The `x-axis` describes the range in number of bins over which the entropy of the specified set of data is calculted
- This range is determined by the minimum and maximum numbers of bins suggested by unsupervised binning methods

The `y-axis` describes the entropy of the set of data when descritized with each number of bins
- This range is determined by the minimum and maximum entropy calculated for the set of measurements

**Data**

The set of all measurements of one of the following features across all wells and timesteps
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `grey solid line` plots the behavior of entropy as a function of number of bins
- ***(x, y)*** (number of bins over which the data is discretized for its entropy calculation, the calculated entropy)
- ***Behavior*** logarithmic

The `colored dotted lines` mark a set of numbers of bins
- ***(x, y)*** (the number of bins that each of the methods (specified in the legend) suggest for the set of data, _)
- ***Behavior*** vertical

The `red dashed line` marks the optimal number of bins
- ***(x, y)*** (the knee point of the graph of entropy, _)
- ***Behavior*** vertical

## Observations

The knee point of the graph of entropy (`red dashed line`) marks the point at which adding more bins fails to add significantly more detail to the set of data
- This serves as out optimal number of bins for calculating entropy (and thus mutual information)

The optimal number of bins for `area` is 330, and for both `rfp` and `gfp` is 410. 

