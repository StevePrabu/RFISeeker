from datetime import datetime, timedelta
from astropy.wcs import WCS
import os.path


def plotStarlink(wcs,UTCtime, debug):
	fl = open('starlinkTLE_all_tle.txt')

	line = fl.readline()
	counter = 1
	line1 = 'SATELLITE'
	while line:
		if counter%2 ==1:
			line2=line
		else:
			line3=line
			sat=ephem.readtle(str(line1), str(line2),str(line3))
			sat.compute(mwa)
			x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
			if (0 <= x < 2000) and (0 <= y < 2000):
				plt.plot(x,y, marker='.', color='yellow')
				if debug is True:
					print("Plotting Starlink")
		counter += 1
		line = fl.readline()
	return;


def plotLEO(wcs,UTCtime, debug):
	fl = open('tle.txt')
	line = fl.readline()
	counter = 1
	line1 = 'SATELLITE'
	while line:
		if counter%2 ==1:
			line2=line
		else:
			line3=line
			sat=ephem.readtle(str(line1), str(line2),str(line3))
			sat.compute(mwa)
			x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
			if (0 <= x < 2000) and (0 <= y < 2000):
				plt.plot(x,y, marker='+', color='white')
				if debug is True:
					print("Plotting LEO")
		counter += 1
		line = fl.readline()

	delay = [-12, -8, -5, 5, 8, 12]

	for d in delay:
		time_temp = UTCtime + timedelta(seconds=int(d))
		mwa.date = time_temp
		fl = open('tle.txt')
		line = fl.readline()
		counter = 1
		line1 = 'SATELLITE'
		while line:
			if counter%2 ==1:
				line2=line
			else:
				line3=line
				sat=ephem.readtle(str(line1), str(line2),str(line3))
				sat.compute(mwa)
				x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
				if (0 <= x < 2000) and (0 <= y < 2000):
					plt.plot(x,y, marker='.', color='white', markersize='1')
					if debug is True:
						print("Plotting LEO trail")
			counter += 1
			line = fl.readline()
	return;






def plotHEO(wcs,UTCtime, debug):
	fl = open('HEOtle.txt')
	line = fl.readline()
	counter = 1
	line1 = 'SATELLITE'
	while line:
		if counter%2 ==1:
			line2=line
		else:
			line3=line
			sat=ephem.readtle(str(line1), str(line2),str(line3))
			sat.compute(mwa)
			LOS = sat.range
			x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
			if np.all((0 <= x < 2000) and (0 <= y < 2000)):
				plt.plot(x,y, marker='+', color='black')
				if debug is True:
					print("Plotting HEO")
		counter += 1
		line = fl.readline()
	delayHEO = [-15, -8, 8, 15]
	for dHEO in delayHEO:
		time_temp = UTCtime + timedelta(seconds=int(dHEO))
		mwa.date = time_temp
		fl = open('HEOtle.txt')
		line = fl.readline()
		counter = 1
		line1 = 'SATELLITE'
		while line:
			if counter%2 ==1:
				line2=line
			else:
				line3=line
				sat=ephem.readtle(str(line1), str(line2),str(line3))
				sat.compute(mwa)
				LOS = sat.range
				x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
				if np.all((0 <= x < 2000) and (0 <= y < 2000)):
					plt.plot(x,y, marker='.', color='black', markersize='1')
					if debug is True:
						print("Plotting HEO trail")
			counter += 1
			line = fl.readline()	
	return;


def plotMEO(wcs,UTCtime,debug):
	fl = open('MEOtle.txt')	
	line = fl.readline()
	counter = 1
	line1 = 'SATELLITE'
	while line:
		if counter%2 ==1:
			line2=line
		else:
			line3=line
			sat=ephem.readtle(str(line1), str(line2),str(line3))
			sat.compute(mwa)
			x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
			if (0 <= x < 2000) and (0 <= y < 2000):
				plt.plot(x,y, marker='+', color='green')	
				if debug is True:
					print("Plotting MEO")

		counter += 1
		line = fl.readline()	

	delayMEO = [-10, -5, 5, 10]

	for dMEO in delayMEO:
        	time_temp = UTCtime + timedelta(minutes=int(dMEO))
                mwa.date = time_temp
                fl = open('MEOtle.txt')
                line = fl.readline()
                counter = 1
                line1 = 'SATELLITE'
                while line:
                	if counter%2 ==1:
                        	line2=line
                        else:
                        	line3=line
                                sat=ephem.readtle(str(line1), str(line2),str(line3))
                                sat.compute(mwa)
                                x, y = wcs.all_world2pix([[np.degrees(sat.ra.real), np.degrees(sat.dec.real)]], 1)[0]
                                if (0 <= x < 2000) and (0 <= y < 2000):
                                	plt.plot(x,y, marker='.', color='green', markersize='1')
					if debug is True:
						print("Plotting MEO trail")
			counter += 1
                        line = fl.readline()
	return;




