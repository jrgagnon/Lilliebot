#Help function: Lets users know what commands this bot recognizes
def help():
    return '```Below are the commands recognized\n' \
           '- *pic (national dex number) or (pokemon name)\n' \
           '    :posts a picture of that pokemon\n' \
           '- *stats (national dex number) or (pokemon name)\n' \
           '    :gives you the stats asscoiated with that pokemon\n' \
           '- *mega (national dex number) or (pokemon name)\n' \
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

#Get the bot token from the token file
def get_token():
    token_file = open('token.txt', 'r')

    token = token_file.readline()
    token = token[0: -1]

    token_file.close()

    return token

# Function that formats the info for posting the stats associated with a pokemon
# Takes an array of information assciated with a pokemon
def stats_print(info):
    m = '```Name: '
    m = m + info[2] + '\n'
    m = m + 'Number: ' + info[1] + '\n'
    if info[4] == '$':
        m = m + 'Type: ' + info[3] + '\n'
    else:
        m = m + 'Type: ' + info[3] + ' ' + info[4] + '\n'
    m = m + 'Evolution: ' + info[6] + '\n'

    if info[5] != '$':
        m = m + 'Has Mega: ' + info[5] + '\n'
    else:
        m = m + 'Has Mega: No' + '\n'

    m = m + 'HP: ' + info[7] + '\n'
    m = m + 'Attack: ' + info[8] + '\n'
    m = m + 'Defense: ' + info[9] + '\n'
    m = m + 'Special Attack: ' + info[10] + '\n'
    m = m + 'Special Defense: ' + info[11] + '\n'
    m = m + 'Speed: ' + info[12] + '\n'
    m = m + 'Weaknesses: ' + info[13]
    for x in info[14:]:
        m = m + ' ' + x
    m = m + '```'
    return m

# Function that formats the info for posting the stats associated with a  mega pokemon
# Takes an array of information assciated with a mega pokemon
def mega_print(info):
    m = '```Name: '
    if info[1] == '383' or info[1] == '382':
        m = m + 'Primal ' + info[2] + '\n'
    else:
        m = m + 'Mega ' + info[2] + '\n'

    m = m + 'Number: ' + info[1] + '\n'
    if info[4] == '$':
        m = m + 'Type: ' + info[3] + '\n'
    else:
        m = m + 'Type: ' + info[3] + ' ' + info[4] + '\n'
    m = m + 'HP: ' + info[5] + '\n'
    m = m + 'Attack: ' + info[6] + '\n'
    m = m + 'Defense: ' + info[7] + '\n'
    m = m + 'Special Attack: ' + info[8] + '\n'
    m = m + 'Special Defense: ' + info[9] + '\n'
    m = m + 'Speed: ' + info[10] + '\n'
    m = m + 'Weaknesses: ' + info[11]
    for x in info[12:]:
        m = m + ' ' + x
    m = m + '```'
    return m

# Function that prints a 3 column list of pokemon with an assciated type_one
# Takes an array of pokemon
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

# Function that prints ability information
# Takes an array of ability information
def ability_print(info):
    m = '```Ability Name: '
    m = m + info[0] + '\n' + '\n'
    m = m + 'Description:' + '\n'
    m = m + info[1] + '\n' + '\n'
    m = m + '```'
    return m

# Generates a string of spaces the length of the number passed
def spacing(num_spaces):
    count = 0
    m = ''
    while count < num_spaces:
        m = m + ' '
        count = count + 1

    return m
