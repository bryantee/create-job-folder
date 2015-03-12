#!/usr/bin/python3

import shutil
import datetime
import os, sys

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def newDir(date, address):
    """name and create directory in Dropbox"""
    directory_name = date + ' - ' + address
    os.mkdir(dropbox_path_to_fm + directory_name)
    print('%s has been created in Dropbox/Fannie Mae folder...' % directory_name)
    return (dropbox_path_to_fm + directory_name + '/')

def copyDir(new_dir):
    """copies files over to new directory from template"""
    copytree(path_to_template, new_dir)
    print("DONE and COPIED!")
    

# Welcome Screen
print("-= WELCOME TO THE FANNIE MAE JOB FOLDER TEMPLATE START =-")
print("\n")

# Check to see if path exists in config file and saves to variable
# If not, then it asks user and saves input to variable and line for future
my_file = open("/home/bryan/Desktop/test.txt", "r+")
dropbox_path = ''
dropbox_path = my_file.readline()
if dropbox_path == '':
    dropbox_path = input("Nothing here. What's the path to Dropbox? (Include trailing '/') ")
    print("...Setting path of dropbox to %s...." % dropbox_path)
    my_file.write(str(dropbox_path))
else:
    print("Dropbox path is: %s" % dropbox_path)
my_file.close()

# PATH variables
dropbox_path_to_fm = (dropbox_path + '1 - Jobs/Charter Alliance/Fannie Mae/')
path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/Fannie Mae/xXxADDRESSxXx/')


# Get date details, print to console and set variable
todays_date = str(datetime.date.today())
print("Today's date is %s" % todays_date)

# Collect address from user. Used to create directory name.
directory_name = (input("What is the address at this property? : "))

# Call function to create dir
copyDir(newDir(todays_date, directory_name))

input("Press any to close...")



	
