import os
from os import *
import shutil
import glob
from utils.utils import *
from variables.variables import *

def pull_FU_field_maps(population, FU_dir, motor):

    print '========================================================================================'
    print '                                Pulling Field Maps Now                                   '
    print '========================================================================================'


    count = 0
    for subject in population:
        count += 1
        
        #I/O
        field_maps_src = os.path.join(FU_dir, subject, 'foll', 'NII')
        Mag_dir   = mkdir_path(os.path.join(motor, subject, 'foll', 'MAG'))
        Phase_dir = mkdir_path(os.path.join(motor, subject, 'foll', 'PHASE'))
        
        #MAG Maps - Copy to tmp dir
        #if map is numbered as a 6
        print '======================================'
        print ' %s. Getting Phase data for %s' %(count,subject)
        print '======================================'
        for mag_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_6.nii')):
            mag_src = mag_map
            shutil.copy(mag_src, Mag_dir)
        #if map is numbered as an 8
        for mag_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_8.nii')):
            mag_src = mag_map
            shutil.copy(mag_src, Mag_dir)
        #Rename file
        print ' %s. Renaming Phase data for %s' %(count,subject)
        for file in os.listdir(Mag_dir):
            if file.endswith('.nii'):
                os.rename(str(os.path.join(Mag_dir, file)),
                          str(os.path.join(Mag_dir, 'MAGNITUDE.nii')))
            
        #Phase Maps - Copy to tmp dir
        #if map is numbered as a 7
        print '======================================'
        print ' %s. Getting Magnitiude data for %s' %(count,subject)
        print '======================================'
        for phase_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_7.nii')):
            phase_src = phase_map
            shutil.copy(phase_src, Phase_dir)
        #if map is numbered as an 9
        for phase_map in glob.glob(os.path.join(field_maps_src, 'DICOM_gre_field_mapping_fmri_*_9.nii')):
            phase_src = phase_map
            shutil.copy(phase_src, Phase_dir)
        #Rename file
        print ' %s. Renaming Magnitude data for %s' %(count,subject)
        for file in os.listdir(Phase_dir):
            if file.endswith('.nii'):
                os.rename(str(os.path.join(Phase_dir, file)),
                          str(os.path.join(Phase_dir, 'PHASE.nii')))
                
pull_FU_field_maps(population, FU_dir, motor)