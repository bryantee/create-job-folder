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

def newDir(date, address, name=''):
    """name and create directory in Dropbox"""
    directory_name = date + ' - ' + name + address
    os.mkdir(dropbox_path_to_client + directory_name)
    print('%s has been created in Dropbox/%s' % (directory_name, client_name) )
    return (dropbox_path_to_client + directory_name + '/')

def copyDir(new_dir):
    """copies files over to new directory from template"""
    copytree(path_to_template, new_dir)
    print("DONE and COPIED!")


# Check to see if path exists in config file and saves to variable
# If not, then it asks user and saves input to variable and line for future
if os.path.isfile('dropbox_path.txt'):
    my_file = open("dropbox_path.txt", "r")
    dropbox_path = my_file.readline()
    print("Dropbox path is: %s" % dropbox_path)
else:
    my_file = open("dropbox_path.txt", "w")
    dropbox_path = input("Nothing here. What's the path to Dropbox? (Include trailing '/') ")
    print("...Setting path of dropbox to %s...." % dropbox_path)
    my_file.write(str(dropbox_path))
my_file.close()

# Welcome Screen
# User selects what client to use for folder
print("-= WELCOME TO THE JOB FOLDER TEMPLATE START =- \n")
print("Choose a client: \n")
print("1.) Charter Home Alliance\n")
print("2.) Custom\n")
print("3.) Nu Tone\n")
print("4.) Home Advisor\n")
print("5.) American Homes\n")

client_selected = int(input("(Enter only the number for the coresponding job type: "))

# PATH variables
if client_selected == 1:
    client_name = 'Charter Home Alliance'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Charter Alliance/')
    path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/Fannie Mae/xXxADDRESSxXx/')
elif client_selected == 2:
    client_name = 'Custom'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Custom/')
    path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/Custom/')
elif client_selected == 3:
    client_name = 'Nu Tone'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Nu Tone/')
    path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/NuTone/')
elif client_selected == 4:
    client_name = 'Home Advisor'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Home Advisor/')
    path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/AH4R/')
elif client_selected == 5:
    client_name = 'American Homes'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/AH4R/')
    path_to_template = (dropbox_path + '2 - Documents/1 - Job Folder Templates/AH4R/')


# Get date details, print to console and set variable
todays_date = str(datetime.date.today())
print("Today's date is %s" % todays_date)

# Collect address and customer from user. Used to create directory name.

if client_selected == 2 or client_selected == 4:
	customer_address =  " (" + (input("What is the ADDRESS at this property? : ")) + ")"
	customer_name = (input("What is the LAST name of the customer? : "))
	customer_name = customer_name.upper()
else:
	customer_address = input("What is the address? ")

# Call function to create dir
if client_selected == 2 or client_selected == 4:
	copyDir(newDir(todays_date, customer_address, customer_name))
else:
	copyDir(newDir(todays_date, customer_address))

input("Press any to close...")
