import csv

#Help function: Lets users know what commands this bot recognizes
def help():
    return '```Below are the commands recognized\n' \
           '- *pic (national dex number) or (pokemon name)\n' \
           '    :posts a picture of that pokemon\n' \
           '- *stats (national dex number) or (pokemon name)\n' \
           '    :gives you the stats asscoiated with that pokemon\n' \
           '- *type (pokemon type)\n' \
           '    :posts names of all pokemon of that type\n' \
           '- *mono (pokemon type)\n' \
           '    :posts names of all pokemon whose type is only type is the requested one\n' \
           '- *dual (pokemon type) (pokemon type)\n' \
           '    :posts names of all pokemon who have that type combination\n' \
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

def format(info):
    m = '```Name: '
    m = m + info[2] + '\n'
    m = m + 'Number: ' + info[1] + '\n'
    if info[4] == '$':
        m = m + 'Type: ' + info[3] + '\n'
    else:
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

def types_print(type_list):

    count = 0
    m = '```'

    for item in type_list:
        if count != 2:
            m = m + item + spacing(20 - len(item)) + '| '
            count = count + 1
        else:
            m = m + item + '\n'
            count = count + 1

        if count == 3:
            count = 0
    m = m + '```'
    return m

def spacing(num_spaces):
    count = 0
    m = ''
    while count < num_spaces:
        m = m + ' '
        count = count + 1

    return m
