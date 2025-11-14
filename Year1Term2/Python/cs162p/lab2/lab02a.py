import sys



filename : str = sys.argv[1]

try:
    file = open(filename, 'r')
    people : list = []
    iter : int = 0

    while (True):
        line : str = file.readline()
        
        if not line: break
        
        # Check for first line
        if line[0] == '#': continue

        # Separate data
        info : str = line.split("|")
        id : str = info[0]
        name : str = info[1]
        age : str = info[2]
        job : str = info[3]
        wage : str = info[4]

        person : str = age + '|' + name
        people.append(person)

    file.close()

    people.sort()

    for i in range(len(people)):
        split : str = people[i].split('|')
        age : str = split[0]
        name : str = split[1]

        # Am I supposed to be using the splits? This works either way.
        print(people[i])

except:
    print("Ah shit, I messed up.")