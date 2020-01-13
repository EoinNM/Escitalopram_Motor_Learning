import os 
from os import *
import shutil
from variables.variables import *
from utils.utils import *

def copy_task(population, ZFS_fMRI, days):

    print '========================================================================================'
    print '                                Copy MOTORTASK Data                                    '
    print '========================================================================================'
    
    count = 0
    for subject in population:
        count +=1
        
        for day in days:
            #I/O
            task_path = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'functional')
            task = os.path.join(task_path, 'MOTORTASK.nii')
            anat_path = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'anatomical')
            anat = os.path.join(anat_path, 'ANATOMICAL.nii')
            phase_path = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'field_maps', 'Phase')
            phase = os.path.join(phase_path, 'PHASE.nii')
            magn_path = os.path.join(ZFS_fMRI, subject, day, 'SPM_fMRI', 'field_maps', 'Mag')
            magn = os.path.join(magn_path, 'MAGNITUDE.nii')
            
            data_dir = mkdir_path(os.path.join('/nobackup/roggen2/Molloy/', 'TASK_RePreproc', subject, day))
            
            #copy task data
            print 'Now copying task data to new location for %s. %s, %s' %(count, subject, day)
            shutil.copy(task, data_dir)
            
            print 'Now copying anat data to new location for %s. %s, %s' %(count, subject, day)
            shutil.copy(anat, data_dir)

            print 'Now copying phase data to new location for %s. %s, %s' %(count, subject, day)
            shutil.copy(phase, data_dir) 
            
            print 'Now copying magnitude data to new location for %s. %s, %s' %(count, subject, day)
            shutil.copy(magn, data_dir)
        
        #os.system("SPM matlab -softwareopengl -nodesktop -nosplash -noFigureWindows -r \"Task_Preproc"")
            
copy_task(['MCLT'], ZFS_fMRI, days)
