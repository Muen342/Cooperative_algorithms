import random
import math

population = 1000
generations = 500
mutation = 0.5
crossover = 0.5
maxDepth = 4

operators = ["IF", "NOT", "AND", "OR"]
terminals = ["a0", "a1", "d0", "d1", "d2", "d3"]
totalNodes = operators + terminals

def generateRandomIndex(n):
    return math.floor(random.random()*n)

def fillArgs(depth, node):
    if(node['data'] == 'AND'):
        depth +=1
        node['left'] = createTree(depth)
        node['right'] = createTree(depth)
    elif(node['data'] == 'OR'):
        depth +=1
        node['left'] = createTree(depth)
        node['right'] = createTree(depth)
    elif(node['data'] == 'NOT'):
        depth +=1
        node['left'] = createTree(depth)
    else:
        depth += 1
        node['left'] = createTree(depth)
        node['middle'] = createTree(depth)
        node['right'] = createTree(depth)
    return node

def createTree(depth):
    if(depth >= maxDepth-1):
        # terminate with a terminal
        nodeArg = terminals[math.floor(random.random()*len(terminals))]
        node = {}
        node['data'] = nodeArg
        return node
    nodeArg = totalNodes[math.floor(random.random()*len(totalNodes))]
    node = {}
    node['data'] = nodeArg
    # break if it is a terminal
    if(node['data'] in terminals):
        return node
    else:
        return fillArgs(depth,node)

def generateInitialSolutions(number):
    solutions = []
    for i in range(number):
        depth = 0
        nodeArg = totalNodes[math.floor(random.random()*len(totalNodes))]
        node = {}
        node['data'] = nodeArg
        # break if it is a terminal
        if(nodeArg in terminals):
            solution = node
        else:
            solution = fillArgs(depth, node)
        solutions.append(solution)
    return solutions

# check if it includes non solutions in the output
def isOthersIn(solutionPair, digitalNum):
    for i in range(0,4):
        if(solutionPair[2+i] == 1 and i != digitalNum):
            return True
    return False


def convertToTF(sol):
    ret = []
    for i in sol:
        if(i):
            ret.append(True)
        else:
            ret.append(False)
    return ret

def getRealSolutionPairs():
    solutionPairs = []
    a0 = [0,1]
    a1 = [0,1]
    d0 = [0,1]
    d1 = [0,1]
    d2 = [0,1]
    d3 = [0,1]
    for i in a0:
        for j in a1:
            for k in d0:
                for l in d1:
                    for m in d2:
                        for n in d3:
                            solutionPairs.append([i,j,k,l,m,n])
    for pairInd in range(len(solutionPairs)):
        digitalNum = int(str(solutionPairs[pairInd][0])+str(solutionPairs[pairInd][1]),2)
        # find if it is good or not to count as fitness
        if(solutionPairs[pairInd][2+digitalNum] == 1 and isOthersIn(solutionPairs[pairInd],digitalNum) == False):
            solutionPairs[pairInd] = convertToTF(solutionPairs[pairInd])
            solutionPairs[pairInd].append(True)
        else:
            solutionPairs[pairInd] = convertToTF(solutionPairs[pairInd])
            solutionPairs[pairInd].append(False)
    return solutionPairs

fullRealPairs = getRealSolutionPairs()

def getFitness(solution, pairs):
    count = 0
    for pair in pairs:
        # if return is not conforming to the evaluation, it is default unfit
        try:
            if(pair[6]):
                result = evaluateNode(solution,pair[0],pair[1])
                index = int(result['data'][1])+2
                if(result['value'] == pair[index]):
                    count += 1
            else:
                result = evaluateNode(solution,pair[0],pair[1])
                index = int(result['data'][1])+2
                if(result['value'] != pair[index]):
                    count += 1
                else:
                    isGood = False
                    for i in range(4):
                            if(pair[i+2] and i != index):
                                isGood = True
                                break
                    if(isGood):
                        count += 1
        except:
            pass
    return count

