import os
import pandas as pd
import numpy as np
from variables.variables import *
from utils.utils import *
import shutil

def copy_ondur_event(population, days):

    count = 0
    for subject in population:
        count += 1
	
    	for day in days:
            
            print 'copying files files now for %s. %s, %s' %(count, subject, day)
            lrn_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_learn.ons'%(day))
            smp_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_simple.ons'%(day))
            rst_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_rest.ons'%(day))
            rst_dur = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_rest.dur'%(day))
            new_loc = mkdir_path(os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/event_sim/', subject, day))
            
            shutil.copy(lrn_ons, new_loc)
            shutil.copy(smp_ons, new_loc)
            shutil.copy(rst_ons, new_loc)
            shutil.copy(rst_dur, new_loc)
            
    print 'All files now copied, moving onto creating event design durations'
            
copy_ondur_event(population, days)

def update_files(population, days):
    
    #Now edit those files so they refer to trial onsets of LRN and SMP only
    
    count = 0
    for subject in population:
        count += 1
        
        for day in days:
        
            lrn_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/event_sim/', subject, day, '%s_learn.ons'%(day))
            smp_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/event_sim/', subject, day, '%s_simple.ons'%(day))
            
            print 'Updating files now for the first trials - %s. %s, %s'%(count, subject, day)
            #Create onsets/durs for the first trials in each block
            #1 Onsets
            #A LRN Condition
            with open (lrn_ons, 'r') as lrn_ons_infile:
                lrn_ons_lines = lrn_ons_infile.readlines()
                with open(lrn_ons, 'w') as lrn_ons_outfile:
                    for num, line in enumerate(lrn_ons_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           lrn_ons_outfile.write(line)
            #B SMP Condition               
            with open (smp_ons, 'r') as smp_ons_infile:
                smp_ons_lines = smp_ons_infile.readlines()
                with open(smp_ons, 'w') as smp_ons_outfile:
                    for num, line in enumerate(smp_ons_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           smp_ons_outfile.write(line)
                           
update_files(population, days)