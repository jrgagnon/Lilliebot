import csv

def generate_dict():
    pokedex = {}
    with open('databases/lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if row[1].isnumeric():
                pokedex[row[2].upper()] = row
    return pokedex

def generate_list():
    numbers = []
    with open('databases/lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if row[1].isnumeric():
                numbers.append(row[2].upper())
    return numbers

#Stats: Takes either a pokemons national dex number or name
#       Returns their stats from a csv
#Type is what row it should search, 1 for number, 2 for name
#Info is what number or name we are looking for
def stats(type, info):
    if type == 3:
        with open('databases/forms.csv', newline='') as stats:
            #read csv, and split on "," the line
            csv_file = csv.reader(stats, delimiter=",")

            for row in csv_file:
                #if current rows 1st value is equal to input, print that row
                if info == row[1]:
                    return row
            return -1
    else:
        with open('databases/lillie_bot_database.csv', newline='') as stats:
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

    with open('databases/mega_pokemon.csv', newline='') as stats:
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
