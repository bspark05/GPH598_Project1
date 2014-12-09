#Class Document
==================
##[File IO](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)
Method |Description                                               
---|---
pysal.core.FileIO.FileIO.**[open](http://www.pysal.org/library/open.html#FileIO.open)**(connectionString, mode) | Parses the connectionString and mode to determine the correct file handler. If a custom handler is not found a python file object will be returned.
FileIO.open(connectionString, mode='r') | Parses the String and return a list containing values.

##Descriptive point patterns [ I ](https://github.com/GPH498598F14/GPH498598F14/blob/master/project/05_point_pattern_basics.pdf)&[ II ](https://github.com/GPH498598F14/GPH498598F14/blob/master/project/09_point_distance.pdf)

Method |Description                                               
---|---
Statistics.meanCenter(points) | Calculate mean center of points and return the coordinates of the point
Statistics.medianCenter(points) | Calculate median center of points and return the coordinates of the point
Statistics.weightedMeanCenter(weight, points) | Calculate weighted mean center of points with weight matrix and return the coordinates of the point
Statistics.standardDistance(points, weightedMeanCenter) | Cacluate standard distance of points and return the distance
Statistics.centerOfMinimumDistance(points, diff) | Find center of minimum distance of points using quadtree until the difference of distance become smaller than 'diff' and return the coordinates of the point

##Polygon
Method |Description                                               
---|---
scipy.spatial.**[ConvexHull](http://docs.scipy.org/doc/scipy-dev/reference/generated/scipy.spatial.ConvexHull.html)**(points[, incremental, qhull_options]) | Creates a Convex hulls in N dimensions.
Polygon.**makeConvexHull**(points[, incremental, qhull_options]) | Returns coordinates of a Convex hull in numpy 2-D array
Polygon.**makeMBR**(points) | Returns coordinates of a MBR in numpy 2-D array
