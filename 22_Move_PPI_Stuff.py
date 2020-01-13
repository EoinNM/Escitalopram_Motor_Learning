import os
from variables.variables import *
from utils.utils import *
import glob
import shutil

def move_ppi(population_FULL, days):

    for subject in population_FULL:
            for day in days:
                
                dir_loc = '/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_Blocks/'
                dst_loc = '/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/PPI_Files_From_57_Sample/'
    
                #IO
                src = glob.glob(os.path.join(dir_loc, subject, day, 'VOI*'))
                dst = mkdir_path(os.path.join(dst_loc, subject, day))
                
                print src

move_ppi(population_FULL, days)