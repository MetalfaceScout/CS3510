import heapq

def minCostSupplyWater(nwells : int, wells: list, pipes: list):
    graph = buildGraph(nwells, wells, pipes)
    return findMST(graph, nwells)


def buildGraph(nwells, wells, pipes):

    #start node has an edge of "well cost" weight to each house

    '''
            (S)
            | |
          (H) (H)
    '''

    graph = {}
    graph[0] = {}
    #add starting edges from wells to node 0
    for i, well in enumerate(wells):
        graph[0][i+1] = well

    #setup graph with empty dictionaries
    for i in range(len(pipes)):
        graph[i+1] = {}

    #add pipe edges
    for pipe in pipes:
        housesrc = pipe[0]
        housedest = pipe[1]
        cost = pipe[2]

        #does an edge with a lower weight already exist? if so, don't add this one
        try:
            if graph[housesrc][housedest] < cost:
                continue
        except KeyError:
            pass

        #add edge from source to destination
        try:
            graph[housesrc].update({housedest : cost})
        except KeyError:
            graph[housesrc] = {housedest : cost}

        #see if an edge already exists again (likely unnessicary)
        try:
            if graph[housedest][housesrc] < cost:
                continue
        except KeyError:
            pass
        
        #add edge from dest to source
        try:
            graph[housedest].update({housesrc : cost})
        except KeyError:
            graph[housedest] = {housesrc : cost}
    
    return graph

def findMST(graph, nwells):
    min_queue = []

    visited = set()
    t_cost = 0

    heapq.heappush(min_queue, (0,0)) #(cost, node)

    while len(visited) < nwells + 1:
        cost, house = heapq.heappop(min_queue)

        if house in visited:
            continue

        visited.add(house)
        t_cost += cost

        for neighbor_key in graph[house]:
            n_cost = graph[house][neighbor_key]
            if neighbor_key not in visited:
                heapq.heappush(min_queue, (n_cost, neighbor_key))
    
    return t_cost



if __name__ == "__main__":
    testoneresult = minCostSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]])
    print(f"Test 1: {testoneresult}")

    testtworesult = minCostSupplyWater(4, [1,2,2,1], [[1,2,1], [1,2,3], [2,3,2], [3,4,3], [1,4,2]])
    print(f"Test 2: {testtworesult}")

    testthreeresult = minCostSupplyWater(5, [10, 2, 2, 10, 2], [[1,2,1], [2,3,1], [3,4,1], [1,4,2], [2,5,2]])
    print(f"Test 3: {testthreeresult}")