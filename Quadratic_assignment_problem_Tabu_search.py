import math
import random
flow = [
    [0,	0,	5,	0,	5,	2,	10,	3,	1,	5,	5,	5,	0,	0,	5,	4,	4,	0,	0,	1],
    [0	,0	,3	,10	,5	,1	,5	,1	,2	,4	,2	,5	,0	,10	,10	,3	,0	,5	,10,	5],
    [5	,3	,0	,2	,0	,5	,2	,4	,4	,5	,0	,0	,0	,5	,1	,0	,0	,5	,0	,0],
    [0	,10	,2	,0	,1	,0	,5	,2	,1	,0	,10	,2	,2	,0	,2	,1	,5	,2	,5	,5],
    [5	,5	,0	,1	,0	,5	,6	,5	,2	,5	,2	,0	,5	,1	,1	,1	,5	,2	,5	,1],
    [2	,1	,5	,0	,5	,0	,5	,2	,1	,6	,0	,0	,10	,0	,2	,0	,1	,0	,1	,5],
    [10	,5	,2	,5	,6	,5	,0	,0	,0	,0	,5	,10	,2	,2	,5	,1	,2	,1	,0	,10],
    [3	,1	,4	,2	,5	,2	,0	,0	,1	,1	,10	,10	,2	,0	,10	,2	,5	,2	,2	,10],
    [1	,2	,4	,1	,2	,1	,0	,1	,0	,2	,0	,3	,5	,5	,0	,5	,0	,0	,0	,2],
    [5	,4	,5	,0	,5	,6	,0	,1	,2	,0	,5	,5	,0	,5	,1	,0	,0	,5	,5	,2],
    [5	,2	,0	,10	,2	,0	,5	,10	,0	,5	,0	,5	,2	,5	,1	,10	,0	,2	,2	,5],
    [5	,5	,0	,2	,0	,0	,10	,10	,3	,5	,5	,0	,2	,10	,5	,0	,1	,1	,2	,5],
    [0	,0	,0	,2	,5	,10	,2	,2	,5	,0	,2	,2	,0	,2	,2	,1	,0	,0	,0	,5],
    [0	,10	,5	,0	,1	,0	,2	,0	,5	,5	,5	,10	,2	,0	,5	,5	,1	,5	,5	,0],
    [5	,10	,1	,2	,1	,2	,5	,10	,0	,1	,1	,5	,2	,5	,0	,3	,0	,5	,10,	10],
    [4	,3	,0	,1	,1	,0	,1	,2	,5	,0	,10	,0	,1	,5	,3	,0	,0	,0	,2	,0],
    [4	,0	,0	,5	,5	,1	,2	,5	,0	,0	,0	,1	,0	,1	,0	,0	,0	,5	,2	,0],
    [0	,5	,5	,2	,2	,0	,1	,2	,0	,5	,2	,1	,0	,5	,5	,0	,5	,0	,1	,1],
    [0	,10	,0	,5	,5	,1	,0	,2	,0	,5	,2	,2	,0	,5	,10	,2	,2	,1	,0	,6],
    [1	,5	,0	,5	,1	,5	,10	,10	,2	,2	,5	,5	,5	,0	,10	,0	,0	,1	,6	,0],
]

