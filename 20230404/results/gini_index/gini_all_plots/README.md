## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10
- `area_gini_all_10_no_start.png`
- `gfp_gini_all_10_no_start.png`
- `rfp_gini_all_10_no_start.png`
  
## Figure descriptions
**Axes**

The `x-axis` describes time, in minutes, of the experiment
- This range has a minimum of `~600 mins` (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the Gini coefficient of a well's distribution
- This range is determined by the range in Gini coefficient values calculated for each well at each timestep

**Data**

The distributions of each of the following features in each well at each timestep
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `colored lines` plot the behavior of Gini coefficient as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions were taken, the Gini index of the distribution of the well specified in the legend)
- ***Behavior*** generally low and constant (in `gfp`) or slowly increasing (in `rfp`) after the rise in temperature at `~2200 mins`

## Observations

As in most results, the `area` plot has a behavior that is different from `rfp` and `gfp`, given that the feature has been shown to have no significance
- This assumes a range higher than that of `rfp` and `gfp`, indicating less evenness in the distribution of cell size in the populations
- Lower Gini coefficients seemed to become available to populations after the increase in temperature

Both `rfp` and `gfp` have similar behavior with the following interesting details
- Well `01` has a relatively higher Gini coefficient in its `gfp` distributions than the others (although still very, very small given its value at `0.06`)
- Well `14` has an interesting steep increase after timestep `~5000 mins` in both distributions, indicating a growing decrease in evenness of `rfp` and `gfp` values over time
- Well `06` is observed to have a higher Gini coefficient in relation to other distributions in `rfp` than in `gfp`
- Well `12` is very near `0` in both `gfp` and `rfp` distributions
- Although the increase in temperature seems to only allow higher Gini coefficients to become available in `rfp` distributions, the increase in temperature allows lower Gini coefficients to become available to `gfp` distributions

These figures quantify the uncertainty seen in each well's distributions, identifying interesting outliers specified above but also showing the general behavior of a minor shift in Gini coefficients for wells after the increase in temperature
