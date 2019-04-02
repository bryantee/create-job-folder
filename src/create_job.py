#!/usr/bin/python3

from helpers import (
    newDir,
    copyDir,
    getDropboxPath,
    createDropboxPath,
    getDefaultTemplatePath,
    createDefaultTemplatePath,
    createClient,
    promtClientCreation,
    clientsExist,
    getClientListFromDb,
    printClientSelectionList,
    printTodaysDate,
)
from tinydb import TinyDB
import datetime


def main():
    db = TinyDB("../db.json")
    file_paths_table = db.table("file_paths")
    clients_table = db.table("clients")
    dropbox_path = getDropboxPath(file_paths_table)
    default_template_path = getDefaultTemplatePath(file_paths_table)

    if clientsExist(clients_table) == False:
        print(
            "Looks like you don't have any clients. Let's get started by adding some..."
        )
        promtClientCreation(clients_table)

    clients = getClientListFromDb(clients_table)
    mapOfClients = printClientSelectionList(clients)
    selection = int(input("(Make a selection by number only: "))
    number_of_clients = len(clients)

    if selection == number_of_clients + 1:
        continue_adding = True
        # Then selection was at for option to add more
        while continue_adding == True:
            promtClientCreation(clients_table)
            continue_input = input("Added! Want to add more? (y/n)")
            continue_adding = True if continue_input == "y" else False

        mapOfClients = printClientSelectionList(getClientListFromDb(clients_table))
        selection = int(input("(Make a selection by number only: "))

    selectedClient = mapOfClients[selection]
    dropbox_path_to_client = dropbox_path + selectedClient["path"]
    client_name = selectedClient["name"]

    # TODO: Add logic to overide default template path if specified by user
    # this will allow for more flexibility when creating template specific to jobs / clients
    path_to_template = default_template_path

    printTodaysDate()

    # Collect address and customer from user. Used to create directory name.
    customer_address = input("What is the job name? (or address) ")

    # Call function to create dir
    copyDir(
        newDir(todays_date, customer_address, dropbox_path_to_client, client_name),
        path_to_template,
    )

    input("Press any to close...")


if __name__ == "__main__":
    main()
