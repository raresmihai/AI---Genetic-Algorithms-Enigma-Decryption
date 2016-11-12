import random
import string
import re

def output(initial_text, encrypted_text, encryption_rule):
    print("Text before encryption is {0}".format(initial_text))
    print("Text after encryption is {0}".format(encrypted_text))
    print("The encryption rule applied is {0}".format(encryption_rule))

def encryption():
    encryption_rule = list(string.ascii_uppercase)
    random.shuffle(encryption_rule)
    with open("text_to_be_encrypted.txt") as fd:
        initial_text = list(fd.read().upper())
    for i in range(len(initial_text)):
        letter = initial_text[i]
        if letter.isalpha():
            index = ord(letter) - ord('A')
            initial_text[i] = encryption_rule[index]
    return "".join(initial_text)

def build_dictionary():
    with open("dictionary_input.txt","r",encoding='utf-8') as fd:
        input_dictionary = set(re.findall("\w+", fd.read().upper()))
    return input_dictionary

def generate_individuals():
    letters = list(string.ascii_uppercase)
    individuals = []
    individuals_count = 0
    while individuals_count < 100:
        indiv = list(letters)
        random.shuffle(indiv)
        if indiv not in individuals:
            individuals.append(indiv)
            individuals_count += 1
    return individuals

def print_individual():
    individuals = generate_individuals()
    print(individuals[0])

def decrypt(cryptotext,key):
    cryptotext = list(cryptotext)
    for i in range(len(cryptotext)):
        letter = cryptotext[i]
        if letter.isalpha():
            index = ord(letter) - ord('A')
            cryptotext[i] = key[index]
    return "".join(cryptotext)


def fitness(individual, cryptotext, dictionary):
    decryption = decrypt(cryptotext,individual)
    decrypted_words = re.findall("\w+", decryption)
    fitness = 0
    for word in decrypted_words:
        if word in dictionary:
            fitness += 1
    return fitness

def print_fitness_individuals():
    dict = ["ANA","ARE","MERE","PE","A","D","PA","NU","DA"]
    cryptotext = "MDM MRQ AQRQ Y B D C SU GF XC"
    individuals = generate_individuals()
    for indiv in individuals:
        print(fitness(indiv,cryptotext,dict),end=" ")


def order_by_fitness(individuals,cryptotext,dictionary):
    ordered_individuals = sorted(individuals,key = lambda x: fitness(x,cryptotext,dictionary))
    ordered_individuals = ordered_individuals[::-1]
    maximum_fitness = max(fitness(ordered_individuals[0],cryptotext,dictionary),1)
    individuals_with_fitness = dict()
    for individual in individuals:
        fi = fitness(individual,cryptotext,dictionary)/maximum_fitness
        individuals_with_fitness[individual] = fi
    return individuals_with_fitness


def solve():
    cryptotext = encryption()
    dictionary = build_dictionary()
    individuals = generate_individuals()
    ordered_individuals = order_by_fitness(individuals,cryptotext,dictionary)









def scor_turnir(individual, criptotext, dictionar):
    fitness_weight  = 0.7
    random_bonus_weight = 0.3
    random_bonus = random.random()
    scor = individual[1] * fitness_weight + random_bonus * random_bonus_weight
    return scor

def castigator(individual_1, individual_2):
    if scor_turnir(individual_1) > scor_turnir(individual_2):
        return individual_1
    else:
        return individual_2

def fight_turnir(individuals_1, individuals_2):
    if len(individuals_1) == 1 and len(individuals_2) == 1:
        return castigator(individuals_1, individuals_2)
    else:
        return fight_turnir(fight_turnir(individuals_1[0:len(individuals_1)/2-1], individuals_1[len(individuals_1)/2:]),
                            fight_turnir(individuals_2[0:len(individuals_2)/2-1], individuals_2[len(individuals_2)/2:]))
def turnir(individuals):
    random.shuffle(individuals)
    n = random.choice([2, 4, 8, 16, 32, 64])
    top_n_individuals = individuals[0:n-1]
    castigator = fight_turnir(top_n_individuals[0:n/2-1], top_n_individuals[n/2, n-1])
    return castigator

#solve()
#print (scor_turnir("","",""))
