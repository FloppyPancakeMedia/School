import sys

## Calculates average rate for professions in document. Prints professions in alphabetical order along with rates. ##

filename : str = sys.argv[1]

try:
    file = open(filename, 'r')
    tempJobDict : dict[str, list[float]] = {}

    # Get data necessary for calculation and store in temp dict
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
        wage : float = float(info[4])

        # Populate data
        if job not in tempJobDict:
            tempJobDict[job] = []
        tempJobDict[job].append(wage)

    # Create new dict for data we want to print
    jobWageAverage : dict[str, float] = {}
    for key in tempJobDict.keys():

        jobWageAverage[key] = 0
        average : float = 0

        numOfWages : int = 0
        # Calculate average for job
        for wage in tempJobDict[key]:
            average += wage
            numOfWages += 1
        average /= numOfWages

        jobWageAverage[key] = average
    
    sortedList : list = []
    for key in jobWageAverage.keys():
        sortedList.append(f"{key} on average makes about ${jobWageAverage[key]:.2f}")
    
    sortedList.sort()
    for item in sortedList:
        print(item)
        
except Exception as e:
    print("that's no good...")
    print(e)