distance = [
    [0,	1,	2,	3,	4,	1,	2,	3,	4	,5,	2,	3,	4,	5,	6,	3,	4,	5,	6,	7],
    [1,	0,	1,	2,	3,	2,	1,	2,	3	,4,	3,	2,	3,	4,	5,	4,	3,	4,	5,	6],
    [2,	1,	0,	1,	2,	3,	2,	1,	2	,3,	4,	3,	2,	3,	4,	5,	4,	3,	4,	5],
    [3,	2,	1,	0,	1,	4,	3,	2,	1	,2,	5,	4,	3,	2,	3,	6,	5,	4,	3,	4],
    [4,	3,	2,	1,	0,	5,	4,	3,	2	,1,	6,	5,	4,	3,	2,	7,	6,	5,	4,	3],
    [1,	2,	3,	4,	5,	0,	1,	2,	3	,4,	1,	2,	3,	4,	5,	2,	3,	4,	5,	6],
    [2,	1,	2,	3,	4,	1,	0,	1,	2	,3,	2,	1,	2,	3,	4,	3,	2,	3,	4,	5],
    [3,	2,	1,	2,	3,	2,	1,	0,	1	,2,	3,	2,	1,	2,	3,	4,	3,	2,	3,	4],
    [4,	3,	2,	1,	2,	3,	2,	1,	0	,1,	4,	3,	2,	1,	2,	5,	4,	3,	2,	3],
    [5,	4,	3,	2,	1,	4,	3,	2,	1	,0,	5,	4,	3,	2,	1,	6,	5,	4,	3,	2],
    [2,	3,	4,	5,	6,	1,	2,	3,	4	,5,	0,	1,	2,	3,	4,	1,	2,	3,	4,	5],
    [3,	2,	3,	4,	5,	2,	1,	2,	3	,4,	1,	0,	1,	2,	3,	2,	1,	2,	3,	4],
    [4,	3,	2,	3,	4,	3,	2,	1,	2	,3,	2,	1,	0,	1,	2,	3,	2,	1,	2,	3],
    [5,	4,	3,	2,	3,	4,	3,	2,	1	,2,	3,	2,	1,	0,	1,	4,	3,	2,	1,	2],
    [6,	5,	4,	3,	2,	5,	4,	3,	2	,1,	4,	3,	2,	1,	0,	5,	4,	3,	2,	1],
    [3,	4,	5,	6,	7,	2,	3,	4,	5	,6,	1,	2,	3,	4,	5,	0,	1,	2,	3,	4],
    [4,	3,	4,	5,	6,	3,	2,	3,	4	,5,	2,	1,	2,	3,	4,	1,	0,	1,	2,	3],
    [5,	4,	3,	4,	5,	4,	3,	2,	3	,4,	3,	2,	1,	2,	3,	2,	1,	0,	1,	2],
    [6,	5,	4,	3,	4,	5,	4,	3,	2	,3,	4,	3,	2,	1,	2,	3,	2,	1,	0,	1],
    [7,	6,	5,	4,	3,	6,	5,	4,	3	,2,	5,	4,	3,	2,	1,	4,	3,	2,	1,	0]
]

initialSolution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Top right half is to show tabu tenure of the swaps in short term memory, and bottom left is for long term frequency
tabuListMatrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]



# Solution is array of numbers from 1-20
def calcCost(solution, useFrequency=None, frequency=None):
    cost = 0
    for ind in range(len(solution)):
        for ind2 in range(ind, len(solution)):
            dep1 = solution[ind]
            dep2 = solution[ind2]
            cost += distance[ind-1][ind2-1]*flow[dep1-1][dep2-1]
    if(useFrequency):
        cost += frequency
    return cost

def swap(solution, i, j):
    solution[i], solution[j] = solution[j], solution[i]
    return solution

# all neighboring solutions
def neighborhoodSwaps(solution, useLessNeighborhood):
    swaps = []
    count = 0
    for i in range(len(solution)):
        for j in range(i, len(solution)):
            if(i!= j and not useLessNeighborhood):
                swaps.append([i,j])
            elif(i!= j and useLessNeighborhood and count % 2 == 0):
                swaps.append([i,j])
            count += 1
    return swaps

