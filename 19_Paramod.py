import os
import pandas as pd
import numpy as np
from variables.variables import *
from utils.utils import *
import shutil


def copy_paramods(population, motor, days):
    
    count = 0
    for subject in population:
        count += 1
        for day in days:

	    print '%s. copying files now for %s, %s' %(count,subject, day)
            
	    #1 RT SMP
            src_path_rt_smp = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_PARAMOD/NEW_2019/paramod_files/syn/smp/', '%s'%(day))
            src_rt_smp = os.path.join(src_path_rt_smp, '%s_RT_SMP_%s.txt'%(subject, day))
            dst_rt_smp = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_Blocks/', subject, day)
            shutil.copy(src_rt_smp, dst_rt_smp)
	    #2 RT LRN
	    src_path_rt_lrn = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_PARAMOD/NEW_2019/paramod_files/syn/lrn/', '%s'%(day))
            src_rt_lrn = os.path.join(src_path_rt_lrn, '%s_RT_LRN_%s.txt'%(subject, day))
            dst_rt_lrn = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_Blocks/', subject, day)
            shutil.copy(src_rt_lrn, dst_rt_lrn)
	    #3 Error SMP
	    src_path_error_smp = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_PARAMOD/NEW_2019/paramod_files/error/smp/', '%s'%(day))
            src_error_smp = os.path.join(src_path_error_smp, '%s_Error_SMP_%s.txt'%(subject, day))
            dst_error_smp = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_Blocks/', subject, day)
            shutil.copy(src_error_smp, dst_error_smp)
	    #4 Error LRN
            src_path_error_lrn = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_PARAMOD/NEW_2019/paramod_files/error/lrn/', '%s'%(day))
            src_error_lrn = os.path.join(src_path_error_lrn, '%s_Error_LRN_%s.txt'%(subject, day))
            dst_error_lrn = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA/MOTORTASK_Blocks/', subject, day)
            shutil.copy(src_error_lrn, dst_error_lrn)
            
copy_paramods(population, motor, days)
