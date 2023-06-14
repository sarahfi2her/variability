Analyzing phenotypic variability of yeast cells under stress

## Shannon entropy
Shannon entropy, in information theory, measures the uncertainty, or `information`, inherent to a random variable's outcome, quantifying in combination the number of states in which a variable can appear and the probabilities with which it does so
- A variable with low entropy appears in few states with a high probability, making the certainty of the value of the measurement high
- A variable with high entropy appears in many states with equally low probabilities, making the certainty of the value of the measurement low

The value of a variable's entropy is a measurement in units of `bits` 
- A single `bit` measures the entropy of a binary variable that has two equally accessible states, that is, the entropy of a single coin toss

The entropy of a variable is bound by `0 bits` and `log2(M) bits`, where `M` is the number of states in which the variable can appear
- A variable whose outcome is always certain will have an entropy of `0 bits`
- A variable whose outcome is equally likely to appear in any of its `M` accessible states will have an entropy of `log2(M) bits`
- Generally, a variable whose outcome is restricted to fewer states with higher probabilities will have a lower entropy than a variable whose outcome can appear in many states without favoring any of them

Discrete Shannon entropy is calculated as follows, where each `pk` describes the probability that the random variable measured will fall have an outcome in state `k`:
> `- (sum over all k)(pk * log2(pk))`

- For a variable whose outcome is equally likely to appear in any of its `M` states, `pk` is `1/M` for each state `k`
- For a variable whose outcome is not equally likely across all states, each `pk` is calculated as follows
> `(# of measurements of the variable in state k) / (total # of measurements of the variable)`

- The sum of all `pk` is always `1`

Suppose you are given a series of many measurements (*taken on a continuous scale*) and asked to calculate the entropy of the set
- Simply put, with how much certainty can we predict the value of a randomly selected measurement?

To put this in the context of the Shannon entropy equation we've introduced, we must define a few parameters:
- `M`, the number of states in which a measurement can appear
- `P`, the probability distribution of all measurements such that `P = (the set of all pk) = {p1, p2, ..., pM}`

Naively, we could consider `M` to be the set measurements gathered, and `P` to be the corresponding normalized set that counts the number of times that a given measurement appears (*although this would be a really, really bad idea*)
- Each `pk` would be really, really small
     - Since there are a practically infinite number of measurements in a continuous data range, it would be safe to assume that no more than a few measurements were the same
     - Then, we could assume that nearly all measurements would have a really, really small `pk` 
- All `pk` would be really, really similar
    - If each `pk` were really, really small, then they would vary, on average, by some really, really small amount
    - Then, all measurements are practically evenly distributed across all states
- Not every possible state would be accounted for
    - In theory, you could measure values that look like `0.000001`, `0.000002`, `0.000003`, and so on, but it is impossible that all of these practically infinite number of measurements exist in a finite set
    - The calculated entropy of this set would not be robust enough to account for any measurement that is not included in `M`

Given what we know about entropy, it is safe to say that these really, really small and similar probabilities across a really, really large number of states would produce a really, really high entropy that isn't even robust enough to account for all necessary conditions

A solution to this problem does the following
- Increases the size of the average `pk`
- Increases the deviation from the average `pk` (*assuming that the distribution isn't constant*)
- Accounts for all possible states
- Does this by decreasing the number of states, a method called `binning`

## Binning

Now that we know we must discretize our continuous numerical samplings, there remains a question of what method is best for doing it

**Unsupervised non-dynamic binning** is a process of categorizing data without optimization specialized to the desired output, producing a set of intervals equal in width 
- Given a number of bins `x`, the maximum possible value `max`, and the minimum possible value `min`, the `equal-width` method will calculate bin intervals as follows
> `[min, min+w), [min+w, min+2w), [min+2w, min+3w), ... [min+(x-1)w, max]`, where `w = (max - min)/x`
- Given a total number of measurements `n`, the `square-root` method will calculate `equal-width` bins, where `w` is defined as follows 
> `sqrt(n)`
    - Optimal only in speed and simplicity
- Given a total number of measurements `n`, the `rice` method will calculate `equal-width` bins, where `w` is defined as follows 
> `2 * (cube root of n)`
    - Commonly overestimates number of bins required, as it does not take variability into account 
- Given a total number of measurements `n`, the `sturges` method will calculate `equal-width` bins, where `w` is defined as follows 
> `log2(n)+1`
    - Only optimal for normal distributions of data, as it underestimates number of bins for large non-Gaussian datasets
- The `doane` method is a modification of the `sturges` method, adding a factor of `k` to `w`, where `k` is defined as follows
> `1 + ( (3*(mean-median)/(std)) / sqrt( (6(n-2))/((n+1)(n+3)) ) )`
    - An improved version of `sturges`, working better with non-normal datasets
- Given a total number of measurements `n` and an ordered distribution of measurements `M`, the `fd` method will calculate `equal-width` bins, where `w` is defined as follows
> `2 * ( ((median of values above median) - (median of values below median)) / (cube root of n) )`
    - Resilient to outliers, accounts for data variability and data size
- Given a total number of measurements `n` and a distribution of measurements `M`, the `scott` method will  `equal-width` bins, where `w` is defined as follows
> `(3.49 * phi(M)) / (cube root of n)`
    - Less resilient to outliers, accounts for data variability and data size
- The `stone` method uses a leave-one-out cross-validation estimate of the integrated squared error of a set of measurements 
    - Regarded as a generalization of the `scott` method
- The `auto` binning method uses the bin edges of whichever of the `sturges` and `fd` methods produces more bins 

**Unsupervised dynamic binning** is a process of categorizing data without optimization specialized to the desired output but producing an optimal set of intervals unequal in width
- The Bayesian `block` method manipulates bin edges until its fitness function, depending on the width of each block and the number of data points within each block, is optimized
    -  Extract signals to identify where statistical fluctuations are important, minimizing bins that have a wide distribution within them
    
**Supervised non-dynamic binning** is a process of categorizing data entries that does optimize to the desired output
- The `entropy-based` method is optimized to find the number of bins at which point there is a maximal information gain, with steps described as follows
    1. Calculate the entropy of the set of data for different numbers of bins
    2. Find the location at which the rise entropy becomes optimal (the knee)

The approach that we use for calcualting a bin configuratoin is described as follows
