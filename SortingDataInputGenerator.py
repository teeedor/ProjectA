# SortingInputDataGenerator
# Random Number input Generator for Sorting Algorithms

import random

#createSortingData() FUNCTION

#input
#   number of data points you want in the file
#   the range that the data points are chosen from
#   the filename of the output file
def createSortingData(Num_of_data_Points, endValue, filename):
    data = open(filename+'.txt', 'w')
    i = 0
    for i in range(0, Num_of_data_Points):    #loop through the number given in function call
        r = random.randint(1,endValue+1)           #choose a random number
        s = str(r)                              #Cast it as a string
        data.write(s+'\n')                      #Write the data to a file

    data.close()                                #Close the File
