#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 11:12:29 2018

@author: eoin
"""

import os
from os import *
from variables.variables import *
from utils.utils import *
import glob

def convert_dcm(population, zfs):
    
    count = 0
    for subject in population:
        count += 1
    
        print '================================================'
        print '%s. Converting dicoms for %s' %(count, subject)
        print '================================================'
    
        #I/O
        for images in glob.glob(os.path.join(zfs, subject, 'pres', '*.VER1', 'DICOM')):
            DICOMS = images
            
            nii_dir = mkdir_path(os.path.join(zfs, subject, 'pres', 'NII'))
        
            #read all dicoms
            all_dicoms = []
            for img in os.listdir(DICOMS):
                img = os.path.join(DICOMS, img)
                all_dicoms.append(img)
         
            #convert to nii
            os.system('dcm2niix -o %s %s' %(nii_dir, DICOMS))
        
            

convert_dcm(population, zfs)
        
