import os 
from os import *
import glob
import shutil
from variables.variables import *
from utils.utils import *

def copy_FU_data(foll_population, FU_dir, motor):
    
    count = 0
    for subject in foll_population:
        count +=1
        
	#I/O
        FU_data = os.path.join(FU_dir, subject, 'foll', 'NII')
        tmp_dir = os.path.join(motor, subject, 'foll')
        
	#read all niftis
	if os.listdir(FU_data) is not None:
	    all_nii = []
    	    for nifti in os.listdir(FU_data):
                nifti = os.path.join(FU_data, nifti)
		all_nii.append(nifti)
                    
	#read T2* & MPRAGE
        T1_nii = []
        T2_nii = []
        for nifti in all_nii:
            if os.path.isfile(os.path.join(FU_data, nifti)) and 'DICOM_MPRAGE' in nifti:
                  T1_nii.append(nifti)
            else:
                  if os.path.isfile(os.path.join(FU_data, nifti)) and 'DICOM_t2star_epi_2D_motortask' in nifti:
                      T2_nii.append(nifti)

	#copy from zfs to MOTORTASK 'foll' tmp directory
        #1. task
	print 'Copying MOTORTASK nifti for %s. %s'%(count, subject)
	for motortask in T2_nii:        
	    shutil.copy(motortask, tmp_dir)
        #2. anat
	print 'Copying ANATOMICAL nifti for %s. %s'%(count, subject)
	for anatomical in T1_nii:
            shutil.copy(anatomical, tmp_dir)

 	#rename functional & anatomical
	print 'Renaming MOTORTASK & ANATOMICAL niftis for %s. %s'%(count, subject)
        for file in os.listdir(tmp_dir):
            if file.startswith('DICOM_t2star'):
                os.rename(str(os.path.join(tmp_dir, file)), str(os.path.join(tmp_dir, 'MOTORTASK.nii')))
	    else:
                 if file.startswith('DICOM_MPRAGE'):
	             os.rename(str(os.path.join(tmp_dir, file)), str(os.path.join(tmp_dir, 'ANATOMICAL.nii')))


copy_FU_data(foll_population, FU_dir, motor)
        
