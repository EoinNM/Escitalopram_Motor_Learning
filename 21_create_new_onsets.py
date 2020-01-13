import os
import pandas as pd
import numpy as np
from variables.variables import *
from utils.utils import *
import shutil

def copy_files(population, days):
    
    #Copy all the original onset, duration and score files to a new directory

    trial_types = ['first', 'second', 'third']
    conditions = ['rest', 'learn', 'simple']
    
    for subject in population:
        for day in days:
            for trial_type in trial_types:
                for con in conditions:
            
                    #define paths to all originally used onset & duration files
                    ons_path = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    ons = os.path.join(ons_path, '%s_%s.ons'%(day, con))
                    dur_path = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    dur = os.path.join(dur_path, '%s_%s.dur'%(day, con))

                    #create new dirst for each of first, second and last trials
                    new_loc = mkdir_path(os.path.join('/NOBACKUP2/molloy/', 'TRIAL_ONS_DURS', '%s'%(trial_type), subject, day))
                                
                    #copy the onset & duration files to each of the new locations:
                    #first the onsets               
                    shutil.copy(ons, new_loc)
                    #and now the durations
                    shutil.copy(dur, new_loc)
                    
                    #define paths to all originally used scores files
                    #1. Accuracy/Error Scores
                    ACC_LRN_path  = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    ACC_LRN       = os.path.join(ACC_LRN_path, '%s_%s.txt'%(subject, day))
                    ACC_SMP_path  = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    ACC_SMP       = os.path.join(ACC_SMP_path, '%s_%s_smp.txt'%(subject, day))
                    #2. RT Scores
                    RT_LRN_path   = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    RT_LRN        = os.path.join(RT_LRN_path, '%s_%s_RT_lrn.txt'%(subject, day))
                    RT_SMP_path   = os.path.join('/NOBACKUP2/molloy/MOTORTASK/', subject, day)
                    RT_SMP        = os.path.join(RT_SMP_path, '%s_%s_RT_SMP.txt'%(subject, day))
                    
                    #Copy the scores to the new dir also
                    shutil.copy(ACC_LRN, new_loc)
                    shutil.copy(ACC_SMP, new_loc)
                    shutil.copy(RT_LRN, new_loc)
                    shutil.copy(RT_SMP, new_loc)
                    
    print 'All files now copied successfully - Moving on to Updating files'            
                    
copy_files(population, days)

