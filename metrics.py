#### imports ###################################################################

from library import (emd_fn, gini_coefficient_fn, knee_locator_fn, 
                         mutual_information_fn, pairs_from_list_fn, scale_fn,
                         shannon_entropy_fn, xy_from_dict_fn)
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#### class definition ##########################################################

class Bins():
    def __init__(self, pop_dict, interval=10,
                 methods=['fd', 'doane', 'scott', 'stone', 'rice', 'sturges', 
                            'sqrt']):
        self.pop_dict = pop_dict
        self.interval = interval
        self.methods = methods
        self.min_val = self.get_val(lambda x: min(x))
        self.max_val = self.get_val(lambda x: max(x))
        self.bin_width_dict = self.get_bin_width_dict()
        (self.n_list, self.bin_edges_dict, self.entropy_dict, 
         self.method_bin_dict) = self.get_n_list()
        self.n_bins = self.get_n_bins()
        self.bin_edges = self.get_bin_edges()
        self.ylim = self.get_ylim()
        
    def get_val(self, fn):
        vals = [fn(pop) for pop in self.pop_dict.values()]
        return fn(vals)

    def get_bin_width_dict(self):
        bin_width_dict = {}
        for m in self.methods:
            edges = [np.histogram(p, bins=m)[1] for p in self.pop_dict.values()]
            width = np.array([e[1]-e[0] for e in edges]).mean()
            bin_width_dict[m] = width
        return bin_width_dict
    
    def lo_bound(self, n):
        if n % 10 == 0: return n - 10
        return n - (n % 10)
        
    def hi_bound(self, n):
        return n + (10 - (n % 10))
    
    def get_n_list(self):
        method_bin_dict = {}
        for m in self.methods:
            method_bin_dict[m] = int((self.max_val-self.min_val)/
                                     self.bin_width_dict[m])
        n_list = [n for n in range(self.lo_bound(min(method_bin_dict.values())), 
                                   self.hi_bound(max(method_bin_dict.values()))
                                   +1) if n%10==0]
        entropy_dict = {}
        bin_edges_dict = {}
        for n in n_list:
            bin_edges = np.linspace(self.min_val, self.max_val, n+1)
            entropy = np.array([shannon_entropy_fn(self.pop_dict[t], bin_edges) 
                                for t in self.pop_dict]).mean()
            bin_edges_dict[n] = bin_edges
            entropy_dict[n] = entropy
        return (n_list, bin_edges_dict, entropy_dict, method_bin_dict)
    
    def get_n_bins(self):
        x, y = xy_from_dict_fn(self.entropy_dict)
        n_bins = knee_locator_fn(x, y)
        return n_bins

    def get_bin_edges(self):
        return np.linspace(self.min_val, self.max_val, self.n_bins+1)
    
    def get_ylim(self):
        return self.hi_bound(max([max(np.histogram(pop, bins=self.bin_edges)[0]) 
                                  for pop in self.pop_dict.values()]))
    
class EarthMoversDistance():
    def __init__(self, pop_dict, pop_dict_list):
        self.pop_dict = pop_dict
        self.pop_dict_list = pop_dict_list
        self.emd_dict = self.get_emd_dict()

    def get_emd_dict(self):
        emd_dict = {}
        for t in sorted(self.pop_dict.keys()):
            pop_list = [p_dict[t] for p_dict in self.pop_dict_list]
            subset_size = int(np.array([len(p) for p in pop_list]).mean()/
                              len(pop_list))
            if subset_size > 0:
                joint_pop = np.concatenate([np.random.choice(pop, subset_size) 
                                            for pop in pop_list])
                pop = self.pop_dict[t]
                emd_dict[t] = emd_fn(pop, joint_pop)
        return emd_dict
    
class EMDPairwise():
    def __init__(self, timestep_list, pop_dict_list, well_id_list):
        self.timestep_list = timestep_list
        self.pop_dict_list = pop_dict_list
        self.well_id_list = well_id_list
        self.pair_list = pairs_from_list_fn(np.arange(len(self.well_id_list)))
        self.emd_pair_dict = self.get_emd_pair_dict()
        self.emd_matrix_dict = self.get_emd_matrix_dict()

    def get_emd_pair_dict(self):
        emd_pair_dict = {}
        for n1, n2 in self.pair_list:
            w1 = self.well_id_list[n1]
            w2 = self.well_id_list[n2]
            emd_pair_dict[(w1, w2)] = {}
            for t in self.timestep_list:
                pop1 = self.pop_dict_list[n1][t]
                pop2 = self.pop_dict_list[n2][t]
                emd_pair_dict[(w1, w2)][t] = emd_fn(pop1, pop2)
        return emd_pair_dict
    
    def get_emd_matrix_dict(self):
        matrix_dict = {}
        for t in self.timestep_list:
            matrix = []
            for w1 in self.well_id_list:
                row = []
                for w2 in self.well_id_list:
                    if w1 < w2:
                        row.append(self.emd_pair_dict[(w1, w2)][t])
                    elif w2 < w1:
                        row.append(self.emd_pair_dict[(w2, w1)][t])
                    else:
                        row.append(0)
                matrix.append(row)
            matrix_dict[t] = matrix
        return matrix_dict

class Entropy():
    def __init__(self, pop_dict, bins):
        self.pop_dict = pop_dict
        self.bins = bins
        self.entropy_dict = self.get_entropy_dict()

    def get_entropy_dict(self):
        entropy_dict = {}
        for t in sorted(self.pop_dict.keys()):
            entropy_dict[t] = shannon_entropy_fn(self.pop_dict[t], self.bins)
        return entropy_dict