def evaluateNode(node, a0, a1):
    if(node['data'] == 'AND'):
        node1 = {}
        node1['data'] = 'result'
        node1['value'] = evaluateNode(node['left'], a0, a1)['value'] and evaluateNode(node['right'], a0, a1)['value']
        return node1
    elif(node['data'] == 'OR'):
        node1 = {}
        node1['data'] = 'result'
        node1['value'] = evaluateNode(node['left'], a0, a1)['value'] or evaluateNode(node['right'], a0, a1)['value']
        return node1
    elif(node['data'] == 'IF'):
        if(evaluateNode(node['left'], a0, a1)['value'] == True):
            return evaluateNode(node['middle'], a0, a1)
        else:
            return evaluateNode(node['right'], a0, a1)
    elif(node['data'] == 'NOT'):
        node1 = {}
        node1['data'] = node['left']['data']
        node1['value'] = not evaluateNode(node['left'],a0,a1)['value']
        return node1
        
    elif(node['data'] == 'a0'):
        node['value'] = a0
    elif(node['data'] == 'a1'):
        node['value'] = a1
    # for outputs default is 1
    else:
        node['value'] = 1
    return node
    # go to the left to evaluate

def getHeight(node):
    left = 0
    middle = 0
    right = 0
    if('left' in node.keys()):
        left = 1 + getHeight(node['left'])
    if('middle' in node.keys()):
        middle =  1 + getHeight(node['middle'])
    if('right' in node.keys()):
        right = 1 + getHeight(node['right'])
    if('left' not in node.keys() and 'middle' not in node.keys() and 'right' not in node.keys()):
        return 1
    return max(left, middle, right)

def getSize(node):
    left = 0
    middle = 0
    right = 0
    if('left' in node.keys()):
        left = getSize(node['left'])
    if('middle' in node.keys()):
        middle =  getSize(node['middle'])
    if('right' in node.keys()):
        right = getSize(node['right'])
    if('left' not in node.keys() and 'middle' not in node.keys() and 'right' not in node.keys()):
        return 1
    return left + middle + right + 1

# returns the nodes and the instructions to get to that node
def postOrderTraversal(node, instructions):
    left = []
    middle = []
    right = []
    instrLeft = []
    instrRight = []
    instrMid = []
    if('left' in node.keys()):
        result = postOrderTraversal(node['left'],instructions + ['left'])
        instrLeft = result[1]
        left = result[0]
    if('middle' in node.keys()):
        result = postOrderTraversal(node['middle'],instructions + ['middle'])
        instrMid = result[1]
        middle = result[0]
    if('right' in node.keys()):
        result = postOrderTraversal(node['right'],instructions + ['right'])
        instrRight = result[1]
        right = result[0]
    return [left + middle + right + [node], instrLeft + instrMid + instrRight + [instructions]]

def getRandomNode(node):
    size = getSize(node)
    index = math.floor(random.random()*size)
    allNodes = postOrderTraversal(node, [])
    return [allNodes, index]

def selectParents(population, popSize, evaluationMetric):
    totalElements = popSize - 2
    fitnesses = []
    for element in population:
        fitnesses.append(getFitness(element,evaluationMetric))
    # choose top 2 for elitism
    max1 = fitnesses.index(max(fitnesses))
    fitnesses.remove(max(fitnesses))
    parent1 = population[max1]
    population.remove(population[max1])


    max2 = fitnesses.index(max(fitnesses))
    fitnesses.remove(max(fitnesses))
    parent2 = population[max2]
    population.remove(population[max2])

    parents = [parent1, parent2]

    total = sum(fitnesses)
    prob = []
    for fit in fitnesses:
        prob.append(fit/total)
    displacement = random.random()/totalElements
    step = 1/totalElements
    current = 0
    for i in range(len(prob)):
        prob[i] = prob[i] + current
        current = prob[i]
    
    for i in range(1,totalElements+1):
        point = (i*step + displacement) % 1
        for j in range(len(prob)):
            if(j != len(prob)-1):
                if(prob[j+1] >= point):
                    parents.append(population[j])
                    break
            else:
                if(prob[0] >= point):
                    parents.append(population[len(population)-1])
                    break
    return parents

# to set the branch of the tree given the instructions to reach it
def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def applyMutation(population, mutationProbability):
    newPop = []
    for element in population:
        temp = element
        if(random.random() <= mutationProbability):
            randomNode = getRandomNode(element)
            instructions = randomNode[0][1]
            index = randomNode[1]
            if(len(instructions[index]) == 0):
                temp = createTree(0)
            else:
                # the depth is the length of the instructions and pass in to make a tree less than this
                nested_set(temp,instructions[index],createTree(len(instructions[index])))
        newPop.append(temp)
    return newPop

