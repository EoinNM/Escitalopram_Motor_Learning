import os
import shutil
import glob
from variables.variables import *
from utils.utils import *

SPFT = '/data/pt_nro174_mri/SPFT/DATA/Assessment/'
DATA = '/NOBACKUP2/molloy/MOTORTASK/'
sessions = ['S1', 'S2', 'S3', 'S4', 'S5']

def copy_logs(population, population2, workspace, SPFT, DATA, days):

    for subject in population:
        #I/O
        log_path = os.path.join(SPFT, subject)
        base = os.path.join(DATA, subject, 'base')
        day1 = os.path.join(DATA, subject,  'day1')
        day7 = os.path.join(DATA, subject, 'day7')
        
        for session in sessions:
            for i in glob.glob(os.path.join(SPFT, subject, '*%s-SPFT_7T_Daily.log*' %(session))):
                if session == 'S1':
                    shutil.copy(i, base)
                elif session == 'S2':
                    shutil.copy(i, day1)
                elif session == 'S5':
                    shutil.copy(i, day7)
                    
        #rename to uniform .log
        log_base = os.path.join(DATA, subject, 'base')
        log_day1 = os.path.join(DATA, subject, 'day1')
        log_day7 = os.path.join(DATA, subject, 'day7')
        
        #rename baseline files
        for i in os.listdir(log_base):
            if i.endswith('log'):
                os.rename(str(os.path.join(log_base, i)),
                          str(os.path.join(log_base, 'base.log')))
                
        #rename day1 files
        for i in os.listdir(log_day1):
            if i.endswith('log'):
                os.rename(str(os.path.join(log_day1, i)),
                          str(os.path.join(log_day1, 'day1.log')))
                
        #rename day7 files
        for i in os.listdir(log_day7):
            if i.endswith('log'):
                os.rename(str(os.path.join(log_day7, i)),
                          str(os.path.join(log_day7, 'day7.log')))

copy_logs(population, population2, workspace, SPFT, DATA, days)
