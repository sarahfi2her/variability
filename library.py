#### imports ###################################################################

from copy import copy
from kneed import KneeLocator
import numpy as np
from scipy.stats import entropy, wasserstein_distance

#### function declaration ######################################################

def emd_fn(old_pop, new_pop):
    return wasserstein_distance(old_pop, new_pop)

def gini_coefficient_fn(l):
    total = 0
    for i, xi in enumerate(l):
        l_copy = copy(l)
        l_copy.pop(i)
        total += np.sum(np.abs(xi - np.array(l_copy)))
    return total / (2*len(l)*sum(l))

def pairs_from_list_fn(l):
    pairs = [(item1, item2) for i, item1 in enumerate(l) for item2 in l[i + 1:]]
    return pairs

def knee_locator_fn(x, y, curve='concave', direction='increasing'):
    knee_locator = KneeLocator(x, y, curve=curve, direction=direction)
    return knee_locator.knee

def labelx_from_dict_fn(labelx_dict):
    label_unordered = list(labelx_dict.keys())
    x_unordered = [labelx_dict[key] for key in label_unordered]
    label_ordered = [label for _, label in 
                     sorted(zip(x_unordered, label_unordered))]
    x_ordered = sorted(x_unordered)
    return label_ordered, x_ordered

def xy_from_dict_fn(xy_dict):
    x = sorted(xy_dict.keys())
    y = [xy_dict[key] for key in x]
    return x, y

def scale_fn(old, new):
    if old == []: return old
    old_range = float(max(old)) - float(min(old))
    new_range = float(max(new)) - float(min(new))
    scaled = [(((val - min(old)) / old_range) * new_range + min(new)) 
                for val in old]
    return scaled

def shannon_entropy_fn(population, bins):
    hist, _ = np.histogram(population, bins=bins, density=True)
    hist = hist[hist > 0]
    return entropy(hist)

def mutual_information_fn(pop_list, subset_size, bins):
    joint_pop = np.concatenate([np.random.choice(pop, subset_size) 
                                for pop in pop_list])
    joint_e = shannon_entropy_fn(joint_pop, bins)
    avg_e = np.array([shannon_entropy_fn(pop, bins) for pop in pop_list]).mean()
    mi = joint_e - avg_e
    return mi

################################################################################
