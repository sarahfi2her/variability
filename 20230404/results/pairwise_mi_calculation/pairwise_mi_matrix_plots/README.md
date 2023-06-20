## Folder contents
This folder contains the following figures, each plottinf a set fo measurements of the feature and time that corresponds to their name
- `area_1000_pairwise_mi_matrix.png`
- `area_5000_pairwise_mi_matrix.png`
- `gfp_1000_pairwise_mi_matrix.png`
- `gfp_5000_pairwise_mi_matrix.png`
- `rfp_1000_pairwise_mi_matrix.png`
- `rfp_5000_pairwise_mi_matrix.png`

## Figure descriptions 
Each matrix features indices that correspond to each well (`01`, `03`, `04`, `05`, `06`, `07`, `08`, `10`, `11`, `12`, `13`, `14`, `15`), and a colorbar that indicates the color scale for the pairwise mutual information value between them 

**Data**

The distribution of measurements of the following feaures from each well at each timestep
- area of a cell (`area`)
- mean gfp across all pixels in a cell (`gfp`)
- mean rfp across all pixels in a cell (`rfp`)

## Observations
As in most analyses, `area` pairwise mutual information matrices have no insights, given that there is no trend in its behavior 

The following can be observed in the pairwise matrices of `gfp`
- At `1000 mins`, before any change in temperature, there are few pairs of wells with significant mutual information, but notes can be made of pairs (`01, 07`), (`01, 09`), (`06, 07`), (`06, 09`), (`06, 13`), and (`09, 13`)
- At `5000 mins`, after the large change in temperature, this regime shifts to reveal wells `01`, `03`, `14`, and `15` that share high mutual information with all other wells, while the other wells have low mutual information with one another

The following can be observed in the pairwise matrices of `rfp`
- At `1000 mins`, before any change in temperature, there are, again, few pairs of wells with significant mutual information, but notes can be made of pairs (`05, 07`), (`05, 09`), (`05, 10`), (`06, 07`), (`06, 09`), and (`06, 10`)
- At `5000 mins`, after the large change in temperature, this regime shifts in a way similar to `gfp` to reveal wells `01`, `03`, `14`, and `15` that share high mutual information with all other wells (except the pair (`03, 14`)), while the other wells have low mutual information with one another

`gfp` and `rfp` behave similarly, indicating that wells `01`, `03`, `14`, and `15` are apart from the rest of the pack of distributions

  
