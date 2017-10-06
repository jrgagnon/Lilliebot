import csv

#move_info: take a move name and searchs the database for it
#move_name is the desired move
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

# Function that formats the info for posting move info
# Takes an array of information assciated with a move
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
