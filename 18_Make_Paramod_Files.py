import os
import pandas as pd
import numpy as np
from variables.variables import *
from utils.utils import *

day7 = os.path.join('/NOBACKUP2/molloy/SPFT/Parametric_Modulation/RT/Paramod_SMP/', 'day7_SMP.csv')
df_day7 = pd.read_csv(day7, index_col = 0) 

for c in df_day7.columns:
    day7 = mkdir_path(os.path.join('/NOBACKUP2/molloy/SPFT/Parametric_Modulation/RT/Paramod_SMP/day7_SMP/'))
    os.chdir(day7)
    df_day7[c].to_csv(c + '_day7_RT_SMP.txt', index = False, header = False)
