'''
Name: 
Course:
Assignment:

Description:

'''




import csv
import sys
import os
import os.path
import xml.etree.ElementTree as ET


# standard XML statements
tree = ET.parse(sys.argv[1])

root = tree.getroot()


# //////////////////////////////////////////////////////////////////////
# 
#                 P A R T   O N E
#
# //////////////////////////////////////////////////////////////////////


# question 1
for node in tree.iter(tag='camera'):
   if node.attrib['name'] is 'cam2':
      node.attrib['vendor'] = 'XClassCams'

# question 2
if node.attrib['name'] is 'cam3':
   sub_node = node.find('fovv')
   sub_node.text = '75'

# question 3
for node in tree.iter(tag='heading'):
   if float(node.text) > 23:
      node.text = '22.5'
      
      
# question 4
tree.write(sys.argv[2])


#
tree = []


# //////////////////////////////////////////////////////////////////////
# 
#                 P A R T   T W O
#
# //////////////////////////////////////////////////////////////////////

# read the file again
tree = ET.parse(sys.argv[1])

# get the root element
root = tree.getroot()


# get the root name
root_name = root.tag

# create directory if it does not exist
if not os.path.exists(root_name):
   os.mkdir(root_name)
   
   
# get the names of the files to written out
children = root.getchildren()

# loop though the children and for every child create a file and 
# write the data to the file
for child in children:  
   header = []
   string = []
   header_not_done = True;
   grandchild = child.getchildren()

   # if the child have attributes
   if len(child.attrib.keys()) > 0:
      header = child.attrib.keys()
      for key in child.attrib.keys():
         string.append(child.attrib[key])

   
   # blank lists
   string3 = []
   string4 = []

   # construct the name of the output file
   csv_out_file = root.tag + os.sep + child.tag + '.csv'
   fout = open(csv_out_file, 'wb')
   csv_writer = csv.writer(fout)
   for grand in grandchild: # camera, heading, temperature, rates
      string2 = []

      # work with the attributes to constuct the header
      if len(grand.attrib.items()) > 0: 
         if header_not_done:
            header += grand.attrib.keys()


         # get the keys
         for key in grand.attrib.keys():
            string2.append(grand.attrib[key])


      # see if we have great grand children
      string3 = string + string2
      if len(grand.getchildren()) > 0:
         for gr in grand.getchildren():
            if gr.tag not in header:
               header.append(gr.tag)
               header += gr.attrib.keys()

            # if they have text elements
            if len(gr.text) > 0:
              string3.append(gr.text.strip())

            if len(gr.attrib.items()) > 0:
               for key in gr.attrib.keys():
                 string3.append(gr.attrib[key])          
            
      else:
         if len(grand.text):
            string3.append(grand.text.strip())

         if grand.tag not in header:
            header.append(grand.tag)
      
      string4.append(string3)

      # write the header once
      if header_not_done:
         header_not_done = False
         csv_writer.writerow(header)

      # write the data 
      csv_writer.writerow(string3)

   # close the stream
   fout.close()      





print 'Done'+'!'*10