import os
from os import *
from variables.variables import *
from utils.utils import *
import nipype.interfaces.fsl as fsl
import shutil

def check_norm(motor, population, days):
    
    count = 0
    for subject in population:
        count +=1
        for day in days:
            
            in_wauMOTOR  = os.path.join(motor, subject, day)
            wau_file = os.path.join(in_wauMOTOR, 'wauMOTORTASK.nii')
            norm_check = mkdir_path(os.path.join('/NOBACKUP2/molloy/fMRI_QC/Normalisation/', 'OTHER_VOLS', subject, day))
            single_vol = mkdir_path(os.path.join('/NOBACKUP2/molloy/fMRI_QC/Normalisation/', 'FIRST_VOLS'))
            
            print 'Copying the normalised functional data to the QC directory for %s. %s, %s' %(count, subject, day)
            shutil.copy(wau_file, norm_check)
            
            os.chdir(norm_check)
            
            print 'Now splitting each nifti file into subcomponent volumes for %s. %s, %s' %(count, subject, day)
            os.system('fslsplit wauMOTORTASK.nii %s_%s_vols -t' %(subject, day))
            
            print'Now inflating the new first volume for %s. %s, %s' %(count, subject, day)
            os.system('gunzip -k %s_%s_vols0000.nii.gz' %(subject, day))
            
            #move first vols to new dir for summing
            first_vols_src = os.path.join(norm_check, '%s_%s_vols0000.nii'%(subject, day))
            first_vols_dst = os.path.join(single_vol)
            print'Now moving the new first volume for %s. %s, %s' %(count, subject, day)
            shutil.move(first_vols_src, first_vols_dst)
            
            os.chdir(first_vols_dst)

            
            print 'Now thresholding and binarising normalised gray task mask for %s. %s, %s' %(count, subject, day)
            os.system('fslmaths %s_%s_vols0000.nii -thr 0.2 -bin %s_%s_thr_bin_vols0000.nii' %(subject, day, subject, day))
            
            print 'Now inflating the binarised and thresholded images for %s. %s, %s' %(count, subject, day)
            os.system('gunzip -k %s_%s_thr_bin_vols0000.nii.gz' %(subject, day))
            
            #remove the unzipped file
            os.system('rm -r %s_%s_thr_bin_vols0000.nii.gz' %(subject, day))
            
    print 'Summed GM Image exists go to %s to look' %(single_vol)
    os.system('fslmaths %s_base_thr_bin_vols0000.nii -add %s_day1_thr_bin_vols0000.nii -add %s_day7_thr_bin_vols0000.nii sum_wau_MOTORTASK' %(subject, subject, subject))
    os.system('gunzip -k sum_wau_MOTORTASK.nii.gz')
        
    
check_norm(motor, population, days)
