import numpy as np
import math
import Polygon as poly
import matplotlib.pyplot as plt

def meanCenter(points):
    pointsArray = np.array(points)
    mnCenter = np.mean(pointsArray, axis=0)
    #print(mnCenter)
    return mnCenter

def medianCenter(points):
    pointsArray = np.array(points)
    medCenter = np.median(pointsArray, axis=0)
    #print(medCenter)
    return medCenter

def weightedMeanCenter(weight, points):
    pointsArray = np.array(points)
    weightArray = np.array(weight)
    
    weightArray1 = weightArray*pointsArray
    wmc = sum(weightArray1)/sum(weightArray)
    return wmc

def standardDistance(points, WMC):
    pointsArray = np.array(points)
    WMCArray = np.array(WMC)
    sd1 = sum((pointsArray-WMCArray)*(pointsArray-WMCArray))/len(pointsArray)
    sd2 = math.sqrt(sd1[0]+sd1[1])
    return sd2


def centerOfMinimumDistance(points):
    pointsArray = np.array(points)
    extent = poly.makeMBR(points)
    initCenter = [(extent[1][0]+extent[0][0])/2, (extent[2][1]+extent[1][1])/2]
    initHeight = (extent[2][1]-extent[1][1])/4
    initWidth = (extent[1][0]-extent[0][0])/4
    
    center = initCenter
    width = initWidth
    height = initHeight
    
    times = 0
    difference = -1
    
    while difference > 1 or difference == -1:
        quaterPoints = makeQuaterPoints(center, width, height)
        newCenter = findRectangle(quaterPoints, pointsArray)
        
        difference = math.sqrt((center[0]-newCenter[0])**2 + (center[1]-newCenter[1])**2)
        
        center = newCenter
        
        width = width/2
        height = height/2
        times +=1  
    
    plt.plot(pointsArray[:,0], pointsArray[:,1], 'kx')
    plt.plot(quaterPoints[:,0],quaterPoints[:,1],'ro')
    plt.plot(extent[:,0],extent[:,1],'bo')
    plt.plot(center[0], center[1],'rx')
    plt.show()
    
    
    
        
def makeQuaterPoints(centerPoint, width, height):
    pointsList =[]
    pointsList.append([centerPoint[0]-width, centerPoint[1]-height])
    pointsList.append([centerPoint[0]+width, centerPoint[1]-height])
    pointsList.append([centerPoint[0]+width, centerPoint[1]+height])
    pointsList.append([centerPoint[0]-width, centerPoint[1]+height])
    pointsArray = np.array(pointsList)
    #print(pointsList)
    
    return pointsArray

def findRectangle(quaterPoints, pointsArray):
    minDistance = -1
    minDistanceCoor = []

    for stdPoint in quaterPoints:
        tempDist = 0
        for point in pointsArray:
            tempDist += (point[0]-stdPoint[0])**2+(point[1]-stdPoint[1])**2
        
        if minDistance>tempDist or minDistance == -1:
            minDistance = tempDist
            print(minDistance)
            minDistanceCoor = stdPoint
            
    return minDistanceCoor
            
