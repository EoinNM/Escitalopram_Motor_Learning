import os
from os import *
import shutil
from variables.variables import *
from utils.utils import *

new = '/data/pt_nro174_mri/NOBACKUP_BACKEDUP/REST/'

def move_RS(population, ZFS_fMRI, rest, days):
    
    for subject in population:
        for day in days:
            #I/O
            src_rst  = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'rest')
            src_ana  = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'rest_anatomical')
            dst_rst = os.path.join(new, subject, day, 'rest')
	    rest_ana = os.path.join(new, subject, day)
            #Copy
            shutil.move(src_rst, dst_rst)
            shutil.move(src_ana, rest_ana)
            
move_RS(population, ZFS_fMRI, rest, days)
