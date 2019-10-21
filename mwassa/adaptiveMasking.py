from astropy.io import fits
import numpy as np


def mask(psfHDU,pointsInit,pointsValue,imgSize):
    masked = np.zeros((imgSize,imgSize))
    psfData = psfHDU[0].data[0,0,:,:]
    sidelobeSeed = np.std(psfData)*1
    maskArray = np.asarray(np.where(psfData > 0)).T
    maskArray[:,0] -= int(imgSize/2.0)
    maskArray[:,1] -= int(imgSize/2.0)
    outputPoints = []
    #pointSorted = np.asarray([x for _,x in sorted(zip(pointsValue,pointsInit),reverse=True)])
    index = np.argsort(pointsValue)
    pointSorted = pointsInit[np.flip(index)]
    counter = 0
    for currentPoint in pointSorted:
        if masked[currentPoint[0],currentPoint[1]] ==1:
            continue
        else:
	    if counter  == 0:
            	outputPoints.append(np.asarray(currentPoint))
		counter += 1
            mask = maskArray
            mask[:,1] += currentPoint[0]
            mask[:,0] += currentPoint[1]
            for m in mask:
                if 0 <= m[0] < imgSize and 0 <= m[1] < imgSize:
                    masked[m[0],m[1]]=1
            mask[:,1] -= currentPoint[0]
            mask[:,0] -= currentPoint[1]
    return outputPoints




