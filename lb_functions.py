import csv

# Searches the database for all pokemon who are part the passed type_req
# type_req is the type that is desired
def types(type_req):

    with open('databases/lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if type_req.upper() == row[3].upper() or type_req.upper() == row[4].upper():
                type_list.append(row[2])
        return type_list

# Searches the database for all pokemon whos types are the ones passed
# type_one and type_two are the types desired
def dual_types(type_one, type_two):
    with open('databases/lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if (type_one.upper() == row[3].upper() and type_two.upper() == row[4].upper()) or (type_two.upper() == row[3].upper() and type_one.upper() == row[4].upper()):
                type_list.append(row[2])
        return type_list

# Searches the database for all pokemon whos only type is the passed type
# type_req is the type that is desired
def mono(type_req):
    with open('databases/lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if type_req.upper() == row[3].upper() and row[4] == '$':
                type_list.append(row[2])
        return type_list

# Searches the database for the passed ability
# ability_name is the ability that is desired
def ability(ability_name):

    with open('databases/ability_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        #loop through csv list
        for row in csv_file:
            #if current rows name is equal to input, print that row
            if ability_name.upper() == row[0].upper():
                return row
        return -1

# Searches for the given nature
# nature_name is the desired nature
def nature(nature_name):

    with open('databases/natures.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        #loop through csv list
        for row in csv_file:
            #if current rows name is equal to input, print that row
            if nature_name.upper() == row[0].upper():
                return row
        return -1
