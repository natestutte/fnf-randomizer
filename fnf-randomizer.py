#! /usr/bin/env python

import json
import string
import random
import os

def randomize(song):
    with open(song, 'r') as file:
        contents = file.read()
        data = ''.join(a for a in contents if a in string.printable)
        end = ''.join(a for a in contents if a not in string.printable)

    data = json.loads(data)

    for a in data['song']['notes']:
        for b in a['sectionNotes']:
            if b[1] > 3:
                b[1] = random.randint(4, 7)
            else:
                b[1] = random.randint(0, 3)
    for a in data['notes']:
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

    for a in directories:
        for b in os.listdir(f'./assets/data/{a}'):
            print(f"Randomizing {b}")
            randomize(f'assets/data/{a}/{b}')
            print(f"{b} randomized")
    input("Successfully randomized. Please press ENTER...")

if __name__ == "__main__":
    main()