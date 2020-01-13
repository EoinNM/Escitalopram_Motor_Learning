#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:58:55 2018

@author: molloy

Copy Field Maps and Rename
"""

import os
from os import *
from variables.variables import *
from utils.utils import *
import shutil
import glob

def field_maps(population, workspace, days):
    
    count = 0
    for subject in population:
        count +=1
        for day in days:
            
            
            print '=================================================='
            print '%s. Moving and Renaming Field Maps for %s, %s' %(count, subject, day)
            print '=================================================='
            
            #I/O
            field_maps_src = os.path.join(mri_temp, subject, day)
            Phase_dir = mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'field_maps', 'Phase'))
            Mag_dir = mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'field_maps', 'Mag'))
            
            
            for magnitude_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_12.nii')):
                Mag_src = magnitude_map
                os.system('cp %s %s' %(Mag_src, Mag_dir))
                
            for phase_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_13.nii')):
                Phase_src = phase_map
                os.system('cp %s %s' %(Phase_src, Phase_dir))
                
            for file in os.listdir(Mag_dir):
                if file.endswith('.nii'):
                    os.rename(str(os.path.join(Mag_dir, file)),
                              str(os.path.join(Mag_dir, 'MAGNITUDE.nii')))
                
            for file in os.listdir(Phase_dir):
                if file.endswith('.nii'):
                    os.rename(str(os.path.join(Phase_dir, file)),
                              str(os.path.join(Phase_dir, 'PHASE.nii')))

            
field_maps(population, workspace, days)
                
            
            
            