def applyCrossover(population, crossoverProbability):
    newPop = []
    # population = random.shuffle(population)
    if(len(population) % 2 == 1):
        newPop.append(population[0])
        population = population[1:]

    for i in range(int(len(population)/2)):
        parent1 = population[2*i]
        parent2 = population[2*i+1]
        if(random.random() <= crossoverProbability):
            randomNode1 = getRandomNode(parent1)
            instructions1 = randomNode1[0][1]
            nodes1 = randomNode1[0][0]
            index1 = randomNode1[1]
            randomNode2 = getRandomNode(parent2)
            instructions2 = randomNode2[0][1]
            nodes2 = randomNode2[0][0]
            index2 = randomNode2[1]
            child1 = parent1
            child2 = parent2

            if(len(instructions1[index1]) == 0 or len(instructions2[index2]) == 0):
                if(len(instructions1[index1]) == 0 and len(instructions2[index2]) == 0):
                    child1 = nodes2[index2]
                    child2 = nodes1[index1]
                elif(len(instructions2[index2]) == 0):
                    child1 = nodes2[index2]
                    nested_set(child2,instructions1[index1],nodes1[index1]) 
                elif(len(instructions1[index1]) == 0):
                    child2 = nodes1[index1]
                    nested_set(child1,instructions2[index2],nodes2[index2]) 
                    
            else:
                nested_set(child2,instructions1[index1],nodes1[index1])   
                nested_set(child1,instructions2[index2],nodes2[index2]) 

            while(getHeight(child1) > maxDepth or getHeight(child2) > maxDepth):
                randomNode1 = getRandomNode(parent1)
                instructions1 = randomNode1[0][1]
                nodes1 = randomNode1[0][0]
                index1 = randomNode1[1]
                randomNode2 = getRandomNode(parent2)
                instructions2 = randomNode2[0][1]
                nodes2 = randomNode2[0][0]
                index2 = randomNode2[1]
                child1 = parent1
                child2 = parent2
                if(len(instructions1[index1]) == 0 or len(instructions2[index2]) == 0):
                    if(len(instructions1[index1]) == 0 and len(instructions2[index2]) == 0):
                        child1 = nodes2[index2]
                        child2 = nodes1[index1]
                    elif(len(instructions2[index2]) == 0):
                        child2 = nodes1[index1]
                        nested_set(child1,instructions2[index2],nodes2[index2]) 
                    elif(len(instructions1[index1]) == 0):
                        child1 = nodes2[index2]
                        nested_set(child2,instructions1[index1],nodes1[index1]) 
                else:
                    nested_set(child2,instructions1[index1],nodes1[index1])   
                    nested_set(child1,instructions2[index2],nodes2[index2]) 
            newPop.append(child1)
            newPop.append(child2)
        else:
            newPop.append(parent1)
            newPop.append(parent2)  
    return newPop 

def selectSurvivors(population, best2):
    return best2 + population

def GA(popSize,numGenerations,mutationProbability,crossoverProbability,evaluationMetric):
    population = generateInitialSolutions(popSize)
    bestSolutionFitness = []
    for i in range(numGenerations):
        parents = selectParents(population,popSize, evaluationMetric)
        # best 2 selected as parents and inserted to final population as well
        best2 = parents[:2]
        bestSolutionFitness.append(getFitness(parents[1],evaluationMetric))
        # population = applyCrossover(population,crossoverProbability)
        population = applyMutation(population, mutationProbability)

        # insert 2 best for elitism again and re-evaluate if they are best, if
        # they are include them again automatically here
        population = selectSurvivors(population, best2)
    
    maxFitness = 0
    maxIndex = 0
    for i in range(len(population)):
        fitness = getFitness(parents[1],evaluationMetric)
        if(fitness > maxFitness):
            maxFitness = fitness
            maxIndex = i
    bestSolution = population[maxIndex]
    return [bestSolution, bestSolutionFitness]

random.seed(457)
result = GA(population,generations,mutation,0,fullRealPairs)

# found with the above parameters
GPSol = {'data': 'IF', 'left': {'data': 'a1', 'value': True}, 'middle': {'data': 'IF', 'left': {'data': 'NOT', 'left': {'data': 'a0', 'value': True}}, 'middle': {'data': 'd1', 'value': 1}, 'right': {'data': 'd3', 'value': 1}}, 'right': {'data': 'd2', 'value': 1}}
print('solution')
print(result[0])
print('\n')

print('Fitnesses')
print(result[1])
