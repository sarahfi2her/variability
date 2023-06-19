## Folder contents
This folder contains the following figures, each plotting a set of measurements of the feature that corresponds to their name
- `area_distribution_330_bins.png`
- `gfp_distribution_410_bins.png`
- `rfp_distribution_410_bins.png`

## Figure descriptions
**Axes**

The `x-axis` describes the range in values of `area`, `gfp`, or `rfp`
- This range is determined by the minimum and maximum values of the specified feature

The `y-axis` describes the density of the population that falls into each histogram bucket
- This range is determined by the range in percentage of cells that fall into each bin

**Data**

The set of all measurements of one of the following features across all wells and timesteps
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

**Plots**

The `blue histogram` plots the distribution of the data
- ***(x, y)*** (value of the measurement, the percentage of cells that fall within the bucket interval)
- ***Behavior*** multimodal (`gfp`, `rfp`), Gaussian (`area`)

## Observations

Each histogram is a visualization of the distribution of data, descritized with its optimal number of bins
