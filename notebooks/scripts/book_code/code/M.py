import inspect
def printer():
	print 'I am in function',
	print inspect.getfile(inspect.currentframe())
