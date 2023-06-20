## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10
- `area_validation_mi_10.png`
- `gfp_validation_mi_10.png`
- `rfp_validation_mi_10.png`

## Figure descriptions
**Axes**

The `x-axis` describes the range in sampling size of subsets of cells selected from each well for mutual information calculation
- This range has a minimum of 0 and a maximum determined by average number of cells across all of the wells in the set of selected timesteps

The `y-axis` describes the mutual information of the sampled population
- This range is determined by the range in mutual information calculated for each of the sample populations

**Data**

A joint random sampling of the subset size of one of the following features from each well at the specified timestep
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `colored lines` plot the behavior of mutual information as a function of well sampling size
- ***(x, y)*** (the number of cells randomly sampled frome each well at a given timestep (specified in the legend), the mutual information calculation between wells)
- ***Behavior*** logarithmic

## Observations
The mutual information at a timestep should be constant regardless of the well sampling size
- We can naively expect these lines to be horizontal

To account for the logarithmic behavior of these lines, we conclude that any number of cells less than the number at which the logarithmic line plateaus (`~50`) 
is too small of a sampling size to produce meaningful results

Therefore, when analyzing future graphs that plot some behavior as a function of time, we can ignore the data obtained at timesteps at which 
some well does not have at least this minimum number of cells
