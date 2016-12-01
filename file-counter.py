############################################################################################################################################################################################
##File_Counter.py
##
##Author: Ryan Davison
##
##
##Date: August 9, 2012
##
##Purpose: This script is intended to loop through a root directory and its sub directories and count the number of files with a specific extension.
##
############################################################################################################################################################################################
import os

directorypath = raw_input("Enter path of top level folder: ")
directorypath = str(directorypath)
extension = raw_input("Enter the extension for the file type you want to search for: .")
counter = []
print


#Loop through all folders and subfolders in your target directory. Find each file with a specific extension and return a count.
for root, dirs, files in os.walk(directorypath):
      for fi in files:
            if fi.endswith(extension):
                  print fi
                  counter.append(fi)

if counter != 0:
      print "%i" % (len(counter)), extension, "files were found."
      print
else:
      print "No", extension, "file(s) were found."
      print


del counter

#The Repeat class allows you to run the script again on a different directory if you so desire.
class Repeat():
    y = raw_input("Do you want to run the counter again? (y/n): ")
    if y == 'y':

#Edit the path on the following line to point to where your File_Counter.py script is located.

        execfile(os.path.realpath(__file__))
    elif y != y:
          print "done"
