import shutil
import datetime
import os
import sys
from tinydb import TinyDB, Query


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def newDir(date, address, dropbox_path_to_client, client_name, name=""):
    """name and create directory in Dropbox"""
    directory_name = date + " - " + name + address
    os.makedirs(dropbox_path_to_client + directory_name)
    print("%s has been created in Dropbox/%s" % (directory_name, client_name))
    return dropbox_path_to_client + directory_name + "/"


def copyDir(new_dir, path_to_template):
    """copies files over to new directory from template"""
    copytree(path_to_template, new_dir)
    print("DONE and COPIED!")


def getDropboxPath(file_paths_table):
    """get the dropbox path from the database or else create one"""
    Path = Query()
    items = file_paths_table.search(Path.type == "Dropbox")

    if len(items) > 0:
        return items[0].get("path")
    else:
        return createDropboxPath(file_paths_table)


def createDropboxPath(file_paths_table):
    """create the dropbox path and save in database"""
    path = input("Nothing here. What's the path to Dropbox? (Include trailing '/') ")
    print("...Setting path of dropbox to %s...." % path)
    file_paths_table.insert({"type": "Dropbox", "path": path})

    return path


def getDefaultTemplatePath(file_paths_table):
    """get the default template path or else create one"""
    Path = Query()
    items = file_paths_table.search(Path.type == "Default Template")

    if len(items) > 0:
        return items[0].get("path")
    else:
        return createDefaultTemplatePath(file_paths_table)


def createDefaultTemplatePath(file_paths_table):
    """create a default template path and save in database"""
    path = input("What should be the default template path? (Include trailing '/')")
    print("...Setting path of default template to %s...." % path)
    file_paths_table.insert({"type": "Default Template", "path": path})

    return path


def createClient(client_name, client_path, client_table):
    """Creates a client in the table"""
    client_table.insert({"name": client_name, "path": client_path})


def promtClientCreation(client_table):
    """Promt user for creation of client"""
    client_name = input("Enter the name of a client you would like to add:")
    client_path = input(
        "Where should the directory be relative to your main directory?:"
    )

    try:
        createClient(client_name, client_path, client_table)
        print("Created client %s at %s" % (client_name, client_path))
    except Exception as inst:
        print("There was an issue creating the client", inst)


def clientsExist(client_table):
    """determines whether any clients exist in the table"""
    return len(client_table.all()) > 0


def getClientListFromDb(clients_table):
    """Returns a list of all the clients in a given table"""
    return clients_table.all()


def printClientSelectionList(clients):
    """
    Print client list for selection
    
    Returns map of clients with index PK
    """
    if len(clients) == 0:
        print(
            "You don't seem to have any clients. We'll need to create some to start...\n"
        )
    else:
        print("\n -= WELCOME TO THE JOB FOLDER TEMPLATE START =- \n")
        print("Choose a client: \n")

        mapOfClients = {}

        for index, item in enumerate(clients, start=1):
            print("%s.) %s" % (index, item["name"]))
            mapOfClients[index] = item

            if index == len(clients):
                print("%s.) Add a new one \n" % (str(index + 1)))

        return mapOfClients


def printTodaysDate():
    todays_date = str(datetime.date.today())

    print("Today's date is %s" % todays_date)

