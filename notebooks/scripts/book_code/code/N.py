import inspect, os
def printer():
	print 'I am in function',
	print inspect.getfile(inspect.currentframe())