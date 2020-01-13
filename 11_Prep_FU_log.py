import os
from os import *
import shutil
import glob
from variables.variables import *
from utils.utils import *

log_dir = '/data/pt_nro174_mri/SPFT/DATA/FU/'

def copy_FU(population, FU_dir, motor, log_dir):
    
    count = 0
    for subject in population:
	count += 1
        log_data = os.path.join(log_dir, subject)
        dst_dir  = mkdir_path(os.path.join(motor, subject, 'foll'))
	
	print 'Copying log file now for %s. %s'%(count, subject)        
        for i in glob.glob(os.path.join(log_data, '*_S6-SPFT_7T_Daily.log')):
            shutil.copy(i, dst_dir)

        for i in os.listdir(dst_dir):
            if i.endswith('log'):
                os.rename(str(os.path.join(dst_dir, i)),
                          str(os.path.join(dst_dir, 'foll.log')))


copy_FU(population, FU_dir, motor, log_dir)
