# testing input with while loop

'''
while True:
    reply = raw_input('Enter text:')
	#reply = input('Enter text:') # Python 3.x
	if reply == 'stop': break
	print reply.upper()
'''	
'''
import sys
while True:
	if sys.version[0] == '2':
		reply = raw_input('Enter text:')
	elif sys.version[0] == '3':
		reply = input('Enter text:') 
	else:
		print 'can''t compute'
		break
		
	if reply == 'stop': break
	print reply.upper()
'''	
'''	
while True:
    reply = raw_input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')
'''
'''
while True:
    reply = raw_input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')
'''
'''
while True:
    reply = raw_input('Enter text:')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')
'''


while True:
    reply = raw_input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print('Bye')