class GiniIndex():
    def __init__(self, pop_dict):
        self.timestep_list = sorted(pop_dict.keys())
        self.pop_dict = self.get_pop_dict(pop_dict)
        self.scaled_pop_dict = self.get_pop_dict()
        self.gini_dict = self.get_gini_dict()
        self.scaled_gini_dict = self.get_gini_dict(scaled=True)

    def get_pop_dict(self, pop_dict=[]):
        res_pop_dict = {}
        for t in self.timestep_list:
            if pop_dict == []:
                res_pop_dict[t] = scale_fn(self.pop_dict[t], [0, 100])
            else:
                res_pop_dict[t] = sorted(pop_dict[t])
        return res_pop_dict

    def get_gini_dict(self, scaled=False):
        gini_dict = {}
        for t in self.timestep_list:
            if scaled:
                gini_dict[t] = gini_coefficient_fn(self.scaled_pop_dict[t])
            else:
                gini_dict[t] = gini_coefficient_fn(self.pop_dict[t])
        return gini_dict

class MutualInfoInterwell():
    def __init__(self, timestep_list, all_well_pop_dict, bin_edges):
        self.timestep_list = timestep_list
        self.all_well_pop_dict = all_well_pop_dict
        self.bin_edges = bin_edges
        self.subset_size_dict, self.pop_list_dict = self.get_timestep_dicts()
        self.mi_dict = self.get_mi_dict()
        self.start_timestep = self.get_start_timestep()

    def get_timestep_dicts(self):
        subset_size_dict = {}
        pop_list_dict = {}
        for t in self.timestep_list:
            if t == len(self.timestep_list):
                pop_list = [self.all_well_pop_dict[n] 
                            for n in self.all_well_pop_dict 
                            if n%len(self.timestep_list)==0]
            else:
                pop_list = [self.all_well_pop_dict[n] 
                            for n in self.all_well_pop_dict 
                            if n%len(self.timestep_list)==t]
            subset_size = int(np.array([len(p) for p in pop_list]).mean()/
                              len(pop_list))
            pop_list_dict[t] = pop_list
            subset_size_dict[t] = subset_size
        return subset_size_dict, pop_list_dict
    
    def get_mi_dict(self):
        mi_dict = {}
        for t in self.timestep_list:
            if self.subset_size_dict[t] > 0:
                mi = mutual_information_fn(self.pop_list_dict[t],
                                           self.subset_size_dict[t], 
                                           self.bin_edges)
                mi_dict[t] = mi
        return mi_dict
            
    def get_start_timestep(self):
        start = None
        for t in self.timestep_list:   
            if start == None and self.subset_size_dict[t] > 30:
                start = t
        return start
        
class MutualInfoPairwise():
    def __init__(self, timestep_list, all_well_pop_dict, well_id_list, 
                 bin_edges):
        self.timestep_list = timestep_list
        self.all_well_pop_dict = all_well_pop_dict
        self.well_id_list = well_id_list
        self.bin_edges = bin_edges
        self.pair_list = pairs_from_list_fn([i for i in 
                                             range(len(self.well_id_list))])
        self.mi_pair_dict = self.get_mi_pair_dict()
        self.mi_matrix_dict = self.get_mi_matrix_dict()

    def get_timestep_dicts(self, w1, w2):
        subset_size_dict = {}
        pop_list_dict = {}
        for t in self.timestep_list:
            if t == len(self.timestep_list):
                pop_list = [self.all_well_pop_dict[n] 
                            for n in self.all_well_pop_dict 
                            if n%len(self.timestep_list)==0]
            else:
                pop_list = [self.all_well_pop_dict[n] 
                            for n in self.all_well_pop_dict 
                            if n%len(self.timestep_list)==t]
            pop_list = [pop_list[w1], pop_list[w2]]
            subset_size = int(np.array([len(p) for p in pop_list]).mean()/
                              len(pop_list))
            pop_list_dict[t] = pop_list
            subset_size_dict[t] = subset_size
        return subset_size_dict, pop_list_dict
    
    def get_mi_dict(self, subset_size_dict, pop_list_dict):
        mi_dict = {}
        for t in self.timestep_list:
            if subset_size_dict[t] > 0:
                mi = mutual_information_fn(pop_list_dict[t],
                                           subset_size_dict[t], 
                                           self.bin_edges)
                mi_dict[t] = mi
        return mi_dict

    def get_mi_pair_dict(self):
        mi_pair_dict = {}
        for w1, w2 in self.pair_list:
            subset_size_dict, pop_list_dict = self.get_timestep_dicts(w1, w2)
            mi_dict = self.get_mi_dict(subset_size_dict, pop_list_dict)
            mi_pair_dict[(self.well_id_list[w1], 
                          self.well_id_list[w2])] = mi_dict
        return mi_pair_dict
    
    def get_mi_matrix_dict(self):
        matrix_dict = {}
        for t in self.timestep_list:
            matrix = []
            for w1 in self.well_id_list:
                row = []
                for w2 in self.well_id_list:
                    if w1 < w2:
                        row.append(self.mi_pair_dict[(w1, w2)][t])
                    elif w2 < w1:
                        row.append(self.mi_pair_dict[(w2, w1)][t])
                    else:
                        row.append(0)
                matrix.append(row)
            matrix_dict[t] = matrix
        return matrix_dict
            
################################################################################
