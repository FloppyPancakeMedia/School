import sys

## Counts the number of people with a certain age in a file ##

filename : str = sys.argv[1]

ages_of_folks : dict[int, int] = dict()

try:
    # What type of data is a file?
    file = open(filename, 'r')

    while(True):
        info : str = file.readline()
        
        # Handle beg/end of input
        if not info: break
        if info[0] == '#': continue

        separated_info : list = info.split('|')

        age : int = int(separated_info[2])
        if age not in ages_of_folks:
            ages_of_folks[age] = 1
        else:
            ages_of_folks[age] += 1

    # Calculate 
    for i in ages_of_folks.keys():
        data : str = "Age: " + str(i) + " contains: " + str(ages_of_folks[i]) + " people"
        print(data)

    file.close()

except:
    print("Poop, something went wrong")
