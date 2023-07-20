#### imports ###################################################################

import copy
import glob
import pandas as pd

#### class definition ##########################################################

class Experiment():
    def __init__(self, number, colors=[]):
        self.number = number
        self.colors = colors
        self.fpath = f'data_proc/{self.number}/'
        self.well_id_list = self.get_well_id_list()
        self.well_dict = self.get_well_dict()
        self.timestep_list = self.get_timestep_list()
        self.elapsed_dict = self.get_timestep_dict('elapsed')
        self.temp_dict = self.get_timestep_dict('temp')
        self.gfp_pop_dict = self.get_gfp_pop_dict()
        self.all_well_gfp_pop_dict = self.get_all_well_gfp_pop_dict()

    def get_well_id_list(self):
        file_list = sorted(glob.glob(f'{self.fpath}*.csv'))
        well_id_list = [f[len(self.fpath):len(self.fpath)+2] for f in file_list]
        return well_id_list
    
    def get_well_dict(self):
        well_dict = {}
        if self.colors != []:
            for well, color in zip(self.well_id_list, self.colors):
                well_dict[well] = Well(self.number, well, color)
        else:
            for well in self.well_id_list:
                well_dict[well] = Well(self.number, well)
        return well_dict
    
    def get_timestep_list(self):
        ref = self.well_dict[self.well_id_list[0]]
        return copy.deepcopy(ref.timestep_list)

    def get_timestep_dict(self, feature):
        feature_dict = {}
        ref = self.well_dict[self.well_id_list[0]]
        for t in self.timestep_list:
            val = list(ref.df.loc[ref.df['timestep'] == t][feature])[0]
            feature_dict[t] = val
        return feature_dict 

    def get_gfp_pop_dict(self):
        pop_dict = {}
        for t in self.timestep_list:
            pop_list = []
            for w in self.well_dict.values():
                pop_list.extend(copy.deepcopy(w.gfp_pop_dict[t]))
            pop_dict[t] = pop_list
        return pop_dict
    
    def get_all_well_gfp_pop_dict(self):
        all_well_pop_dict = {}
        for i, well in enumerate(self.well_id_list):
            pop_list = list(self.well_dict[well].gfp_pop_dict.values())
            for j, pop in enumerate(pop_list):
                all_well_pop_dict[i*len(pop_list) + j] = pop
        return all_well_pop_dict
            
    
class Well():
    def __init__(self, experiment_number, number, color='grey'):
        self.experiment_number = experiment_number
        self.number = number
        self.color=color
        self.fpath = f'data_proc/{self.experiment_number}/{self.number}.csv' 
        self.df = pd.read_csv(self.fpath)
        self.timestep_list = sorted(set(self.df['timestep']))
        self.gfp_pop_dict = self.get_pop_dict('gfp')

    def get_pop_dict(self, feature):
        pop_dict = {}
        for t in self.timestep_list:
            pop = list(self.df.loc[self.df['timestep'] == t][feature])
            pop_dict[t] = pop
        return pop_dict
    
################################################################################
