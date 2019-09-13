
def intialiseMatplotib(debug):
	
	if debug is False:
		import matplotlib
		matplotlib.use('Agg')
		import matplotlib.pyplot as plt
		
	else:
		import matplotlib.pyplot as plt
		
	return plt;

