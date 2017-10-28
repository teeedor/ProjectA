import SortingDataInputGenerator

# Implement bubble sort

#Set flags to show the time it takes to run the sorting algorithm
#showTime = false

swapFlag = True
Num_of_data_Points = 100
endValue = 10000
filename = 'ExampleData'

#--------------------------------------------------------------------------
#Generate new input data
SortingDataInputGenerator.createSortingData(Num_of_data_Points,endValue,filename)


#--------------------------------------------------------------------------
#read in data from input file


with open (filename+'.txt', 'r') as data:           #This is working
    lines = data.read().splitlines()

#len(lines) to find length of lines
#num_of_elements = len(lines)                        #This is working

#print(num_of_elements)
#print(lines[Num_of_data_Points])


#if showTime:
    #Store the time to check it against later
#--------------------------------------------------------------------------
#start = 0
#end = num_of_elements-1


#for i in range(start, end) and swapFlag == True:     #iterate through the entire list and checck swap flag
    #temp1 = lines[i]
    #temp2 = lines[i+1]


    #check to to see if the two elements we are looking at are in the correct order
    #if
    #If they are leave them be
    #else swap them
        #Activate swap flag to show that a swap has occurred

    #Do this until we make a pass with no changes

#--------------------------------------------------------------------------
#if showTime:
    #get current time and calculate the difference
