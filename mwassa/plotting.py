import matplotlib.pyplot as plt

def intialiseMatplotib(debug):
	global plt
	if debug is False:
		import matplotlib
		matplotlib.use('Agg')
		import matplotlib.pyplot as plt
		
	else:
		import matplotlib.pyplot as plt
		
	return;

