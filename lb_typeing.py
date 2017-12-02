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

def print_effectiveness(e):
    m = '2x Weak: '
    w2 = e[0] ^ e[1]
    w2 = list(w2)
    m = m + w2[0]
    for item in w2[1:]:
        m = m + ', ' + item
    m = m + '\n'

    m = m + '4x Weak: '
    w4 = e[0] & e[1]
    w4 = list(w4)
    m = m + w4[0]
    for item in w4[1:]:
        m = m + ', ' + item
    m = m + '\n'

    m = m + '1/2x Resistant: '
    r2 = e[2] ^ e[3]
    r2 = list(r2)
    m = m + r2[0]
    for item in r2[1:]:
        m = m + ', ' + item
    m = m + '\n'

    m = m + '1/4x Resistant: '
    r4 = e[2] & e[3]
    r4 = list(r4)
    m = m + r4[0]
    for item in r4[1:]:
        m = m + ', ' + item
    m = m + '\n'

    m = m + 'Immunities: '
    imm = e[4] ^ e[5]
    imm = list(imm)
    m = m + imm[0]
    for item in imm[1:]:
        m = m + ', ' + item
    m = m + '\n'

    return m
