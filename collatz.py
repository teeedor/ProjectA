#Collatz

#3n+1
import time
#Take in an input integer or choose to pick a random
#-1 = a choose random integer

#Be able to choose how in depth you want to show the documentation
    #First level: Just show the execution time and number of iterations
    #Second Level: Show the numbers of each iteration
    #Third Level: Show the Operation taken
#---------------------------------------------------------------------

#Example read in input
#raw_input('Enter your input value')

Test1 = False
Test2 = True
Test3 = True
waitTime = .05


#try:
#    mode = int(raw_input('Choose a number to operate on (-1 for random number):'))
#except ValueError:
#    print('choose a correct number')
#
#print(mode)

def CollatzFunc(input):
    temp1=input                 #this is what the operation will take place on
    num_operations = 0

    while temp1 != 1.0:
        if temp1 % 2 == 0:           #If the value is even
            temp1 = temp1/2
            num_operations += 1
            print(temp1)
            if(Test1):
                #Print the
                print('Divide by 2\n')
                print('Current Number of Operations: ',num_operations)
            #if(Test2):
                #Some Comment
            #if(Test3):
                #Some Comment
            time.sleep(waitTime)
        else:
            #multiply by 3 and add 1
            temp1 = ((temp1 * 3) + 1)
            num_operations += 1
            print(temp1)
            if(Test1):
                #Some Comment
                print('Multiply by 3, add 1\n')
                print('Current Number of Operations: ',num_operations)
            #if(Test2):
                #Some Comment
            #if(Test3):
                #Some Comment
            time.sleep(waitTime)
    #Outside of the while loop

    print('Total Number of Operations: ',num_operations)
    #Maybe add functionality to show how long it took to do

#Function Call
CollatzFunc(1005)
