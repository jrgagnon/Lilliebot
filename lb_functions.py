import csv

#Help function: Lets users know what commands this bot recognizes
def help():
    return '```Below are the commands recognized\n' \
           '- *pic followed by either a pokemons national dex number or name\n' \
           '    :posts a picture of that pokemon\n' \
           '- *stats followed by either a pokemons national dex number or name\n' \
           '    :gives you the stats asscoiated with that pokemon\n' \
           '- *random\n' \
           '    :posts the picture of a random pokemon\n' \
           '- *guess\n' \
           '    :used with the random command to guess what pokemon was posted\n' \
           '- *help\n' \
           '    :can be used at anytime to see these commands again```'

#Stats: Takes either a pokemons national dex number or name
#       Returns their stats from a csv
#Type is what row it should search, 1 for number, 2 for name
#Info is what number or name we are looking for
def stats(type, info):
    #read csv, and split on "," the line
    csv_file = csv.reader(open('lillie_bot_database.csv', "rb"), delimiter=",")

    if type == 1:
        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if info == row[type]:
                return row
    else:
        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if info.upper() == row[type].upper():
                return row
