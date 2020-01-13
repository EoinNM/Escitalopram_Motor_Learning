import os
from utils.utils import *
from variables.variables import *

for subject in population:
    for day in days:
        
            mkdir_path(os.path.join('/NOBACKUP2/molloy', 'MOTORTASK_PARAMOD', subject, day))