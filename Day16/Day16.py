import sys
import re

INF = sys.maxsize

def floyd_warshall(graph):
    source_vertices = [column[0] for column in graph]
    destination_vertices = [column[1] for column in graph]
    vertices = list(set(source_vertices) | set(destination_vertices))

    distance = [[INF] * len(vertices) for i in range(len(vertices))]
    next_vertices  = [[0]   * len(vertices) for i in range(len(vertices))]

    for i in range(len(vertices)):
        distance[i][i] = 0
    for source, destination, weight in graph:
        distance[source-1][destination-1] = weight
        next_vertices[source-1][destination-1] = destination-1

    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_vertices[i][j]  = next_vertices[i][k]

    path_reconstruction(distance, next_vertices)

def path_reconstruction(dist, nxt):
    print("Edge \t\t Distance \t Shortest Path")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i != j:
                path = [i]
                while path[-1] != j:
                    path.append(nxt[path[-1]][j])
                print("(%d, %d) \t\t %2d \t\t %s"
                      % (i + 1, j + 1, dist[i][j], ' - '.join(str(p + 1) for p in path)))
    print()

def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res
def ConvertValveToIndex(name):
    global valves
    return valves[name]

def main():

    # Create the edge list
    #read in the data
    with open('testinput.txt','r') as f:
    #with open('input.txt','r') as f:
        array = f.readlines()
    f.close()

    edge_list =[]
    valves = {} # Names of the valves indexed in dict

    flow = []
    # loop through the input to find all the valves
    for i in range(len(array)):
        valves[array[i][6:8]]=i
        flow.append(FindNumbersInString(array[i])[0])
    # lets build the edge list
    for i in range(len(array)):
        line = array[i]
        #find first valve
        start = line.find('valves') + 7
        #always one destination
        dest = line[start:start+2]
        edge_list.append([i,valves[dest], 1])

        # Look for more destinations
        while(line.find(',',start)>=0):
            start = line.find(',',start) + 2
            dest = line[start:start+2]
            edge_list.append([i,valves[dest], 1])

    print(edge_list)


    edge_list1 = [
        [1, 3, -2],
        [2, 1, 4],
        [2, 3, 3],
        [3, 4, 2],
        [4, 2, -1]
    ]
    edge_list2 = [
        [1, 2, 10],
        [1, 3, 20],
        [1, 4, 30],
        [2, 6, 7],
        [3, 6, 5],
        [4, 5, 10],
        [5, 1, 2],
        [5, 6, 4],
        [6, 2, 5],
        [6, 3, 7],
        [6, 5, 6]
    ]

    floyd_warshall(edge_list1)
    floyd_warshall(edge_list2)

if __name__ == '__main__':
    main()