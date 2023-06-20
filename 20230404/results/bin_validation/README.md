## Folder contents

This folder contains the following directories and files

#### `validation_mi.csv`

**Columns**

- `feature` (the feature of which values are sampled)
- `timestep` (the timestep from which values of the corresponding `feature` are sampled)
- `subset_size` (the number of values of the corresponding `feature` sampled from each well at the time corresponding to `timestep`)
- `mi` (the mutual information between the sampled subsets from each well)

**Rows**

Each row indicates (`feature`, `timestep`, `subset_size`, `mi`)
- for each `feature` (`gfp`, `rfp`, or `area`), 
- for each `timestep` (`51`, `101`, `151`, `201`, `251`, `301`, `351`, `401`), 
- and for each `subset_size` in the range `(1, the average number of cells in each well at timestep)`

#### `validation_mi_plots/`
Description in [validation_mi_plots/README.md](https://github.com/sarahfi2her/variability/tree/main/20230404/results/bin_validation/validation_mi_plots#readme)
