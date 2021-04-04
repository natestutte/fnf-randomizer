#! /usr/bin/env python

# Friday Night Funkin Randomizer by Nate Stutte
# Last updated 2-4-2021

import json
import string
import random
import os

def randomize(path, song, notes, character, order):

    # gf-christmas crashes :(
    characterlist = [a.rsplit() for a in open(f'{path}/assets/data/characterList.txt', 'r').readlines() if a != 'gf-christmas\n']
    print(characterlist)

    with open(f"{path}/{song}", 'r') as file:
        contents = file.read()
        data = ''.join(a for a in contents if a in string.printable)
        end = ''.join(a for a in contents if a not in string.printable)

    data = json.loads(data)

    if character:
        print(random.choice(characterlist))
        data['song']['player1'] = random.choice(characterlist)[0]
        data['song']['player2'] = random.choice(characterlist)[0]
    for a in data['song']['notes']:
        if order:
            a['mustHitSection'] = bool(random.getrandbits(1))
        if notes:
            a['sectionNotes'] = [list(t) for t in {tuple(item) for item in a['sectionNotes']}]
            for b in a['sectionNotes']:
                if b[1] > 3:
                    b[1] = random.randint(4, 7)
                else:
                    b[1] = random.randint(0, 3)
    for a in data['notes']:
        if order:
            a['mustHitSection'] = bool(random.getrandbits(1))
        if notes:
            a['sectionNotes'] = [list(t) for t in {tuple(item) for item in a['sectionNotes']}]
            for b in a['sectionNotes']:
                if b[1] > 3:
                    b[1] = random.randint(4, 7)
                else:
                    b[1] = random.randint(0, 3)

    data = json.dumps(data).replace(' ','')

    with open(f"{path}/{song}", 'w') as file:
        file.write(data + end)

def startRandomize(path, notes, chars, order):
    directories = [a for a in os.listdir(f"{path}/assets/data") if '.' not in a and a != 'smash'] # smash doesn't work :(

    for a in directories:
        for b in os.listdir(f"{path}/assets/data/{a}"):
            if '.txt' not in b:
                print(f"Randomizing {b}")
                randomize(path, f'assets/data/{a}/{b}', notes, chars, order)
                print(f"{b} randomized")