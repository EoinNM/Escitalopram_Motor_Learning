import os
from variables.variables import *
from utils.utils import *

def make_new_paths(motor, population, days):
    
    for subject in population:
        for day in days:
    
            first = mkdir_path(os.path.join(motor, subject, day, 'WITHIN'))
            secon = mkdir_path(os.path.join(motor, subject, day, 'BETWEEN'))
            
make_new_paths(motor,population, days)
