Analyzing phenotypic variability of yeast cells under stress

### Week 1 
#### Shannon entropy
- Shannon entropy, in information theory, measures the inherent randomness of a system, quantifying the number of possible states in which a variable could appear and the amount of information known about its possible outcomes
- As entropy increases, so does the uncertainty of the value of a measured random variable, leading to an increased number of possible states but a decrease in information inherent to its possible outcomes
- As entropy decreases, the number of possible states in which a variable could appear decreases, and thus the certainty about the value of that measurement increases along with the information known about it

Discrete Shannon entropy is calculated as follows, where each `pk` describes the probability that the random variable measured has the specified associated outcome:
> `-sum(pk * log(pk))`

In the case of this project, calculating the entropy of, say, GFP fluorescence in a single well at a single timestep is as follows:
- The GFP fluorescence of each pixel of each cell is measured
- The average of each of these pixel's measurements is calculated for each cell
- We find the distribution of the mean GFP fluorescence of all cells in the well
  - Note here that this distribution is a continuous one, or at least one that would not lead to the same arrangement of possible outcomes in every measurement
  - For this reason, we must select a set of bins in which the data can fall, each interval serving as one outcome (*The specific bin selection method used here will be detailed in a later section*)
- We find the discretized distribution of mean GFP fluorescence of all cells in the well
- The discrete Shannon entropy of a cell's GFP fluorescense in the well is calculated with the given formula, where each `pk` is calculated as follows:
> `(# of cells in the well whose GFP value falls in bin/interval k) / (total # of cells in the well)`

Joint Shannon entropy takes the a number of distributions of the same variable and combines them, measuring the Shannon entropy of the outcome of a variable that is randomly selected from any included distribution (*The significance of joint entropy will be detailed in a later section*)

The joint entropy of GFP fluoresence across all wells at a single timestep is as follows:
- The GFP fluorescence of each pixel of each cell is measured in all wells
- The average of each of these pixel's measurements is calculated for each cell in all wells
- Given the average number of cells in each well, we take a random sampling of cells from each well of the following sample size:
> `(average # of cells in each well) / (# of wells measured)`
- We find the discretized distribution of mean GFP fluorescence from each cell in this this hand-picked selection that is distributed across all measured wells
- The discrete Shannon entropy of a cell's GFP fluorescense randomly selected from any well is calculated with the given formula, where each `pk` is calculated as follows:
> `(# of hand-picked cells whose GFP value falls in bin/interval k) / (total # of cells sampled)`

#### Mutual information
- Mutual information measures the amount of dependence one random variable has on another, quantifying the amount of information that a set of measurements share
- Low mutual information measurements indicate variables that are independent from each other, that is, knowing the value of one variable provides little information as to the value of another
- High mutual information measurements indicate variables that are dependent, that is, knowing the valie of one variable provides lots of information as to the value of another

Mutual information is calculated as follows:
> `(joint Shannon entropy) - (mean Shannon entropy)`


