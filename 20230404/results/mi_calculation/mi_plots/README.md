## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10
- `area_mi_line_10_temp_10_start.png`
- `gfp_mi_line_10_temp_10_start.png`
- `rfp_mi_line_10_temp_10_start.png`
- `mi_line_all_10_temp_10_start.png`

## Figure descriptions

**Axes**

The `x-axis` describes the time, in minutes, of the experiment
- This range has a minimum of 0 and a maximum of the number of minutes over which the experiment ran

The `y-axis` describes the mutual information, in bits, between each well's distribution of the feature of interest
- This range is determined by the range in mutual information calculated between each well

**Data**
The distributions of each of the following features from each of the wells at each timestep
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `colored lines` (`green` for `gfp`, `red` for `rfp`, or `blue` for `area`) plot the behavior of mutual information as a function of time
- ***(x, y)*** (the time at which the distributions are referenced, the mutual information calculated between the distributions in values of the feature of interest in each well)
- ***Behavior** stable agter initial rise in temperature (after `~2500 mins`)

The `grey line` indicates the temperature, scaled to the other data for visualization
- ***(x, y)*** (the time at which the temperature is referenced, the relative temperature at that time (scaled for visualization))
- ***Behavior*** small increase at `~1500 mins`, major increase between `2000 mins` and `3000 mins`, dip between `~3300 mins` and `~3800 mins`

The `gold dashed line` markeds the time in the experiment at which there are at least 50 cells in each well
- ***(x, y)*** (starting point for valid measurements, _)
- ***Behavior*** vertical

## Observations 

A high mutual information indicates wells that have distinct character from one another in a given feature of interest

The plot of `area` remains near `0.0 bits`, indicating a low mutual information and indistinguishable distributions between wells throughout the experiment

However, `rfp` and `gfp` are informative of distinguishable phenotypes
- Both plots of `rfp` and `gfp` have similar behavior
- There is a rise in mutual information at the start of the experiment that leats to a plateau at `~0.5 bits` between `1000 mins` and `2000 mins`
- There is a short dip in mutual information at `~1800 mins` when the temperature first begins to increase
- There is a steady increase in mutual information between `~2000 mins` and `~2200 mins` at which time the mutual information plateaus for the remainder of the experiment
- The mutual information in `rfp` sees a very slight decreasing slope throughout this plateau
- The plateau begins before the rise in temperature stops, indicating a potential saturation in mutual information

From this graph, we can see that there is a correlation in the mutual information of `rfp` and `gfp`, reacting to the increase in temperature until a constant mutual information arises
