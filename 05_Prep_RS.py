#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:45:17 2018

@author: molloy
"""

import os
from os import *
import shutil
import glob
from utils.utils import *
from variables.variables import *

leftovers = ["TCET", "VS7T", "BMQX","FL9T", "HS8X", "KTIT", "NT6T", "RMAX", "WSKT", "BSVT", "KTKT", "OK7T", "SATX", "TSFT", "ZJ4T"]

def prep_RS(mri_temp, population, days):
    
    count = 0
    for subject in population:
        count +=1
        for day in days:
            
            print '============================================================'
            print '     %s. Copying and Renaming RS Nifits for %s, %s' %(count, subject, day)
            print '============================================================'
           
            # I/O
            subject_dir = os.path.join(mri, subject)
            RS_dst = mkdir_path(os.path.join(subject_dir, day, 'SPM_fMRI', 'rest'))
            
            #copy data
            print 'Now Copying Niftis to ''rest'' folder'
            for RS_nii in glob.glob(os.path.join(subject_dir, day, '*mbep2d_resting*')):
                    RS_src = RS_nii
                    os.system('cp %s %s' % (RS_src, RS_dst))
            
            #rename data
            print 'Now renaming data'
            for nifti in os.listdir(RS_dst):
                    if nifti.endswith('.nii'):
                        os.rename(str(os.path.join(RS_dst, nifti)),
                            str(os.path.join(RS_dst, 'REST.nii')))

prep_RS(mri, leftovers, days)