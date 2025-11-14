import sys
from operator import itemgetter

def print_sorted_list(sorted_list, key_name):
    print(f"Sorted by {key_name}")
    for item in sorted_list:
        print(f"Name: {item[0]} | Class: {item[1]} \n\t Str: {item[2]} Dex: {item[3]} Int:{item[4]} Chr:{item[5]}")

filename = sys.argv[1]

file = open(filename, 'r')

characters = dict()
count = 0

# Gather data from file 
while(True):
    line = file.readline()
    
    # Handle edge cases
    if not line: break
    if line[0] == '#': continue

    data = line.split('|')
    char_name = data[0]
    char_class = data[1]
    char_str = data[2]
    char_dex = data[3]
    char_int = data[4]
    char_chr = data[5]

    characters[count] = [char_name, char_class, char_str, char_dex, char_int, char_chr]
    count += 1

file.close()

##### Main Program #####
characters_list = list()

# Gather list of tuples
for key in characters.keys():
    characters_list.append(characters[key])

# Sort by name
sorted_list = sorted(characters_list, key=itemgetter(0))
print_sorted_list(sorted_list, "name")

# Sort by class
sorted_list = sorted(characters_list, key=itemgetter(1))
print_sorted_list(sorted_list, "Class")

# Sort by strength
sorted_list = sorted(characters_list, key=itemgetter(2))
print_sorted_list(sorted_list, "Strength Value")

# Sort by dex
sorted_list = sorted(characters_list, key=itemgetter(3))
print_sorted_list(sorted_list, "Dexterity Value")