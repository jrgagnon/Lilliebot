import csv

#Help function: Lets users know what commands this bot recognizes
def help():
    return '```Below are the commands recognized\n' \
           '- *pic (national dex number) or (pokemon name)\n' \
           '    :posts a picture of that pokemon\n' \
           '- *stats (national dex number) or (pokemon name)\n' \
           '    :gives you the stats asscoiated with that pokemon\n' \
           '- *stats (national dex number) or (pokemon name)\n' \
           '    :gives you the stats asscoiated with that mega\n' \
           '- *type (pokemon type)\n' \
           '    :posts names of all pokemon of that type\n' \
           '- *mono (pokemon type)\n' \
           '    :posts names of all pokemon whoses only type is that type\n' \
           '- *dual (pokemon type) (pokemon type)\n' \
           '    :posts names of all pokemon who have that type combination\n' \
           '- *move (move name)\n' \
           '    :gives the information asscoiated with that move\n' \
           '- *ability (ability name)\n' \
           '    :gives the information asscoiated with that ability\n' \
           '- *help\n' \
           '    :can be used at anytime to see these commands again```'

#Stats: Takes either a pokemons national dex number or name
#       Returns their stats from a csv
#Type is what row it should search, 1 for number, 2 for name
#Info is what number or name we are looking for
def stats(type, info):

    with open('lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        if type == 1:
            #loop through csv list
            for row in csv_file:
                #if current rows 1st value is equal to input, print that row
                if info == row[type]:
                    return row
            return -1
        else:
                #loop through csv list
                for row in csv_file:
                    #if current rows 1st value is equal to input, print that row
                    if info.upper() == row[type].upper():
                        return row
                return -1

#Mega: Takes either a pokemons national dex number or name
#       Returns the stats of their mega from a csv
#Type is what row it should search, 1 for number, 2 for name
#Info is what number or name we are looking for
def mega(type, info):

    with open('mega_pokemon.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        if type == 1:
            #loop through csv list
            for row in csv_file:
                #if current rows 1st value is equal to input, print that row
                if info == row[type]:
                    return row
            return -1
        else:
                #loop through csv list
                for row in csv_file:
                    #if current rows 1st value is equal to input, print that row
                    if info.upper() == row[type].upper():
                        return row
                return -1

def types(type_req):

    with open('lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if type_req.upper() == row[3].upper() or type_req.upper() == row[4].upper():
                type_list.append(row[2])
        return type_list

def dual_types(type_one, type_two):
    with open('lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if (type_one.upper() == row[3].upper() and type_two.upper() == row[4].upper()) or (type_two.upper() == row[3].upper() and type_one.upper() == row[4].upper()):
                type_list.append(row[2])
        return type_list

def mono(type_req):
    with open('lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        type_list = []

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if type_req.upper() == row[3].upper() and row[4] == '$':
                type_list.append(row[2])
        return type_list

def ability(ability_name):

    with open('ability_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        #loop through csv list
        for row in csv_file:
            #if current rows name is equal to input, print that row
            if ability_name.upper() == row[0].upper():
                return row
        return -1
