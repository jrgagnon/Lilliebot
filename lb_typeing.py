import csv

class Type:

    def __init__(self, w, r, i):
        self.weaknesses = w
        self.resistances = r
        self.immunities = i

    def getWeaknesses(self):
        return self.weaknesses

    def getResistances(self):
        return self.resistances

    def getImmunities(self):
        return self.immunities

def generate_type_table():

    type_table = {}

    with open('databases/typeings.csv', newline='') as types:
        #read csv, and split on "," the line
        csv_file = csv.reader(types, delimiter=",")

        #loop through csv list
        for row in csv_file:
            weaknesses = []
            resistances = []
            immunities = []
            location = 0
            for item in row[1:]:
                if item == '$':
                    location = location + 1
                elif location == 0:
                    weaknesses.append(item)
                elif location == 1:
                    resistances.append(item)
                elif location == 2:
                    immunities.append(item)

            type_table[row[0]] = Type(weaknesses, resistances, immunities)

    return type_table

def generate_effectiveness(type_table, type1, type2):
    type1Weak = set(type_table[type1].getWeaknesses())
    type1Res = set(type_table[type1].getResistances())
    type1Imm = set(type_table[type1].getImmunities())

    type2Weak = set(type_table[type2].getWeaknesses())
    type2Res = set(type_table[type2].getResistances())
    type2Imm = set(type_table[type2].getImmunities())

    pkmnWeak1 = type1Weak - type2Res - type2Imm
    pkmnWeak2 = type2Weak - type1Res - type1Imm

    pkmnRes1 = type1Res - type2Weak - type2Imm
    pkmnRes2 = type2Res - type1Weak - type1Imm

    effectiveness = []
    effectiveness.append(pkmnWeak1)
    effectiveness.append(pkmnWeak2)

    effectiveness.append(pkmnRes1)
    effectiveness.append(pkmnRes2)

    effectiveness.append(type1Imm)
    effectiveness.append(type2Imm)

    return effectiveness

def generate_effectiveness_mono(type_table, type1):
    typeWeak = set(type_table[type1].getWeaknesses())
    typeRes = set(type_table[type1].getResistances())
    typeImm = set(type_table[type1].getImmunities())

    effectiveness = []
    effectiveness.append(typeWeak)
    effectiveness.append(typeRes)
    effectiveness.append(typeImm)

    return effectiveness

def print_effectiveness(e):
    m = '- 2x Weak: '
    w2 = e[0] ^ e[1]
    w2 = list(w2)
    m = m + w2[0]
    for item in w2[1:]:
        m = m + ', ' + item
    m = m + '\n'

    # 4x Weaknesses
    w4 = e[0] & e[1]
    w4 = list(w4)
    if len(w4) > 0:
        m = m + '- 4x Weak: '
        m = m + w4[0]
        for item in w4[1:]:
            m = m + ', ' + item
        m = m + '\n'

    m = m + '- 1/2x Resistant: '
    r2 = e[2] ^ e[3]
    r2 = list(r2)
    m = m + r2[0]
    for item in r2[1:]:
        m = m + ', ' + item
    m = m + '\n'

    # 1/4x Resistances
    r4 = e[2] & e[3]
    r4 = list(r4)
    if len(r4) > 0:
        m = m + '- 1/4x Resistant: '
        m = m + r4[0]
        for item in r4[1:]:
            m = m + ', ' + item
        m = m + '\n'

    m = m + '- Immunities: '
    imm = e[4] ^ e[5]
    imm = list(imm)
    if len(imm) > 0:
        if imm[0] == '':
            if len(imm) > 1:
                m = m + imm[1]
                if len(imm) > 2:
                    for item in imm[2:]:
                        m = m + ', ' + item
            else:
                m = m + 'None'
        else:
            m = m + imm[0]
            if len(imm) > 1:
                for item in imm[1:]:
                    m = m + ', ' + item
    else:
        m = m + 'None'
    m = m + '\n'

    return m

def print_effectiveness_mono(e):
    m = '- 2x Weak: '
    w2 = e[0]
    w2 = list(w2)
    m = m + w2[0]
    for item in w2[1:]:
        m = m + ', ' + item
    m = m + '\n'

    m = m + '- 1/2x Resistant: '
    r2 = e[1]
    r2 = list(r2)

    if r2[0] == '':
        if len(r2) > 1:
            m = m + r2[1]
            if len(r2) > 2:
                for item in r2[2:]:
                    m = m + ', ' + item
    else:
        m = m + r2[0]
        if len(r2) > 1:
            for item in r2[1:]:
                m = m + ', ' + item
    m = m + '\n'

    m = m + '- Immunities: '
    imm = e[2]
    imm = list(imm)
    if len(imm) > 0:
        if imm[0] == '':
            if len(imm) > 1:
                m = m + imm[1]
                if len(imm) > 2:
                    for item in imm[2:]:
                        m = m + ', ' + item
            else:
                m = m + 'None'
        else:
            m = m + imm[0]
            if len(imm) > 1:
                for item in imm[1:]:
                    m = m + ', ' + item
    else:
        m = m + 'None'
    m = m + '\n'

    return m
