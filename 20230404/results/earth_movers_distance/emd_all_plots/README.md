## Folder contents

This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name with x-values averaged in intervals of 10
- `area_emd_all_10_no_start.png`
- `area_emd_all_10_start.png`
- `gfp_emd_all_10_no_start.png`
- `gfp_emd_all_10_start.png`
- `rfp_emd_all_10_no_start.png`
- `rfp_emd_all_10_start.png`

## Figure descriptions

**Axes**

The `x-axis` describes time, in minutes, of the experiment
- In `*_emd_all_10_start.png` figures, this range has a minimum of 0 and a maximum determined by length, in minutes, of the experiment
- In `*_emd_all_10_no_start.png` figures, this range has a minimum of  `~600 mins` (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the Earth Mover's distance between a well's distribution and the joint distribution across all wells
- This range is determined by the range in Earth Mover's distance values calculated for each well

**Data**

The values of one of the following features in each well at each timestep
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `colored lines` plot the behavior of Earth Mover's distance as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions were taken,
the Earth Mover's distance calculated between the distribution of a well (specified in the legend) and the joint distribition at the corresponding time)
- ***Behavior*** constant with a sharp increase at time `~2200 mins`

The `grey dashed line` (in only `*_emd_all_10_start.png` figures) marks the time at which there are at least 50 cells in each well
- ***(x, y)*** (the starting time of the experiment, _)
- ***Behavior*** vertical

## Observations
As in most results, the `area` plot has a behavior that indicates no particular outstanding wells, given that the feature has been shown to have no significance

Both plots of `gfp` and `rfp` seem to have similar outstanding wells after the jump in temperature at `~2200 mins`, 
- Wells seem to increase in distance from the joint distribution slowly after the jump in temperature
- Well `01` has the most distance from the joint distribution (`~400` in `gfp`, `~70` in `rfp`)
- Well `15` has the next largest distance from the joint distribution (`~200` in `gfp`, `~40` in `rfp`)
- Well `10` seems to stand out from the crowd as well, although more in `rfp` than in `gfp`
- Well `06` sees an interesting deviation from the joint distribution that increases quickly after the jump in temperature, but only in `rfp`

These figures quantify the distance between distributions, identifying interesting outliers specified above but also showing the general behavior of the shift in distributions due to temperature change

