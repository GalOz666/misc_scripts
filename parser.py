import glob
import os
import shutil
import time
import os
import sys

"""globals and functions"""

dir = os.getcwd()

ZVM_path = dir+os.sep+'ZVM_scanned'
VRA_path = dir+os.sep+'VRA_scanned'

""" remove in case of duplicate folders """

shutil.rmtree('ZVM_scanned', ignore_errors=True)
shutil.rmtree('VRA_scanned', ignore_errors=True)

print("copying files...")


def copy_wo_dup(src_list, dst_dir):

    for file_path in src_list:
        """ add date element to file to get random microsecond"""
        split = file_path.rsplit(os.sep, 1)
        name = split[-1]
        site_name = split[0]
        site_name = site_name.rsplit(os.sep)

        try:
            if site_name[-1] == 'ZVM':
                file_rename = site_name[-2]+"_" + name
            else:
                file_rename = site_name[0]+site_name[-1] + "_" + name
        except:
            file_rename = split[0]+"_"+name
            print("had some issues with the folder structure")

        destination = dst_dir+os.sep+file_rename
        source = dir+os.sep+file_path

        shutil.copy2(source, destination)


os.mkdir('ZVM_scanned')
os.mkdir('VRA_scanned')


"""         1.a Get ZVM logs list from sub-folders       """


ZVM_files = list(glob.iglob('**/ZVM/*.csv', recursive=True))

"""         1.b Copy to new created folder and get cmd readable path        """


copy_wo_dup(ZVM_files, ZVM_path)


"""         2. repeat process on VRA logs           """

VRA_files = list(glob.iglob('**/*.txt.gz', recursive=True))

copy_wo_dup(VRA_files, VRA_path)


"""         3. Config file - get path set path recursive        """

glob_list = list(glob.iglob(dir + '/**/version_info.txt', recursive=True))

config_file_path = glob_list[0].rsplit(os.sep, 1)[0]
config_file_path = config_file_path.replace('/', os.sep)

"""         4. Call the parser      """

command = r"SupportParser"+" "+ZVM_path+" "+VRA_path+" "+config_file_path+ r"\version_info.txt"
print(command)

""" Read from parser """
print("\tCalling Support-Parser \n\n")
os.system(f"start cmd /c {command}")
time.sleep(2)
sys.exit()