def update_files(population, days):
    
    #Now edit those files so they refer to 3 trials instead of single blocks of trials
    #1 Onsets & Durations
    
    count = 0
    for subject in population:
        count += 1
        
        for day in days:
        
            lrn_ons_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_learn.ons'%(day))
            lrn_dur_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_learn.dur'%(day))
            smp_ons_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_simple.ons'%(day))
            smp_dur_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_simple.dur'%(day))
            
            print 'Updating files now for the first trials - %s. %s, %s'%(count, subject, day)
            #Create onsets/durs for the first trials in each block
            #1 Onsets
            #A LRN Condition
            with open (lrn_ons_1, 'r') as lrn_ons_1_infile:
                lrn_ons_1_lines = lrn_ons_1_infile.readlines()
                with open(lrn_ons_1, 'w') as lrn_ons_1_outfile:
                    for num, line in enumerate(lrn_ons_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           lrn_ons_1_outfile.write(line)
            #B SMP Condition               
            with open (smp_ons_1, 'r') as smp_ons_1_infile:
                smp_ons_1_lines = smp_ons_1_infile.readlines()
                with open(smp_ons_1, 'w') as smp_ons_1_outfile:
                    for num, line in enumerate(smp_ons_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           smp_ons_1_outfile.write(line)
            #2 Durations
            #A LRN Condition
            with open (lrn_dur_1, 'r') as lrn_dur_1_infile:
                lrn_dur_1_lines = lrn_dur_1_infile.readlines()
                with open(lrn_dur_1, 'w') as lrn_dur_1_outfile:
                    for num, line in enumerate(lrn_dur_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           lrn_dur_1_outfile.write(line)
            #B SMP Condition               
            with open (smp_dur_1, 'r') as smp_dur_1_infile:
                smp_dur_1_lines = smp_dur_1_infile.readlines()
                with open(smp_dur_1, 'w') as smp_dur_1_outfile:
                    for num, line in enumerate(smp_dur_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           smp_dur_1_outfile.write(line)
                           
            #########################################################################################################

            lrn_ons_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_learn.ons'%(day))
            lrn_dur_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_learn.dur'%(day))
            smp_ons_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_simple.ons'%(day))
            smp_dur_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_simple.dur'%(day))

            print 'Updating files now for the second trials - %s. %s, %s'%(count, subject, day)
            #Create onsets/durs for the first trials in each block
            #1 Onsets
            #A LRN Condition
            with open (lrn_ons_2, 'r') as lrn_ons_2_infile:
                lrn_ons_2_lines = lrn_ons_2_infile.readlines()
                with open(lrn_ons_2, 'w') as lrn_ons_2_outfile:
                    for num, line in enumerate(lrn_ons_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           lrn_ons_2_outfile.write(line)
            #B SMP Condition               
            with open (smp_ons_2, 'r') as smp_ons_2_infile:
                smp_ons_2_lines = smp_ons_2_infile.readlines()
                with open(smp_ons_2, 'w') as smp_ons_2_outfile:
                    for num, line in enumerate(smp_ons_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           smp_ons_2_outfile.write(line)
            #2 Durations
            #A LRN Condition
            with open (lrn_dur_2, 'r') as lrn_dur_2_infile:
                lrn_dur_2_lines = lrn_dur_2_infile.readlines()
                with open(lrn_dur_2, 'w') as lrn_dur_2_outfile:
                    for num, line in enumerate(lrn_dur_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           lrn_dur_2_outfile.write(line)
            #B SMP Condition               
            with open (smp_dur_2, 'r') as smp_dur_2_infile:
                smp_dur_2_lines = smp_dur_2_infile.readlines()
                with open(smp_dur_2, 'w') as smp_dur_2_outfile:
                    for num, line in enumerate(smp_dur_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           smp_dur_2_outfile.write(line)
                           
           #########################################################################################################
           
            lrn_ons_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_learn.ons'%(day))
            lrn_dur_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_learn.dur'%(day))
            smp_ons_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_simple.ons'%(day))
            smp_dur_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_simple.dur'%(day))

            print 'Updating files now for the third trials - %s. %s, %s'%(count, subject, day)
            #Create onsets/durs for the third trials in each block
            #1 Onsets
            #A LRN Condition
            with open (lrn_ons_3, 'r') as lrn_ons_3_infile:
                lrn_ons_3_lines = lrn_ons_3_infile.readlines()
                with open(lrn_ons_3, 'w') as lrn_ons_3_outfile:
                    for num, line in enumerate(lrn_ons_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           lrn_ons_3_outfile.write(line)
            #B SMP Condition               
            with open (smp_ons_3, 'r') as smp_ons_3_infile:
                smp_ons_3_lines = smp_ons_3_infile.readlines()
                with open(smp_ons_3, 'w') as smp_ons_3_outfile:
                    for num, line in enumerate(smp_ons_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           smp_ons_3_outfile.write(line)
            #2 Durations
            #A LRN Condition
            with open (lrn_dur_3, 'r') as lrn_dur_3_infile:
                lrn_dur_3_lines = lrn_dur_3_infile.readlines()
                with open(lrn_dur_3, 'w') as lrn_dur_3_outfile:
                    for num, line in enumerate(lrn_dur_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           lrn_dur_3_outfile.write(line)
            #B SMP Condition               
            with open (smp_dur_3, 'r') as smp_dur_3_infile:
                smp_dur_3_lines = smp_dur_3_infile.readlines()
                with open(smp_dur_3, 'w') as smp_dur_3_outfile:
                    for num, line in enumerate(smp_dur_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           smp_dur_3_outfile.write(line)
                           
           #########################################################################################################
                           
            #2 Scores

            #Create parametric modulation values from behavioural scores for each trial in each early, middle and late learning conditions
            #First is the early trial:
            ACC_LRN_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_%s.txt'%(subject, day))
            ACC_SMP_1 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_%s_smp.txt'%(subject, day))
            RT_LRN_1  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_%s_RT_lrn.txt'%(subject, day))
            RT_SMP_1  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/first/', subject, day, '%s_%s_RT_SMP.txt'%(subject, day))
            
            print 'Updating files now for the first trial error & RT Scores - %s. %s, %s'%(count, subject, day)
            #A Error LRN
            with open (ACC_LRN_1, 'r') as ACC_LRN_1_infile:
                ACC_LRN_1_lines = ACC_LRN_1_infile.readlines()
                with open(ACC_LRN_1, 'w') as ACC_LRN_1_outfile:
                    for num, line in enumerate(ACC_LRN_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           ACC_LRN_1_outfile.write(line)
            #B Error SMP               
            with open (ACC_SMP_1, 'r') as ACC_SMP_1_infile:
                ACC_SMP_1_lines = ACC_SMP_1_infile.readlines()
                with open(ACC_SMP_1, 'w') as ACC_SMP_1_outfile:
                    for num, line in enumerate(ACC_SMP_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           ACC_SMP_1_outfile.write(line)
            #2 Durations
            #A RT LRN
            with open (RT_LRN_1, 'r') as RT_LRN_1_infile:
                RT_LRN_1_lines = RT_LRN_1_infile.readlines()
                with open(RT_LRN_1, 'w') as RT_LRN_1_outfile:
                    for num, line in enumerate(RT_LRN_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           RT_LRN_1_outfile.write(line)
            #B SMP Condition               
            with open (RT_SMP_1, 'r') as RT_SMP_1_infile:
                RT_SMP_1_lines = RT_SMP_1_infile.readlines()
                with open(RT_SMP_1, 'w') as RT_SMP_1_outfile:
                    for num, line in enumerate(RT_SMP_1_lines):
                        if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
                           RT_SMP_1_outfile.write(line)
                           
           #########################################################################################################

            #Second is the middle trial
            ACC_LRN_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_%s.txt'%(subject, day))
            ACC_SMP_2 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_%s_smp.txt'%(subject, day))
            RT_LRN_2  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_%s_RT_lrn.txt'%(subject, day))
            RT_SMP_2  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/second/', subject, day, '%s_%s_RT_SMP.txt'%(subject, day))
            
            print 'Updating files now for the second trial error & RT Scores - %s. %s, %s'%(count, subject, day)
            #A Error LRN
            with open (ACC_LRN_2, 'r') as ACC_LRN_2_infile:
                ACC_LRN_2_lines = ACC_LRN_2_infile.readlines()
                with open(ACC_LRN_2, 'w') as ACC_LRN_2_outfile:
                    for num, line in enumerate(ACC_LRN_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           ACC_LRN_2_outfile.write(line)
            #B Error SMP               
            with open (ACC_SMP_2, 'r') as ACC_SMP_2_infile:
                ACC_SMP_2_lines = ACC_SMP_2_infile.readlines()
                with open(ACC_SMP_2, 'w') as ACC_SMP_2_outfile:
                    for num, line in enumerate(ACC_SMP_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           ACC_SMP_2_outfile.write(line)
            #2 Durations
            #A RT LRN
            with open (RT_LRN_2, 'r') as RT_LRN_2_infile:
                RT_LRN_2_lines = RT_LRN_2_infile.readlines()
                with open(RT_LRN_2, 'w') as RT_LRN_2_outfile:
                    for num, line in enumerate(RT_LRN_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           RT_LRN_2_outfile.write(line)
            #B SMP Condition               
            with open (RT_SMP_2, 'r') as RT_SMP_2_infile:
                RT_SMP_2_lines = RT_SMP_2_infile.readlines()
                with open(RT_SMP_2, 'w') as RT_SMP_2_outfile:
                    for num, line in enumerate(RT_SMP_2_lines):
                        if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
                           RT_SMP_2_outfile.write(line)

           #########################################################################################################

            #Third is the last trial
            ACC_LRN_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_%s.txt'%(subject, day))
            ACC_SMP_3 = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_%s_smp.txt'%(subject, day))
            RT_LRN_3  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_%s_RT_lrn.txt'%(subject, day))
            RT_SMP_3  = os.path.join('/NOBACKUP2/molloy/TRIAL_ONS_DURS/third/', subject, day, '%s_%s_RT_SMP.txt'%(subject, day))
            
            print 'Updating files now for the third trial error & RT Scores - %s. %s, %s'%(count, subject, day)
            #A Error LRN
            with open (ACC_LRN_3, 'r') as ACC_LRN_3_infile:
                ACC_LRN_3_lines = ACC_LRN_3_infile.readlines()
                with open(ACC_LRN_3, 'w') as ACC_LRN_3_outfile:
                    for num, line in enumerate(ACC_LRN_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           ACC_LRN_3_outfile.write(line)
            #B Error SMP               
            with open (ACC_SMP_3, 'r') as ACC_SMP_3_infile:
                ACC_SMP_3_lines = ACC_SMP_3_infile.readlines()
                with open(ACC_SMP_3, 'w') as ACC_SMP_3_outfile:
                    for num, line in enumerate(ACC_SMP_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           ACC_SMP_3_outfile.write(line)
            #2 Durations
            #A RT LRN
            with open (RT_LRN_3, 'r') as RT_LRN_3_infile:
                RT_LRN_3_lines = RT_LRN_3_infile.readlines()
                with open(RT_LRN_3, 'w') as RT_LRN_3_outfile:
                    for num, line in enumerate(RT_LRN_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           RT_LRN_3_outfile.write(line)
            #B SMP Condition               
            with open (RT_SMP_3, 'r') as RT_SMP_3_infile:
                RT_SMP_3_lines = RT_SMP_3_infile.readlines()
                with open(RT_SMP_3, 'w') as RT_SMP_3_outfile:
                    for num, line in enumerate(RT_SMP_3_lines):
                        if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
                           RT_SMP_3_outfile.write(line)
                  
    print 'Done'
update_files(population, days)
