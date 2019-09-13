import ephem

def intialiseMWA():
	global mwa
 	mwa = ephem.Observer()
	mwa.lon = '116:40:14.93485'
	mwa.lat = '-26:42:11.94986'
	mwa.elevation = 377.827 #from sea level
	return;

