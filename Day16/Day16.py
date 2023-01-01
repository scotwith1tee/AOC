import sys
import re
from itertools import permutations

#INF = sys.maxsize
INF = 100

def floyd_warshall(graph):
    source_vertices = [column[0] for column in graph]
    destination_vertices = [column[1] for column in graph]
    vertices = list(set(source_vertices) | set(destination_vertices))

    distance = [[INF] * len(vertices) for i in range(len(vertices))]
    next_vertices  = [[0]   * len(vertices) for i in range(len(vertices))]

    for i in range(len(vertices)):
        distance[i][i] = 0
    for source, destination, weight in graph:
        distance[source][destination] = weight
        next_vertices[source][destination] = destination

    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_vertices[i][j]  = next_vertices[i][k]

    pathes = path_reconstruction(distance, next_vertices)
    return [distance, pathes]

def path_reconstruction(dist, nxt):
    print("Edge \t\t Distance \t Shortest Path")
    pathes = [[0 for j in range(len(dist))] for i in range(len(dist))] 
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i != j:
                path = [i]
                while path[-1] != j:
                    path.append(nxt[path[-1]][j])
                print("(%d, %d) \t\t %2d \t\t %s"
                      % (i, j, dist[i][j], ' - '.join(str(p) for p in path)))
                pathes[i][j] = path

    print()
    return pathes

def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res
def ConvertValveToIndex(name):
    global valves
    return valves[name]
def RunSim(start, valveOrder):
    global valves, pathes, flow 
    totFlow = 0
    flowPerMin = 0
    currNode = start
    targetNode = 1000
    valveIndex = 0
    waits = 0
    for m in range(1,31):
        totFlow += flowPerMin
        if targetNode > 500: # find next target  
            # Find the next valve. If we are out of valves just wait
            if valveIndex < len(valveOrder):
                targetNode = valveOrder[valveIndex]
                # start to move to target down the first step towards the target
                currNode = pathes[currNode][targetNode][1]
                valveIndex += 1
            else:
                waits += 1
        elif currNode == targetNode:
            # Turn on the valve
            flowPerMin += flow[currNode]
            # Set the valve flow to zero so we don't find it later
            targetNode = 1000
        else:
            # we are in transit
            currNode = pathes[currNode][targetNode][1]
        #print('Min: ',m,' flowrate: ',flowPerMin, ' totFlow: ', totFlow,' Curr: ', currNode,' Target:',targetNode)
    return totFlow
def main():
    global valves, pathes, flow 
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
        start = line.find('valves')+7
        if start < 7:
            start = line.find('valve')+6

        #always one destination
        dest = line[start:start+2]
        edge_list.append([i,valves[dest], 1])

        # Look for more destinations
        while(line.find(',',start)>=0):
            start = line.find(',',start) + 2
            dest = line[start:start+2]
            edge_list.append([i,valves[dest], 1])

    print(*edge_list, sep="\n")

    cont = floyd_warshall(edge_list)
    dist = cont[0]
    pathes = cont[1]

    activeValves = []
    activeFlow = []
    # Create a list of valves we really care about with pressure
    for i in range(len(flow)):
        if flow[i] > 0:
            activeValves.append(i)
            activeFlow.append(flow[i])
    active = []
    tmpFlow = list(activeFlow)
    tmpFlow.sort(reverse=True)
    # Pick the top flow valves to limit the problem
    for i in range(6):
        maxIndex = activeFlow.index(tmpFlow[i])
        active.append(activeValves[maxIndex])

    

    # Create a list of all possible orders of the valves we care about
    #allIndexes = list(permutations(range(len(activeValves)), len(activeValves)))        
    allValves = list(map(list, permutations(active)))
    print('Found all the combos')

    maxFlow = 0
    for i in range(len(allValves)):
        total = RunSim(valves['AA'], allValves[i])
        if total > maxFlow:
            maxFlow = total
    print('Max Flow = ', maxFlow)

    # We should have everything we need to calculate the optimal valve openings
    totFlow = 0
    flowPerMin = 0
    currNode = valves['AA']
    targetNode = 1000
    weight = [0] * len(dist[0])
    for m in range(1,31):
        totFlow += flowPerMin
        if targetNode > 500: # find a new target  
            # find the best valve option from where I am right now
            # divide the flow by the distance to the valve
            valvesAvail = False
            for i in range(len(dist[currNode])):
                if dist[currNode][i] == 0 or flow[i] == 0:
                    weight[i] = 0
                else:
                    weight[i] = flow[i]/dist[currNode][i]
                    valvesAvail = True # We found a valve with pressure
            # if there are no more valves with pressure just wait
            if valvesAvail == True:
                #find the max index
                targetNode = weight.index(max(weight))
                # start to move to target down the first step towards the target
                currNode = pathes[currNode][targetNode][1]
        elif currNode == targetNode:
            # Turn on the valve
            flowPerMin += flow[currNode]
            # Set the valve flow to zero so we don't find it later
            flow[currNode] = 0
            targetNode = 1000
        else:
            # we are in transit
            currNode = pathes[currNode][targetNode][1]
        print('Min: ',m,' flowrate: ',flowPerMin, ' totFlow: ', totFlow,' Curr: ', currNode,' Target:',targetNode)






    print("")



if __name__ == '__main__':
    main()