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

def copy_nii(mri_temp, population, days):
    count = 0
    for subject in population:
        count +=1
        for day in days:
                
            print '================================================'
            print '        -%s. copying NIIs for %s, %s' %(count, subject, day)
            print '================================================'
            
            #I/O
            source = os.path.join(zfs, subject, day, 'NII')
            destination = mkdir_path(os.path.join(mri_temp, 'SSRI_Niftis', subject, day))
            #copy to temp space
            copy_tree(source, destination)
                
copy_nii(mri_temp, population, days)