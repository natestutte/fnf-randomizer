import json
import string
import random
import os

directories = os.listdir('./assets/data')
print(directories)
# with open('pico-hard.json', 'r') as file:
#     contents = file.read()
#     data = ''.join(a for a in contents if a in string.printable)
#     end = ''.join(a for a in contents if a not in string.printable)

# data = json.loads(data)

# for a in data['song']['notes']:
#     for b in a['sectionNotes']:
#         if b[1] > 3:
#             b[1] = random.randint(4, 7)
#         else:
#             b[1] = random.randint(0, 3)
# for a in data['notes']:
#     for b in a['sectionNotes']:
#         if b[1] > 3:
#             b[1] = random.randint(4, 7)
#         else:
#             b[1] = random.randint(0, 3)

# data = json.dumps(data)

# data = data.replace(' ','')

# with open('pico-hard.json', 'w') as file:
#     file.write(data + end)
