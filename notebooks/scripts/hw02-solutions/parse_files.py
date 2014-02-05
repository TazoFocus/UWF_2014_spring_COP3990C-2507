'''
Name: JE Touma
Course: COP 3990C
Assignment: HW 02

Run: python parse_files input_file_1.txt input_file_2.csv

This script parses a text and a CSV file and writes them out as a CSV and a text files, respectively.
'''

# import necessary libraries
import sys   # for handling command line arguments
import csv   # for handling csv files

# get the input list
cli_list = sys.argv

# extract the names of the input files
txt_input = cli_list[1]
csv_input = cli_list[2]


 
# ---------------------------------------------------
#
# processes the txt file and write out as a csv file
#
# ---------------------------------------------------


# read the file into a list
with open(txt_input, 'rb') as fin:
	lines = fin.readlines()
	
# initialize a dictionary to hold the values
new_data = {}

# loop through the lines and construct the dictionary
for line in lines:
	temp = line.strip().split() # strip and split each line
	temp1 = [float(x) for x in temp[:-1]] # change the data from string to float
	temp1.sort() # sort the data
	temp1 = [str(x) for x in temp1] # change back to string
	new_data[temp[-1].strip()] = [str(x) for x in temp1] # make the list as a string
	
	
# print the dictionary
print '\n'*4
print 'The dictionary from ', txt_input, ' is:'
print new_data
print '\n'*4
# csv input file -> txt output file
txt_output = csv_input.replace('input', 'output')
txt_output = txt_output.replace('csv', 'txt')


# create 1 huge string to print to a file
long_string  = ''

for key in new_data:
	long_string += key + ',' + ','.join(new_data[key]) + '\n'

# remove the new line character from the string 
long_string = long_string.strip()


# save it to a file
fout = open(txt_output, 'wb')
fout.write(long_string)
fout.close()	


# ---------------------------------------------------
#
# processes the csv file and write out as a txt file
#
# ---------------------------------------------------


# open the file and read the first line to get the header info
fin = open(csv_input, 'rb')
header = fin.readline()

# get back to the beginning of the file
fin.seek(0,0)

# use DictReader to read the data into a dictionary format
csv_data = csv.DictReader(fin)


# strip the header into individual column headers	
header = header.strip().split(',')


# initialize a dictionary to read data into
new_data = {}

# initialize each element of the dictionary as an empty list
for x in header:
	new_data[x] = []

	
# parse the data from the file and store it into a dictionary
for line in csv_data:
	for x in header:
		new_data[x].append(line[x])


# print the dictionary to the screen
print 'The dictionary from ', csv_input, ' is:'
print new_data



# txt input file -> csv output file
csv_output = txt_input.replace('input', 'output')
csv_output = csv_output.replace('txt', 'csv')

# initialize a long string to hold all the values
long_string = ''

# loop though dictionary and construct the string
for key in new_data:
	long_string += key + ' ' + ' '.join(new_data[key]) + '\n'

# strip the last new line character
long_string = long_string[:-1]


# write data out to file
fout = open(csv_output, 'wb')
fout.write(long_string)
fout.close()