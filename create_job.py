#!/usr/bin/python3

from tinydb import TinyDB, Query
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
    os.makedirs(dropbox_path_to_client + directory_name)
    print('%s has been created in Dropbox/%s' % (directory_name, client_name) )
    return (dropbox_path_to_client + directory_name + '/')

def copyDir(new_dir):
    """copies files over to new directory from template"""
    copytree(path_to_template, new_dir)
    print("DONE and COPIED!")

def getDropboxPath():
    """get the dropbox path from the database or else create one"""
    Path = Query()
    items = file_paths.search(Path.type == 'Dropbox')

    if len(items) > 0:
        return items[0].get('path')
    else:
        return createDropboxPath()

def createDropboxPath():
    """create the dropbox path and save in database"""
    path = input("Nothing here. What's the path to Dropbox? (Include trailing '/') ")
    print("...Setting path of dropbox to %s...." % path)
    file_paths.insert({ 'type': 'Dropbox', 'path': path })

    return path

def getDefaultTemplatePath():
    """get the default template path or else create one"""
    Path = Query()
    items = file_paths.search(Path.type == 'Default Template')

    if len(items) > 0:
        return items[0].get('path')
    else:
        return createDefaultTemplatePath()

def createDefaultTemplatePath():
    """create a default template path and save in database"""
    path = input('What should be the default template path? (Include trailing \'/\')')
    print("...Setting path of default template to %s...." % path)
    file_paths.insert({ 'type': 'Default Template', 'path': path })

    return path


db = TinyDB('db.json')
file_paths = db.table('file_paths')
dropbox_path = getDropboxPath()
default_template_path = getDefaultTemplatePath()
print('dropbox_path: %s' % dropbox_path)
print('default_template_path: %s' % default_template_path)

# Welcome Screen
# User selects what client to use for folder
print("\n -= WELCOME TO THE JOB FOLDER TEMPLATE START =- \n")
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
elif client_selected == 2:
    client_name = 'Custom'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Custom/')
elif client_selected == 3:
    client_name = 'Nu Tone'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Nu Tone/')
elif client_selected == 4:
    client_name = 'Home Advisor'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/Home Advisor/')
elif client_selected == 5:
    client_name = 'American Homes'
    dropbox_path_to_client = (dropbox_path + '1 - Jobs/AH4R/')

# TODO: Add logic to overide default template path if specified by user
# this will allow for more flexibility when creating template specific to jobs / clients
path_to_template = default_template_path

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
