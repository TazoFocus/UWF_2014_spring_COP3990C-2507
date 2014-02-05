'''
Course: COP3990C
Name: JET
Date: 1/12/14
Assignment: Homework 1

This program computes the mean and variance of a list of randomly generated integers
'''

# import the random package
import random


# initialize some variables
mean          =  0.0
num_of_ints   =  100
lower_number  =  0
upper_number  =  1001
variance      =  0.0


# generate a list of random numbers
random_list = random.sample(xrange(lower_number, upper_number), num_of_ints)


# loop though the list and compute the mean
for random_int in random_list:
   mean = mean + random_int
   
mean = mean / num_of_ints


# loop through the list and compute the variance
for random_int in random_list:
   variance = variance + random_int * random_int
   
variance = variance / num_of_ints - mean * mean


# print the results
print 'The mean for the list of ', num_of_ints, ' randomly generated integers is: ', mean
print 'The variance for the list of ', num_of_ints, ' randomly generated integers is: ', variance
  
