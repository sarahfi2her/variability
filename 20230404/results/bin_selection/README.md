## Folder contents
This folder contains the following directories and files, where `*` indicates any of `area`, `gfp`, or `rfp`

#### `*_bin_entropies.csv`
**Columns**
- `entropies` (the entropy of the distribution `*`)
- `n_bins` (the number of bins over which the distribution `*` is discretized for entropy calculation)

**Rows**

Each row indicates (`entropies`, `n_bins`) for each `n_bins` that is a multiple of 10 in the range 
(minimum number of bins suggested by unsupervised binning methods for the distribution `*` , 
maximum number of bins suggested by unsupervised binning methods for the distribution `*`) 

#### `*_bin_entropies_methods.csv`
**Columns**
- `method` (the name of an unsupervised binning method)
- `n_bins` (the number of bins suggested by the corresponding `method` for discretizing distribution `*`)
- `entropy` (the entropy of distribution `*` when discretized with `n_bins`)

**Rows**

Each row indicates (`method`, `n_bins`, `entropy`) for one of the seven binning methods provided by `matplotlib.pyplot`

#### `*_optimal_bins.csv`
**Columns**
- `n_bins` (optimal number of bins for discretizing distribution `*`)
- `bin_edges` (a list of length `n_bins + 1` describing the optimal edges of bins for discretizing distribution `*`)

**Rows**

A single row indicates (`n_bins`, `bin_edges`) for the optimal, entropy-based, bin configuration for discretizing distribution `*`

#### `bin_entropies_plots/`
Description in [bin_entropies_plots/README.md]([https://github.com/sarahfi2her/variability/tree/main/20230404/results/bin_selection/bin_entropies_plots#readme])

#### `distribution_plots/`
Description in [distribution_plots/README.md]([https://github.com/sarahfi2her/variability/tree/main/20230404/results/bin_selection/distribution_plots#readme])


