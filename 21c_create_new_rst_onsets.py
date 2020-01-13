import os
import pandas as pd
import numpy as np
from variables.variables import *
from utils.utils import *
import shutil

trial_types = ['first', 'second', 'third']

def copy_rst(population, days):

    count = 0
    for subject in population:
        count += 1
	
	for day in days:
		for trial_type in trial_types:

			print 'copying RST files now for %s. %s, %s' %(count, subject, day)
			rst_ons = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_rest.ons'%(day))
			rst_dur = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/MOTORTASK/', subject, day, '%s_rest.dur'%(day))
			new_loc = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/', trial_type, subject, day)
	
			shutil.copy(rst_ons, new_loc)
			shutil.copy(rst_dur, new_loc)
            
copy_rst(population, days)

def update_rst(population, days):

    count = 0
    for subject in population:
        count += 1
	
    	for day in days:

			print 'Updating files now for the first trials - %s. %s, %s'%(count, subject, day)
			rst_ons_1 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/first/', subject, day, '%s_rest.ons'%(day))
			rst_dur_1 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/first/', subject, day, '%s_rest.dur'%(day))
		
			#Create onsets/durs for the first trials in each block
			#1 Onsets
			with open (rst_ons_1, 'r') as rst_ons_1_infile:
			    rst_ons_1_lines = rst_ons_1_infile.readlines()
			    with open(rst_ons_1, 'w') as rst_ons_1_outfile:
				for num, line in enumerate(rst_ons_1_lines):
				    if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
				       rst_ons_1_outfile.write(line)
		
			#2 Durations
			with open (rst_dur_1, 'r') as rst_dur_1_infile:
			    rst_dur_1_lines = rst_dur_1_infile.readlines()
			    with open(rst_dur_1, 'w') as rst_dur_1_outfile:
				for num, line in enumerate(rst_dur_1_lines):
				    if num == 0 or num == 3 or num == 6 or num == 9 or num == 12:
				       rst_dur_1_outfile.write(line)

			print 'Updating files now for the second trials - %s. %s, %s'%(count, subject, day)
			rst_ons_2 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/second/', subject, day, '%s_rest.ons'%(day))
			rst_dur_2 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/second/', subject, day, '%s_rest.dur'%(day))

			#Create onsets/durs for the third trials in each block
			#1 Onsets
			with open (rst_ons_2, 'r') as rst_ons_2_infile:
			    rst_ons_2_lines = rst_ons_2_infile.readlines()
			    with open(rst_ons_2, 'w') as rst_ons_2_outfile:
				for num, line in enumerate(rst_ons_2_lines):
				    if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
				       rst_ons_2_outfile.write(line)
		
			#2 Durations
			with open (rst_dur_2, 'r') as rst_dur_2_infile:
			    rst_dur_2_lines = rst_dur_2_infile.readlines()
			    with open(rst_dur_2, 'w') as rst_dur_2_outfile:
				for num, line in enumerate(rst_dur_2_lines):
				    if num == 1 or num == 4 or num == 7 or num == 10 or num == 13:
				       rst_dur_2_outfile.write(line)

			print 'Updating files now for the third trials - %s. %s, %s'%(count, subject, day)
			rst_ons_3 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/third/', subject, day, '%s_rest.ons'%(day))
			rst_dur_3 = os.path.join('/NOBACKUP2/molloy/MOTORTASK/MOTORTASK_DATA_ANALYSES/TRIAL_ONS_DURS/third/', subject, day, '%s_rest.dur'%(day))

			#Create onsets/durs for the third trials in each block
			#1 Onsets
			with open (rst_ons_3, 'r') as rst_ons_3_infile:
			    rst_ons_3_lines = rst_ons_3_infile.readlines()
			    with open(rst_ons_3, 'w') as rst_ons_3_outfile:
				for num, line in enumerate(rst_ons_3_lines):
		                    if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
				       rst_ons_3_outfile.write(line)
		
			#2 Durations
			with open (rst_dur_3, 'r') as rst_dur_3_infile:
			    rst_dur_3_lines = rst_dur_3_infile.readlines()
			    with open(rst_dur_3, 'w') as rst_dur_3_outfile:
				for num, line in enumerate(rst_dur_3_lines):
		                    if num == 2 or num == 5 or num == 8 or num == 11 or num == 14:
				       rst_dur_3_outfile.write(line)

update_rst(population, days)
