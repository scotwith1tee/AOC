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
                #print("(%d, %d) \t\t %2d \t\t %s"
                #      % (i, j, dist[i][j], ' - '.join(str(p) for p in path)))
                pathes[i][j] = path

    #print()
    return pathes

def FindNumbersInString(string):    
    """Find all positive AND negative integers in a string """
    res = [int(d) for d in re.findall(r'-?\d+', string)]
    return res
def ConvertValveToIndex(name):
    global valves
    return valves[name]
def RunSim(start, valveOrder, time):
    global valves, pathes, flow, dist, activeFlow
    totFlow = 0
    flowPerMin = 0
    currNode = start
    targetNode = 1000
    valveIndex = 0
    waits = 0
    remTime = time

    for i in range(len(valveOrder)):
        timeToOpen = dist[currNode][valveOrder[i]]
        if(remTime <= timeToOpen+2):
            # Find another option
            break;
        else:
            timeUsed = timeToOpen + 1
            currNode = valveOrder[i]
            newFlow = activeFlow[valveOrder[i]-1]
        remTime -= timeUsed
        newFlowSum = flowPerMin * timeUsed
        flowPerMin += newFlow
        totFlow += newFlowSum

        #print('Min: ',30-remTime,' flowrate: ',flowPerMin, ' totFlow: ', totFlow,' Curr: ', currNode,' Target:',targetNode)

    # Add any remainging Time
    totFlow += remTime*flowPerMin
    # for m in range(1,31):
    #     totFlow += flowPerMin
    #     if targetNode > 500: # find next target  
    #         # Find the next valve. If we are out of valves just wait
    #         if valveIndex < len(valveOrder):
    #             targetNode = valveOrder[valveIndex]
    #             #check to see if we can get to the node and turn it on before time runs out
    #             # start to move to target down the first step towards the target
    #             currNode = pathes[currNode][targetNode][1]
    #             valveIndex += 1
    #         else:
    #             waits += 1
    #     elif currNode == targetNode:
    #         # Turn on the valve
    #         flowPerMin += flow[currNode]
    #         # Set the valve flow to zero so we don't find it later
    #         targetNode = 1000
    #     else:
    #         # we are in transit
    #         currNode = pathes[currNode][targetNode][1]
    #     #print('Min: ',m,' flowrate: ',flowPerMin, ' totFlow: ', totFlow,' Curr: ', currNode,' Target:',targetNode)
    return [totFlow, remTime]

def main():
    global valves, pathes, flow, dist, activeFlow 
    # Create the edge list
    #read in the data
    #with open('testinput.txt','r') as f:
    with open('input.txt','r') as f:
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

    #print(*edge_list, sep="\n")

    cont = floyd_warshall(edge_list)
    dist = cont[0]
    pathes = cont[1]
    # Find the active flow valves and make a new edge list to run through the path finding algorithm
    activeValves = []
    activeFlow = []
    # Create a list of valves we really care about with pressure
    for i in range(len(flow)):
        if flow[i] > 0:
            activeValves.append(i)
            activeFlow.append(flow[i])

    # Rebuild the edge list
    edge_list =[]
    # Start with AA to all valves with pressure
    # We also need to reindex for the path finding algorithm. index 0 is always AA
    start = valves['AA'] 
    for i in range(len(activeValves)):
        # Go both ways
        edge_list.append([0,i+1, dist[start][activeValves[i]]])
        edge_list.append([i+1, 0, dist[start][activeValves[i]]])
#        edge_list.append([start,activeValves[i], dist[start][activeValves[i]]])
    # Now make an edge list from all the pressure valves to each other
    for i in range(len(activeValves)):
        for j in range(len(activeValves)):
            if i != j:
                edge_list.append([i+1,j+1, dist[activeValves[i]][activeValves[j]]])
    
    # Recalulate all the distances and pathes. We really don't need paths anymore
    cont = floyd_warshall(edge_list)
    dist = cont[0]
    pathes = cont[1]





    #print(*dist, sep = "\n")
    #print(activeFlow)
    activeValves = [] 
    for i in range(len(activeFlow)):
        activeValves.append( i+1)
    active = []
    tmpFlow = list(activeFlow)
    tmpFlow.sort(reverse=True)
    # Pick the top flow valves to limit the problem
    for i in range(8):
        maxIndex = activeFlow.index(tmpFlow[i])
        active.append(activeValves[maxIndex])


    
    #active = [1,2,4,7,8,9,10,12,13,15]
    #active = [11, 10, 15, 1, 9]
    starting = [11, 7, 4, 10, 15, 1, 9, 13]
    #starting = [7, 4, 10, 15, 1, 9, 13]
    #starting = [11, 7, 4, 10, 15, 1]
    otherValves = []
    for i in range(len(activeValves)):
        if activeValves[i] in starting:
            print('')
        else:
            otherValves.append(activeValves[i])
            
    print('Other valves', otherValves)

    #[total, numWaits] = RunSim(0, active,30)
    # Create a list of all possible orders of the valves we care about
    #allIndexes = list(permutations(range(len(activeValves)), len(activeValves)))        
    #allValves = list(map(list, permutations(activeValves,8)))
    allValves = list(map(list, permutations(otherValves)))
    print('Combinations: ', len(allValves))
    print(activeFlow)
    maxFlow = 0
    for i in range(len(allValves)):

        [total, numWaits] = RunSim(0, starting + allValves[i],30)
        if total > maxFlow:
            maxFlow = total
            waits = numWaits
            bestValves = starting + allValves[i]
    print('Max Flow = ', maxFlow, ' Num Waits = ',waits)
    print('Winning Valves: ',bestValves)


    print("")



if __name__ == '__main__':
    main()