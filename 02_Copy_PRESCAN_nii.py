#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:20:48 2018

@author: molloy
"""

import os
from os import *
import shutil
from utils.utils import *
from variables.variables import *
from distutils.dir_util import copy_tree
import glob
import shutil

def copy_nii(workspace, population):
    count = 0
    for subject in population:
        count +=1
                
        print '================================================'
        print '        %s. copying T1 NIIs for %s' %(count, subject)
        print '================================================'
        
        #I/O
        for images in glob.glob(os.path.join(zfs, subject, 'pres', 'NII', 'DICOM_MPRAGE_*3.nii')):
            src = images
            dst = mkdir_path(os.path.join(workspace, 'DATA', subject, 'ANATOMICAL', 'pres'))
            #copy to temp space
            shutil.copy(src, dst)
                
copy_nii(workspace, population)
