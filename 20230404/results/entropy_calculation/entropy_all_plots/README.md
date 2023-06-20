## Folder contents

This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10
- `area_entropy_all_10_no_start.png`
- `gfp_entropy_all_10_no_start.png`
- `rfp_entropy_all_10_no_start.png`

## Figure descriptions
**Axes**

The `x-axis` describes time, in minutes, of the experiment
- This range has a minimum of ~600 mins (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the entropy of a well's distribution
- This range is determined by the range in entropy values calculated for each well at each timestep

**Data**

The distributions of each of the following features in each well at each timestep
- area of a cell (area)
- mean gfp across all pixels in a cell (gfp)
- mean rfp across all pixels in a cell (rfp)

**Plots**

The `colored lines` plot the behavior of entropy as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions were taken, the entropy of the distribution of the well specified in the legend)
- ***Behavior*** generally increasing (in `rfp` and `gfp`)

## Observations
As in most results, the `area` plot has a behavior that is different from `rfp` and `gfp`, given that the feature has been shown to have no significance
- There is a general decreasing trend, indicating that the distribution of area size decreases in standard deviation, especially in well `09` after the rise in temperature at `~2200 mins`
- However, the difference in values is quite small (`0.3 bits`) while the entropy is still quite high (`4.2 bits`), so even this observation has questionable significance

Both `rfp` and `gfp` have a general increasing trend with the following interesting details
- Well `15` sees a major decrease in the entropy of its `gfp` distribution in the face of increased temperature at `~2200 mins`
- Well `12` interestingly maintains the entropy of its `gfp` distribution after the temperature increase
- Wells `12` and `15` similarly see the least entropy increase in their `rfp` distributions
- Well `06` has the largest entropy in both distributions and sees an interestingly steep increase in its `rfp` distribution

These figures quantify the uncertainty seen in each well's distributions, identifying interesting outliers specified above but also showing the general behavior of 
an increase in entropy through time, enhanced by increased temperature
