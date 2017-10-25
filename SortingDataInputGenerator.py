# SortingInputDataGenerator
# Random Number input Generator for Sorting Algorithms

import random

Num_of_Input = 100                      #Number of data points to sort

data = open('data_File', 'w')           #open an output file stream

i = 1
for i in range(1,Num_of_Input+1):       #Iterate from 1 to the limit set above
    r = random.randint(1,3001)          #Choose a random int
    s =str(r)                           #Typcast to String
    data.write(s+'\n')                  #Write the string with newline

data.close()                            #Make sure to close the file when done with it
