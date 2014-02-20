import sys
import csv

def getMean(list):
	'This function computes and returns the average of a list passed in as an argument' 
	sum = 0.0
	for element in list:
		sum += element
		
	return sum/len(list)
	
	
	
def getVariance(list):
	'This function computes and returns the variance of alist passed in as an argument'
	sum = 0.0
	
	for element in list:
		sum += element*element
		
	mean = getMean(list)
	return (sum/len(list) + mean*mean)
	

# ------------------------------------------------------	
# ------------------------------------------------------
# this is method one
# ------------------------------------------------------
# ------------------------------------------------------


# read the data all at once	
data_file = open(sys.argv[1], 'rb')
data = data_file.readlines()
data_file.close()
	

# this is the header	
final_list = ['# of elements,mean,variance']


for line in data:
	line1 = line.strip().split(',')
	line1 = [float(x) for x in line1]
	final_list.append(str(len(line1)) + ',' + str(getMean(line1)) + ',' + str(getVariance(line1)))	
	

# make one long string to write - join with a new line character		
str_to_write = '\n'.join(final_list)

# write string to file
with open(sys.argv[2], 'wb') as fout:
	fout.write(str_to_write)


# ------------------------------------------------------
# ------------------------------------------------------
# this is method two
# ------------------------------------------------------
# ------------------------------------------------------



# this is the header	
final_list = ['# of elements,mean,variance']

# read the data using csv.reader	
with open(sys.argv[1], 'rb') as csv_file:
	data_lines = csv.reader(csv_file)
	
	for line in data_lines:
		line1 = [float(x) for x in line]
		final_list.append(str(len(line1)) + ',' + str(getMean(line1)) + ',' + str(getVariance(line1)))

# make one long string to write - join with a new line character		
str_to_write = '\n'.join(final_list)

# write string to file
with open(sys.argv[3], 'wb') as fout:
	fout.write(str_to_write)


# ------------------------------------------------------
# ------------------------------------------------------
# this is method three
# ------------------------------------------------------
# ------------------------------------------------------

# this is the header	
final_list = [['# of elements','mean','variance']]

# read the data from the file and assign it to lists
with open(sys.argv[1], 'rb') as csv_file:
	data_lines = csv.reader(csv_file)
	
	for line in data_lines:
		line1 = [float(x) for x in line]
		final_list.append([str(len(line1)),str(getMean(line1)),str(getVariance(line1))])
		

# write it out		
with open(sys.argv[4], 'wb') as fout:
	csv_write = csv.writer(fout)
	
	for line in final_list:
		csv_write.writerow(line)
		

print 'Done! '* 8
	
