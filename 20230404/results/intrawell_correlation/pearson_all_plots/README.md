## Folder contents
This folder contains the following figures, each plotting a set of measurements of each of measurements with x-values averaged in intervals of 10
- `pearson_all_10_no_start.png`

## Figure descriptions 
**Axes**

The `x-axis` describes time, in minutes, of the experiment
- This range has a minimum of ~600 mins (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the Pearson correlation between `rfp` and `gfp` measurements within a well
- This range is determined by the range in Pearson correlation values calculated between `rfp` and `gfp` for each well at each timestep

**Data**

The distributions of each of the following features in each well at each timestep
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)
  
**Plots**

The `colored lines` plot the behavior of Pearson correlation between `rfp` and `gfp` as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions are referenced, the Pearson correlation between the distributions of `rfp` and `gfp` in the well specified in the legend)
- ***Behavior** generally stable

## Observations
- The correlation between `rfp` and `gfp` in well `12` dips below the correlation of the others at `~1500 mins` when there is the first slight increase in temperature
- Wells `13` and `14` have similar behaviot shortly after `~2000 mins`
- The correlation in well `10` (the feedbacked well) follows that same trajectory but low until the slight decrease in temperature at `~3300 mins` when the correlation spikes
- The correlation in well `10` decreases again with the increase in temperature at `~3800 mins`, after which time it steatily increases
- There is a steep decrease in correlation at the end of the experiment as the temperature nears `39` degrees
- Well `12` stands out with the highest Pearson correlation (`~0.9`) after `~3300 mins`
- Well `14` momentarily sees a dip in correlation at `~3300 mins` until `~4000 mins`

Apart from the exceptions named above, Pearson correlation seems to be stable and high (above `0.7`) before and after the rise in temperature
