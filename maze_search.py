maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
S = (11,2)
E1 = (19,23)
E2 = (21,2)
# Populate graph of adjacencies
nodes = []
for rowInd in range(len(maze)):
    row = []
    for colInd in range(len(maze[0])):
        if(maze[rowInd][colInd] == 0):
            possiblePaths = []
            if(rowInd -1 > -1 and maze[rowInd-1][colInd] == 0):
                possiblePaths.append((rowInd-1,colInd))
            if(rowInd +1 < len(maze) and maze[rowInd+1][colInd] == 0):
                possiblePaths.append((rowInd+1,colInd))
            if(colInd + 1 < len(maze[0]) and maze[rowInd][colInd+1] == 0):
                possiblePaths.append((rowInd,colInd+1))
            if(colInd -1 > -1 and maze[rowInd][colInd-1] == 0):
                possiblePaths.append((rowInd,colInd-1))
            row.append(possiblePaths)
        else:
            row.append(None)
    nodes.append(row)

def BFS(start, finish, nodes):
    nodesExplored = 1
    firstNode = {
        'node': start,
        'cost': 1,
        'prev': []
    }
    Q = [firstNode]
    # Since all cost is equal, if it was visited before it is extreneous because there would have been a better solution found already
    visited = []
    while(finish != Q[0]['node']):
        # Skip when it was already visited
        if(Q[0]['node'] in visited):
            Q = Q[1:]
            continue
        nodesExplored += 1
        expanded = Q[0]
        visited.append(expanded['node'])
        Q = Q[1:]
        for i in nodes[expanded['node'][0]][expanded['node'][1]]:
            if(i not in visited):
                Q.append({
                    'node': i,
                    'cost': expanded['cost']+1,
                    'prev': expanded['prev']+[expanded['node']]
                })
    Q[0]['prev'].append(finish)
    return {
        'path': Q[0]['prev'],
        'cost': Q[0]['cost'],
        'nodesExplored':nodesExplored
    }

def DFS(start, finish, nodes):
    nodesExplored = 1
    firstNode = {
        'node': start,
        'cost': 1,
        'prev': []
    }
    Q = [firstNode]
    # Since all cost is equal, if it was visited before it is extreneous because there would have been a better solution found already
    visited = []
    while(finish != Q[0]['node']):
        # Skip when it was already visited
        if(Q[0]['node'] in visited):
            Q = Q[1:]
            continue
        nodesExplored += 1
        expanded = Q[0]
        visited.append(expanded['node'])
        Q = Q[1:]
        for i in nodes[expanded['node'][0]][expanded['node'][1]]:
            if(i not in visited):
                node = {
                    'node': i,
                    'cost': expanded['cost']+1,
                    'prev': expanded['prev']+[expanded['node']]
                }
                Q = [node] + Q
    Q[0]['prev'].append(finish)
    return {
        'path': Q[0]['prev'],
        'cost': Q[0]['cost'],
        'nodesExplored':nodesExplored
    }

def AStar(start,finish,nodes):
    nodesExplored = 1
    firstNode = {
        'node': start,
        'cost': 1,
        'prev': []
    }
    Q = [firstNode]
    # Since all cost is equal, if it was visited before it is extreneous because there would have been a better solution found already
    visited = []

    while(findLowest(Q,finish)['node'] != finish):
        # Skip when it was already visited
        lowest = findLowest(Q,finish)
        if(lowest['node'] in visited):
            Q.remove(lowest)
            continue
        nodesExplored += 1
        expanded = lowest
        visited.append(expanded['node'])
        Q.remove(lowest)
        for i in nodes[expanded['node'][0]][expanded['node'][1]]:
            if(i not in visited):
                Q.append({
                    'node': i,
                    'cost': expanded['cost']+1,
                    'prev': expanded['prev']+[expanded['node']]
                })
    lowest = findLowest(Q,finish)
    lowest['prev'].append(finish)
    return {
        'path': lowest['prev'],
        'cost': lowest['cost'],
        'nodesExplored':nodesExplored
    }

def findLowest(Q, finish):
    # Get the closest node
    curLeast = Q[0]['cost']+heuristic(Q[0]['node'],finish)
    curLeastNode = Q[0]
    for i in range(len(Q)):
        if(Q[i]['cost']+heuristic(Q[i]['node'],finish) < curLeast):
            curLeast = Q[i]['cost']+heuristic(Q[i]['node'],finish)
            curLeastNode = Q[i]
    return curLeastNode

def heuristic(current, end):
    return abs(current[0]-end[0]) + abs(current[1]-end[1])

# Testing
methodStrings = ['BFS', 'DFS', 'A*']
methods = [BFS, DFS, AStar]
cases = [(S,E1),(S,E2),((0,0),(24,24))]
caseStrings = ['S to E1', 'S to E2', '(0,0) to (24,24)']
for methodInd in range(len(methods)):
    for caseInd in range(len(cases)):
        print('For the ' + methodStrings[methodInd] + ' method and using the case of ' + caseStrings[caseInd] + ':')
        print(methods[methodInd](cases[caseInd][0], cases[caseInd][1], nodes))
        print('\n')
