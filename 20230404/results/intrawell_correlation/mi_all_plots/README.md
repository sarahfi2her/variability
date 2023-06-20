## Folder contents
This folder contains the following figures, each plotting a set of measurements with x-values averaged in intervals of 10
- `mi_all_10_no_start.png`
  
## Figure descriptions
**Axes**

The `x-axis` describes time, in minutes, of the experiment
- This range has a minimum of `~600 mins` (the time in which all wells have at least 50 cells) and a maximum determined by length of the experiment

The `y-axis` describes the mutual information between `rfp` and `gfp` measurements within a well
- This range is determined by the range in mutual information values calculated between `rfp` and `gfp` for each well at each timestep

**Data**

The distributions of each of the following features in each well at each timestep
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)
  
**Plots**

The colored lines plot the behavior of mutual information between `rfp` and `gfp` as a function of time
- ***(x, y)*** (the time in the experiment at which the distributions are referenced, the mutual information between the distributions of `rfp` and `gfp` in the well specified in the legend)
- ***Behavior*** slightly positive slope

## Observations
- The mutual information between `rfp` and `gfp` in well `03` sees a peak at the first small increase in temperature at `~1500 mins`
- The mutual information in well `07` sees a peak shortly after the increase in temperature at `~2200 mins`, with wells `06` and `03` following shortly behind
- It seems that the increase in temperature between `2000 mins` and `3000 mins` allows a range of increased mutual informations to be assumed (that is, more distinct distributions of `rfp` and `gfp`)
- Well `06` seems to assume the highest mutual information in comparison to the other wells
- Well `14` has the highest slope if increased mutual information after the small increase in temperature at `~3800 mins`
- Wells `12`, `15`, and `13` have a mutual information that remains low and stable
- Most wells (except well `12`) see an increase in mutual information at the end of the experiment as the temperature nears `39 degrees`

Except for the above names exceptions, the mutual information seems to be steadily increasing with a small slope (that is, the distributions of `rfp` and `gfp` become more distinct) throughout the course of the experiment


