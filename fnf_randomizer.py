#! /usr/bin/env python

# Friday Night Funkin Randomizer by Nate Stutte
# Last updated 2-4-2021

import json
import string
import random
import os

def randomize(path, song, notes, character, order):

    # gf-christmas crashes :(
    try:    
        characterlist = [a.rsplit() for a in open(f'{path}/assets/data/characterList.txt', 'r').readlines() if a != 'gf-christmas\n']

        with open(f"{path}/{song}", 'r') as file:
            contents = file.read()
            data = ''.join(a for a in contents if a in string.printable)
            end = ''.join(a for a in contents if a not in string.printable)

        data = json.loads(data)

        if character:
            print(random.choice(characterlist))
            data['song']['player1'] = random.choice(characterlist)[0]
            data['song']['player2'] = random.choice(characterlist)[0]
        if 'song' in data:
            if 'notes' in data['song']:
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
        if 'notes' in data:
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
    except: 
        return f"Could not properly randomize {song}"
    return ""

def startRandomize(path, notes, chars, order):
    try:
        directories = [a for a in os.listdir(f"{path}/assets/data") if '.' not in a and a != 'smash'] # smash doesn't work :(

        status = ""

        for a in directories:
            for b in os.listdir(f"{path}/assets/data/{a}"):
                if '.txt' not in b:
                    print(f"Randomizing {b}")
                    rstatus = randomize(path, f'assets/data/{a}/{b}', notes, chars, order)
                    if rstatus != "":
                        status += rstatus + "\n"
                    print(f"{b} randomized")
    except FileNotFoundError:
        return "Randomization Failed!\n\nCould not locate proper FNF files"
    return f"{status}\nSuccesfully Randomized!"