## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature at the time point that corresponds to their name 
- `gfp_lorenz_combined_1000.png`
- `gfp_lorenz_combined_5000.png`
- `rfp_lorenz_combined_1000.png`
- `rfp_lorenz_combined_5000.png`

## Figure descriptions
**Axes**

The `x_axis` describes the cumulative proportion of the population
- This ranges from `0.0` to `1.0`

The `y_axis` described the cumulative proportion of the feature of interest
- This ranges from `0.0` to `1.0`

**Data**

The distributions of each of the following features in each well at the specified timestep
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `grey line` plots the behavior of the Lorenz curve for a perfectly evenly distributed population
- Populations whose Lorenz curve see that 50% of the population possesses exactly 50% of the feature value

The `colored line` (`green` in graphs of `gfp`, `red` in graphs of `rfp`) plot the behavior of the Lorenz curve
- ***(x, y)*** (percentage of the population, percentage of feature value that is distributed amongst that percentage of the population)

## Observations
The closer a distribution falls to a line with a slope of `1`, the more evenly distributed the feature of interest is amongst its population.
 
When examining the two `rfp` Lorenz plots, we see that, although the curve is slightly deeper at  `5000 mins` than at `1000 mins`, that the distribution of `rfp` is
quite even, and that there is no subset of cells overly expressing `rfp`. 

When examining the two `gfp` Lorenz plots, the same bahavior is observed with slightly deeper curves than in the plots of `rfp` at the same time steps. 

Regargless, these plots show an impressively even distribution of `rfp` and `gfp` that remain evenly distributed throughout the course of the experiment. 
