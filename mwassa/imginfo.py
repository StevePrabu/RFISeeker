from astropy.io import fits
from astropy.wcs import WCS


def info(fileName):
    hdu = fits.open(fileName)
    wcs = WCS(hdu[0].header,naxis=2)
    header = hdu[0].header
    imgSize = int(hdu[0].header['NAXIS1'])
    return imgSize, wcs, header

