import math
import random

def easom(point):
    return -math.cos(point[0])*math.cos(point[1])*math.exp(-((point[0]-math.pi)**2)-((point[1]-math.pi)**2))

def isPass(change, temperature):
    if(temperature <=0):
        return False
    if(change < 0):
        return True
    # This works for when change is negative too because it will always return true in that case
    return random.random() < math.exp(-change/temperature)

def linear(temperature, alpha):
    return temperature - alpha

def exponential(temperature, alpha):
    return temperature*alpha

def slow(temperature, alpha):
    return temperature/(1+alpha*temperature)

# neighborhood[0] is the distance between each point, neighborhood[1] is the amount of times it is expanded
def neighborhoodFunction(current,neighborhood):
    # generate points around the current point
    possibleChanges = [1,-1]
    expandedChanges = []
    for k in range(neighborhood[1]):
        for i in possibleChanges:
            if i*k*neighborhood[0] not in expandedChanges:
                expandedChanges.append(i*k*neighborhood[0])
    expandedChanges.append(0)
    neighborhoodPoints = []
    for i in expandedChanges:
        for j in expandedChanges:
            # Don't add the original point
            if(not(j== 0 and i == 0)):
                neighborhoodPoints.append((current[0]+i,current[1]+j))
    return neighborhoodPoints

def selectFromNeighborhoodFunction(current, neighborhood, iteration, maxIter, temperature, method, alpha):
    neighborhoodPoints = neighborhoodFunction(current,neighborhood)
    if(iteration >= maxIter):
        temperature = method(temperature, alpha)
        iteration = 0
    iteration += 1

    next = None
    passed = []
    for i in neighborhoodPoints:
        if(isPass(easom(i)-easom(current),temperature)):
            passed.append(i)

    # Choose random point that has passed
    if(len(passed)):
        index = pickRandom([(0,len(passed)-1)],1)
        next = passed[round(index[0][0])]
    return {
        'solution': next,
        'iter': iteration,
        'temperature': temperature
    }

# Generates num random combinations given the dimensions
def pickRandom(dimensions, num):
    result = []
    for i in range(num):
        point = []
        for j in dimensions:
            span = abs(j[1] - j[0])
            bottom = min(j[0], j[1])
            point.append(bottom + random.random()*span)
        result.append(point)
    return result

def simulatedAnnealing(temperature,solution,neighborhood, maxIter, method, alpha, maxIdle):
    idleCount = 0
    iteration = 0
    while(idleCount < maxIdle):
        result = selectFromNeighborhoodFunction(solution,neighborhood,iteration,maxIter,temperature,method,alpha)
        if(result['solution'] != None):
            solution = result['solution']
            idleCount = 0
        else:
            idleCount += 1
        iteration = result['iter']
        temperature = result['temperature']
    return solution

def getTemperatureRange(current, neighborhood):
    neighborhoodPoints = neighborhoodFunction(current,neighborhood)
    # Define highest as a temperature that can accept the highest value change 90% of the time
    highest = -math.inf
    lowest = math.inf
    # get the highest and lowest bad solutions
    for point in neighborhoodPoints:
        if(easom(point)-easom(current) > highest):
            highest = easom(point)-easom(current)
        if(easom(point)-easom(current) < lowest and easom(point)-easom(current) > 0):
            lowest = easom(point)-easom(current)
    if(highest == -math.inf):
        return None
    return [-lowest/math.log(0.9,math.e),-highest/math.log(0.9,math.e)]

# Must get a temperature that accepts 60% of worse solutions
def getIdealTemperature(tempRange, neighborhoodPoints, current):
    step = (tempRange[1]-tempRange[0])/1000
    temperatureArray = []
    acceptanceRate = []
    for i in range(1000):
        count = 0
        countWorse = 0
        temperature = tempRange[0]+i*step
        temperatureArray.append(temperature)
        for point in neighborhoodPoints:
            if(easom(point)-easom(current) > 0):
                countWorse += 1
                if(isPass(easom(point)-easom(current),temperature)):
                    count += 1
        acceptanceRate.append(count/countWorse)

    # Get the one closest to 60%
    lowestDist = math.inf
    lowestTemp = None
    for i in range(len(temperatureArray)):
        if(abs(acceptanceRate[i]-0.6) < lowestDist):
            lowestDist = abs(acceptanceRate[i]-0.6)
            lowestTemp = temperatureArray[i]
    return lowestTemp

# get 10 random points in the range
random.seed(457)
easomRange = [(-100,100),(-100,100)]
numPoints =10
print('10 random points:')
print(pickRandom(easomRange,numPoints))

# Choosing [10.403995617042924, -7.971713338794274], generate the temperature range
selectedPoint = [10.403995617042924, -7.971713338794274] 
neighborhood = [0.1,5]
print('temperature range:')
print(getTemperatureRange(selectedPoint,neighborhood))

# get 10 random temperatures in the temperature range 
random.seed(457)
temperatureRange = (8.122053221873624e-79, 1.1135477161730774e-70)
numTemperatures = 10
print('10 random temperatures:')
print(pickRandom([temperatureRange],numTemperatures))

# get ideal temperature
print('the Ideal temperature is:')
print(getIdealTemperature(temperatureRange,neighborhoodFunction(selectedPoint,neighborhood),selectedPoint))

# Solve for all 9 cases
selectedTemperature = 4.878705123045279e-72
maxIdle = 10
maxIter = [100,200,1]
methods = [linear,exponential,slow]
methodString = ['linear', 'exponential','slow']
alphas = [selectedTemperature/2, selectedTemperature/50,selectedTemperature/1000]
for methodIndex in range(len(methods)):
    random.seed(457)
    for alpha in alphas:
        print('The solution found with alpha = ' + str(alpha) + ' and the ' + methodString[methodIndex] + ' method is:')
        print(simulatedAnnealing(selectedTemperature,selectedPoint,neighborhood,maxIter[methodIndex],methods[methodIndex],alpha,maxIdle))