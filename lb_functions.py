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

    with open('lillie_bot_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

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

def format(info):
    m = '```Name: '
    m = m + info[2] + '\n'
    m = m + 'Number: ' + info[1] + '\n'
    m = m + 'Type: ' + info[3] + ' ' + info[4] + '\n'
    m = m + 'Evolution: ' + info[5] + '\n'
    m = m + 'HP: ' + info[6] + '\n'
    m = m + 'Attack: ' + info[7] + '\n'
    m = m + 'Defense: ' + info[8] + '\n'
    m = m + 'Special Attack: ' + info[9] + '\n'
    m = m + 'Special Defense: ' + info[10] + '\n'
    m = m + 'Speed: ' + info[11] + '\n'
    m = m + 'Weaknesses: ' + info[12]
    for x in info[13:]:
        m = m + ' ' + x
    m = m + '```'
    return m
