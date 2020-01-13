#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 08:29:54 2018

@author: eoin
"""

import os
from os import *
from variables.variables import *
from utils.utils import *

def convert_FU_DCM(FU_dir, Follow_Ups):
    
    count = 0
    for subject in Follow_Ups:
        count += 1
        
        print '================================================'
        print '%s. Converting Follow Up Dicoms for %s' % (count, subject)
        print '================================================'

        #Input/Output
        DCM_dir = os.path.join(FU_dir, subject, 'foll', 'DICOM')
        NII_dir = mkdir_path(os.path.join(FU_dir, subject, 'foll','NII'))
        
        #read all dicoms
        all_dicoms = []
        for img in os.listdir(DCM_dir):
            img = os.path.join(DCM_dir, img)
            all_dicoms.append(img)
            
        #convert to nii
        os.system('dcm2niix -o %s %s' %(NII_dir, DCM_dir))

	#remove duplicates
        FU_dir = os.path.join(zfs, subject, 'foll')
        print '-%s. removing duplicates for %s' %(count, subject)
        #clean out duplicate follow ups
        os.system('rm -rf %s' %(FU_dir))
        
convert_FU_DCM(FU_dir, Follow_Ups)
