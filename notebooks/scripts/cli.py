# this scripts demonstrates the command line input
# this works under all os'es


# this allows us to interact with the system
import sys


# the argument list that is passed to the code is stored
# in a list called sys.argv
# this list is just like any list in python so you should treat it as such
cli_list = sys.argv

# how many elements is in the list?
print 'The length of my cli list is: ', len(cli_list)

# what is the list of arguments?
print 'Here is my list: ', cli_list


# what is the first element?
print 'this is the name of my python file: ', cli_list[0]

# how about the rest of the elements
for cli_element in cli_list[1:]:
   print cli_element


