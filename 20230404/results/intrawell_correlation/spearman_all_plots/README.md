## Folder contents

This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10

- `spearman_all_10_no_start.png`

## Figure descriptions

**Axes**

The `x-axis` describes time, in minutes, of the experiment
- This range has a minimum of `~600 mins` (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the Spearman correlation between `rfp` and `gfp` measurement within a well
-  This range is determined by the range in Spearman correlation values calculated between `rfp` and `gfp` for each well at each timestep

**Data**

The distributions of each of the following features in each well at each timestep
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `colored lines` plot the behavior of Spearman correlation between `rfp` and `gfp` as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions were taken, the Spearman correlation between the distributions of `rfp` and `gfp` in the well specified in the legend)
- ***Behavior*** generally stable

## Observations 

- The correlation between `rfp` and `gfp` in well `01` dips well below the other wells before the rise in temperature 
- There is a sudden increase in all Spearman correlation values at `~2200 mins` with the increase in temperature
- Some wells (namely `10`, `06`, `14`, and `07`) participate in a decrease in correlaiton between `3000 mins` and `4000 mins`, in which time there is a drop in temerature
- Well `10` (the well receiving feedback) is significaly less correlated than the rest
- There is a steep decrease in correlation at the end of the experiment as temperature nears `39` degrees

Except for the above named exceptions, correlation seems to be stable and high (above `0.7`) before and after the rise in temperature
