import numpy as np
import math

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
    minDistance = -1
    minDistanceCoor = []
    for point1 in pointsArray:
        dist2 = 0
        #print(point1)
        for point2 in pointsArray:
            #print(index1)
            dist2 += ((point1[0]-point2[0])*(point1[0]-point2[0]))+((point1[1]-point2[1])*(point1[1]-point2[1]))
        if minDistance>dist2 or minDistance==-1:
            minDistance = dist2
            minDistanceCoor = point1
            
                
    return minDistanceCoor
