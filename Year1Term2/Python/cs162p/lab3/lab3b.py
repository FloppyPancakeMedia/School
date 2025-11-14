import sys

## Takes a data file, max hop limit, source node, and destination node as arguments
## Reads from data file to determine default delay from source to destination
## then tries to find more efficient route


## Find all possible paths from start to destination and compare, choose lowest


def parse_data() -> dict[str, dict[str, float]]:
    new_dict : dict[str, dict[str, float]] = {}
    # Create dictionary with source(str) : data for more efficient searching
    while True:
        line : str = data_file.readline()

        # Handle errant conditions #
        if not line: break
        # Skip first line
        if line[0] == '#': continue
        ############################

        splitData = line.split("|")
        if splitData[0] not in new_dict:
            new_dict[splitData[0]] = {}
        
        # Slice delay time out of splitData
        delay_time_input : float
        cost_and_time = splitData[2].split(',')
        delay_time_input = float(cost_and_time[1][6:])
        new_dict[splitData[0]][splitData[1]] = delay_time_input
        
    return new_dict


def get_default_delay(start, end) -> float:
    return data[start][end]


def get_all_paths(paths : dict[int : list[str]], start: str, destination : str, max_hops : int):
    # Create base case
    if max_hops == 0: return paths
    print("Max hops = %s. Paths now: %s" % (max_hops, paths))
    # Loop through all possible destinations from given start
    for dest in data[start]:
        print("Destination: %s" % dest)
        for i in paths.keys():
            if dest in paths[i]:
                continue
            elif dest == destination:
                paths[i].append(dest)
                return
            elif destination in paths[i]:
                continue
            else:
                paths[i].append(dest)
                get_all_paths(paths, dest, destination, max_hops - 1)


def get_best_path(start, end, max_hops, path : str, delay_time):
    # We use this dict to store "1 : [all nodes in path]", "2 : [all nodes in path]", etc
    all_paths : dict[int : list[str]] = {}
    index : int = 1
    # Determine num of paths available
    for dest in data[start]:
        all_paths[index] = [start]
        index += 1
    # This dict will store "1 : delay_time", "2 : delay_time", etc
    path_delays : dict[int : float] = {}
    all_paths = get_all_paths(all_paths, start, end, max_hops)
    print(all_paths)


data_file_name : str = sys.argv[1]
desired_max_hops : int = int(sys.argv[2])
source_node : str = sys.argv[3]
dest_node : str = sys.argv[4]

try:
    data_file = open(data_file_name, 'r')

    data : dict[str, dict[str, float]] = parse_data()
    def_delay : float = get_default_delay(source_node, dest_node)
    print("Default delay to destination: " + str(def_delay))

    start_path : str = source_node
    start_delay_time = 0
    # print(getBestPath(data, sourceNode, destNode, maxHops))
    print(get_best_path(source_node, dest_node, desired_max_hops, start_path, start_delay_time))
    
    

except Exception as e:
    print("An error has occurred: %s" % e)