import numpy as np
from scipy import special


def cumulative_distribution_function(x,location,scale,a):
        temp = (x- location)/abs(scale)
        return 0.5*(1+special.erf(temp/np.sqrt(2.0))) - 2.0*special.owens_t(temp,abs(a))

def skew_norm_pdf(x,e=0,w=1,a=0):
        t = (x-e)/w
        output= 2.0*w*(1/(np.sqrt(2*np.pi)))*np.exp((-t**2)/2)*0.5*(1+special.erf(a*t/np.sqrt(2)))
        return output/sum(output)


def reqCDF(seedValue):
        return 0.5*(1+special.erf(float(seedValue)/np.sqrt(2)))

def getSeedValue(cdf,seedSigma,x):
    diffInCDF = abs(cdf - reqCDF(seedSigma))
    minDiff = min(diffInCDF)
    position_of_min = int(np.asarray(np.where(diffInCDF == minDiff)))
    seedValue = x[position_of_min] + (x[2]-x[1])/2.0
    return seedValue


def getFloodfillValue(cdf,floodfillSigma,x):
    diffInCDF = abs(cdf - reqCDF(floodfillSigma))
    minDiff = min(diffInCDF)
    position_of_min = int(np.asarray(np.where(diffInCDF == minDiff)))
    floodfillValue = x[position_of_min] + (x[2]-x[1])/2.0
    return floodfillValue


