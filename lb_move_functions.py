import csv

#Stats: Takes either a pokemons national dex number or name
#       Returns their stats from a csv
#Type is what row it should search, 1 for number, 2 for name
#Info is what number or name we are looking for
def move_info(move_name):

    with open('move_database.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        #loop through csv list
        for row in csv_file:
            #if current rows name is equal to input, print that row
            if move_name.upper() == row[0].upper():
                return row
        return -1

def move_print(info):
    m = '```Move Name: '
    m = m + info[0] + '\n' + '\n'
    m = m + 'Description:' + '\n'
    m = m + info[1] + '\n' + '\n'
    m = m + 'Type: ' + info[2].capitalize() + '\n'
    m = m + 'Category: ' + info[3].capitalize() + '\n'
    m = m + 'Power: ' + info[4] + '\n'
    m = m + 'Accuracy: ' + info[5] + '\n'
    m = m + 'PP: ' + info[6] + '\n'
    m = m + '```'
    return m
