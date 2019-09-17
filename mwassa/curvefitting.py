import numpy as np
from scipy import special
from scipy.optimize import root_scalar


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
    position_of_min = np.asarray(np.where(diffInCDF == minDiff))
    index = position_of_min[0][0]
    seedValue = x[index] + (x[2]-x[1])/2.0
    return seedValue

def getFloodfillValue(cdf,seedSigma,x):
    diffInCDF = abs(cdf - reqCDF(seedSigma))
    minDiff = min(diffInCDF)
    position_of_min = int(np.asarray(np.where(diffInCDF == minDiff)))
    seedValue = x[position_of_min] + (x[2]-x[1])/2.0
    return seedValue


#def getSeedValue(seedSigma,location,scale,a):
#    target = 0.99999999
#    sol = root_scalar(lambda x, *args: cumulative_distribution_function(x, *args) - target,bracket=(-6*scale + location, 6*scale + location),args=(location, scale, a))
#    return float(sol.root)

#def getFloodfillValue(floodfillSigma,location,scale,a):
#    target = reqCDF(floodfillSigma)
#    sol = root_scalar(lambda x, *args: cumulative_distribution_function(x, *args) - target,bracket=(-6*scale + location, 6*scale + location),args=(location, scale, a))
#    return float(sol.root)

