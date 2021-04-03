#! /usr/bin/env python

# Friday Night Funkin Randomizer by Nate Stutte
# Last updated 2-4-2021

import json
import string
import random
import os

def randomize(song, notes, character, order):

    # gf-christmas crashes :(
    characterlist = [
        'bf',
        'dad',
        'gf',
        'spooky',
        'pico',
        'mom',
        'mom-car',
        'bf-car',
        'parents-christmas',
        'monster-christmas',
        'bf-christmas',
        'monster',
        'bf-pixel',
        'senpai',
        'spirit'
    ]
    
    with open(song, 'r') as file:
        contents = file.read()
        data = ''.join(a for a in contents if a in string.printable)
        end = ''.join(a for a in contents if a not in string.printable)

    data = json.loads(data)

    if character:
        data['song']['player1'] = random.choice(characterlist)
        data['song']['player2'] = random.choice(characterlist)
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

    with open(song, 'w') as file:
        file.write(data + end)

def main():
    directories = [a for a in os.listdir('./assets/data') if '.' not in a and a != 'smash'] # smash doesn't work :(

    answer = {'y': True, 'n': False}

    notes = input("Randomize notes? (y/n)")
    if notes not in (['y'.lower(), 'n'.lower()]):
        print("Please use y/n!")
        notes = input("Randomize notes? (y/n)")
    notes = answer[notes]
    characters = input("Randomize characters? (y/n): ")
    if characters not in (['y'.lower(), 'n'.lower()]):
        print("Please use y/n!")
        characters = input("Randomize characters? (y/n): ")
    characters = answer[characters]
    order = input("Randomize sections to hit? (y/n): ")
    if order not in (['y'.lower(), 'n'.lower()]):
        print("Please use y/n!")
        order = input("Randomize sections to hit? (y/n): ")
    order = answer[order]

    if not notes and not characters and not order:
        print("What? If you didn't want to randomize anything why run this program?")
    else: 
        for a in directories:
            for b in os.listdir(f'./assets/data/{a}'):
                if '.txt' not in b:
                    print(f"Randomizing {b}")
                    randomize(f'assets/data/{a}/{b}', notes, characters, order)
                    print(f"{b} randomized")
        input("Successfully randomized. Please press ENTER...")

if __name__ == "__main__":
    main()