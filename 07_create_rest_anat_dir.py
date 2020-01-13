#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:52:46 2018

@author: molloy
"""

import os
from os import *
import shutil
import glob
from utils.utils import *
from variables.variables import *

def prep_RS(ZFS_fMRI, population, days):
    
    count = 0
    for subject in population:
        count +=1
        for day in days:
            
            print '============================================================'
            print '     %s. Copying ANATOMICAL.nii for %s, %s' %(count, subject, day)
            print '============================================================'
            
            #I/0 
            srcT1 = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'anatomical')
            dstT1 = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'rest_anatomical')

            #copy original T1
            for T1_file in glob.glob(os.path.join(srcT1, 'ANATOMICAL.nii')):
                T1_nii = T1_file
                os.system('cp %s %s %s' %(T1_nii, srcT1, dstT1))
            
prep_RS(ZFS_fMRI, population, days)
            