import os
from os import *
import dicom as dcm
import shutil
import glob
from utils.utils import *
from variables.variables import *

def prep_fMRI_preproc(mri_temp, population, days):
    
    count = 0
    for subject in population:
        for day in days:
            count += 1
        
            print '===================================================================='
            print ' %s. Creating New SPM Dirs & Copying/Renaming Task Nifti for %s, %s'  %(count, subject, day)
            print '===================================================================='
        
            #Nifti location
            NII_dir = os.path.join(mri_temp, subject, day)
            #make new sub dirs for MatLab batch script
            mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'analysis'))
            mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'functional'))
            mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'anatomical'))
            mkdir_path(os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'field_maps'))
            #define SPM paths
            T1_dir = os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'anatomical')
            T2_dir = os.path.join(mri_temp, subject, day, 'SPM_fMRI', 'functional')
            
            #read all niftis
            if os.listdir(NII_dir) is not None:
                all_nii = []
                for nifti in os.listdir(NII_dir):
                    nifti = os.path.join(NII_dir, nifti)
                    all_nii.append(nifti)
                            
            #read T2* & MPRAGE
            T1_nii = []
            T2_nii = []
            for nifti in sorted (all_nii):
                if os.path.isfile(os.path.join(NII_dir, nifti)) and 'DICOM_MPRAGE' in nifti:
                    T1_nii.append(nifti)
                else:
                    if os.path.isfile(os.path.join(NII_dir, nifti)) and 'DICOM_t2star_epi_2D_motortask' in nifti:
                        T2_nii.append(nifti)
                        
            #copy to SPM paths
            for T1_NIFTI in T1_nii:
                shutil.copy(T1_NIFTI, T1_dir)
                for T2_NIFTI in T2_nii:
                    shutil.copy(T2_NIFTI, T2_dir)
                    
            #rename functional & anatomical
            for file in os.listdir(T1_dir):
                if file.endswith('.nii'):
                    os.rename(str(os.path.join(T1_dir, file)),
                              str(os.path.join(T1_dir, 'ANATOMICAL.nii')))
                    
            for file in os.listdir(T2_dir):
                if file.endswith('.nii'):
                    os.rename(str(os.path.join(T2_dir, file)),
                              str(os.path.join(T2_dir, 'MOTORTASK.nii')))
                    
prep_fMRI_preproc(mri_temp, population, days)