def tabuSearch(solution, tabuSize, tabuTenure, maxIterations, useFrequency=None, isDynamicList=None, useAspiration1=None, useAspiration2=None, useLessNeighborhood = None):
    tabuList = []
    iteration = 0
    globalBest = math.inf
    while(iteration < maxIterations):
        if(isDynamicList and iteration % 20 == 0):
            # random size from 1-30
            tabuSize = 1 + round(random.random()*29)
        nSwaps = neighborhoodSwaps(solution, useLessNeighborhood)
        bestSwap = nSwaps[0]
        # assign initial
        bestSol = None
        bestCost = math.inf
        for swapSol in nSwaps:
            if(not useAspiration1 and not useAspiration2):
                if swapSol not in tabuList:
                    if(calcCost(swap(solution[:],swapSol[0],swapSol[1]), useFrequency, tabuListMatrix[swapSol[1]][swapSol[0]]) < bestCost):
                        bestCost = calcCost(swap(solution[:],swapSol[0],swapSol[1]))
                        bestSol = swap(solution[:],swapSol[0],swapSol[1])
                        bestSwap = swapSol
            # global best aspiration
            elif(useAspiration1):
                if (swapSol not in tabuList or calcCost(swap(solution[:],swapSol[0],swapSol[1]), useFrequency, tabuListMatrix[swapSol[1]][swapSol[0]]) < globalBest):
                    if(calcCost(swap(solution[:],swapSol[0],swapSol[1]), useFrequency, tabuListMatrix[swapSol[1]][swapSol[0]]) < bestCost):
                        bestCost = calcCost(swap(solution[:],swapSol[0],swapSol[1]))
                        bestSol = swap(solution[:],swapSol[0],swapSol[1])
                        bestSwap = swapSol
            
            # best in neighborhood
            elif(useAspiration2):
                if(calcCost(swap(solution[:],swapSol[0],swapSol[1]), useFrequency, tabuListMatrix[swapSol[1]][swapSol[0]]) < bestCost):
                    bestCost = calcCost(swap(solution[:],swapSol[0],swapSol[1]))
                    bestSol = swap(solution[:],swapSol[0],swapSol[1])
                    bestSwap = swapSol
        #add bestSwap to tabuList
        tabuList.append(bestSwap)
        tabuListMatrix[bestSwap[0]][bestSwap[1]] = tabuTenure
        if(useFrequency):
            tabuListMatrix[bestSwap[1]][bestSwap[0]] += 1
        

        # if tabulist is too big then forcefully decrement the closest one to 0 and remove it
        if(len(tabuList) > tabuSize):
            while(len(tabuList) > tabuSize):
                tabuListMatrix[tabuList[0][0]][tabuList[0][1]] = 0
                tabuList = tabuList[1:]
        
        # decrement tenure by 1 in tabulist
        for tabu in tabuList:
            tabuListMatrix[tabu[0]][tabu[1]] -= 1
            # remove if it has 0 tenure
            if(tabuListMatrix[tabu[0]][tabu[1]] == 0):
                tabuList = tabuList[1:]
        if(bestSol != None):
            solution =  bestSol[:]
        iteration += 1
        
    return solution

def generateInitialPoints(n, initial):
    solutions = []
    for i in range(n):
        temp = initial[:]
        solution = []
        while(len(temp) > 0):
            randind = math.floor(random.random()*len(temp))
            solution.append(temp[randind])
            temp = temp[:randind] + temp[randind+1:]
        solutions.append(solution)
    return solutions


## for part 2
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500)
print('final solution:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## Part 3.1
randomInitialSolutions = generateInitialPoints(10,initialSolution)
for i in randomInitialSolutions:
    print('initial solution:')
    print(i)
    solution = tabuSearch(i,5,5,500)
    print('final solution:')
    print(solution)
    print('cost:')
    print(calcCost(solution))
    print('\n')

## Part 3.2
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,2,2,500)
print('final solution with tabu size of 2:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,30,30,500)
print('final solution with tabu size of 30:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## part 3.3
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500,None,True)
print('final solution with dynamic list:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## Part 3.4.1 global best aspiration
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500,None,None,True)
print('final solution with global best aspiration:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## Part 3.4.2 neighborhood best aspiration
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500,None,None,None,True)
print('final solution with neighborhood best aspiration:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## Part 3.5
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500,None,None,None,None,True)
print('final solution with less than the whole neighborhood:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')

## Part 3.6
print('initial solution:')
print(initialSolution)
solution = tabuSearch(initialSolution,5,5,500,True)
print('final solution with frequency list:')
print(solution)
print('cost:')
print(calcCost(solution))
print('\n')


