def get_token():
    token_file = open('token.txt', 'r')

    token = token_file.readline()
    token = token[0: -1]

    token_file.close()

    return token

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
