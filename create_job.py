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
    items = file_paths_table.search(Path.type == 'Dropbox')

    if len(items) > 0:
        return items[0].get('path')
    else:
        return createDropboxPath()

def createDropboxPath():
    """create the dropbox path and save in database"""
    path = input("Nothing here. What's the path to Dropbox? (Include trailing '/') ")
    print("...Setting path of dropbox to %s...." % path)
    file_paths_table.insert({ 'type': 'Dropbox', 'path': path })

    return path

def getDefaultTemplatePath():
    """get the default template path or else create one"""
    Path = Query()
    items = file_paths_table.search(Path.type == 'Default Template')

    if len(items) > 0:
        return items[0].get('path')
    else:
        return createDefaultTemplatePath()

def createDefaultTemplatePath():
    """create a default template path and save in database"""
    path = input('What should be the default template path? (Include trailing \'/\')')
    print("...Setting path of default template to %s...." % path)
    file_paths_table.insert({ 'type': 'Default Template', 'path': path })

    return path

def createClient(client_name, client_path, client_table):
    client_table.insert({ 'name': client_name, 'path': client_path })

def promtClientCreation(client_table):
    client_name = input('Enter the name of a client you would like to add:')
    client_path = input('Where should the directory be relative to your main directory?:')

    try:
        createClient(client_name, client_path, client_table)
        print('Created client %s at %s' % (client_name, client_path))
    except Exception as inst:
        print('There was an issue creating the client', inst)
    
def clientsExist(client_table):
    return len(client_table.all()) > 0

def getClientListFromDb():
    return clients_table.all()

def printClientSelectionList(clients):
    if len(clients) == 0:
        print('You don\'t seem to have any clients. We\'ll need to create some to start...\n') 
    else:
        print("\n -= WELCOME TO THE JOB FOLDER TEMPLATE START =- \n")
        print("Choose a client: \n")

        mapOfClients = {}

        for index, item in enumerate(clients, start=1):
            print('%s.) %s' % (index, item['name']))
            mapOfClients[index] = item

            if index == len(clients):
                print('%s.) Add a new one \n' % (str(index + 1)))

        return mapOfClients

db = TinyDB('db.json')
file_paths_table = db.table('file_paths')
clients_table = db.table('clients')
dropbox_path = getDropboxPath()
default_template_path = getDefaultTemplatePath()

if clientsExist(clients_table) == False:
    print('Looks like you don\'t have any clients. Let\'s get started by adding some...')
    promtClientCreation(clients_table)


mapOfClients = printClientSelectionList(clients_table.all())
client_selected = int(input("(Make a selection by number only: "))
number_of_clients = len(clients_table.all())

if client_selected == number_of_clients + 1:
    continue_adding = True
    # Then selection was at for option to add more
    while continue_adding == True:
        promtClientCreation(clients_table)
        continue_input = input('Added! Want to add more? (y/n)')
        continue_adding = True if continue_input == 'y' else False 
    
    mapOfClients = printClientSelectionList(clients_table.all())
    mapOfClients = printClientSelectionList(clients_table.all())
    client_selected = int(input("(Make a selection by number only: "))

selectedClient = mapOfClients[client_selected]
dropbox_path_to_client = dropbox_path + selectedClient['path']
client_name = selectedClient['name']

# TODO: Add logic to overide default template path if specified by user
# this will allow for more flexibility when creating template specific to jobs / clients
path_to_template = default_template_path

# Get date details, print to console and set variable
todays_date = str(datetime.date.today())
print("Today's date is %s" % todays_date)

# Collect address and customer from user. Used to create directory name.
customer_address = input("What is the job name? (or address) ")

# Call function to create dir
copyDir(newDir(todays_date, customer_address))

input("Press any to close...")
