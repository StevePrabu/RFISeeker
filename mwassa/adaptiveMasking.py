from astropy.io import fits
import numpy as np


def mask(pointsInit,pointsValue,imgSize):
    masked = np.zeros((imgSize,imgSize))
    #psfData = psfHDU[0].data[0,0,:,:]
    #sidelobeSeed = np.std(psfData)*1
    #maskArray = np.asarray(np.where(psfData > 0)).T
    #maskArray[:,0] -= int(imgSize/2.0)
    #maskArray[:,1] -= int(imgSize/2.0)
    outputPoints = []
    #pointSorted = np.asarray([x for _,x in sorted(zip(pointsValue,pointsInit),reverse=True)])
    index = np.argsort(pointsValue)
    pointSorted = pointsInit[np.flip(index)]
    #outputPoints = pointSorted
    counter = 0
    for currentPoint in pointSorted:
    	if counter == 0:
    	    outputPoints.append(np.asarray(currentPoint))
    	    break
     	counter +=1
    return outputPoints




