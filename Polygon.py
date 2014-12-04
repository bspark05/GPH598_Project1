from scipy.spatial.qhull import ConvexHull
import numpy as np
 

def __init__(self, params):
    '''
    Constructor
    '''
        
def makeConvexHull(points, incremental=False, qhull_options=None):
    hull = ConvexHull(points, incremental=False, qhull_options=None)
    convexHullList=[]
    for j in hull.vertices:
        convexHullList.append([points[j][0], points[j][1]])
    convexHullArray = np.array(convexHullList)
    return convexHullArray
    
def makeMBR(points):
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)
    mbrArray = np.array([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
    return mbrArray
