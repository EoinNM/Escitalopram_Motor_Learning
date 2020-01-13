import os
from os import *
from variables.variables import *
from utils.utils import *
import nipype.interfaces.fsl as fsl
import shutil

def sum_gm(motor, population, days):
    
    count = 0
    for subject in population:
        count +=1
        for day in days:
        
            in_wc1  = os.path.join(motor, subject, day)
            
            os.chdir(in_wc1)
                    
            print 'Now thresholding and binarising normalised gray matter mask for %s. %s, %s' %(count, subject, day)
            os.system('fslmaths wc1ANATOMICAL.nii -thr 0.2 -bin %s_%s_thr_bin_wc1' %(subject, day))
            
            print'Now inflating the new GM maps for %s. %s, %s' %(count, subject, day)
            os.system('gunzip -k %s_%s_thr_bin_wc1.nii.gz'%(subject, day))
            
            print'Now moving the new GM maps'
            src = os.path.join(in_wc1, '%s_%s_thr_bin_wc1.nii' %(subject, day))
            dst = mkdir_path (fMRI_QC)
            shutil.move(src, dst)
            
        os.chdir(dst)
        print 'Summed GM Image exists go to %s to look' %(dst)
        os.system('fslmaths %s_base_thr_bin_wc1.nii -add %s_day1_thr_bin_wc1.nii -add %s_day7_thr_bin_wc1.nii sum_gm' %(subject, subject, subject))
        

sum_gm(motor, population, days)