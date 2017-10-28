import random
import time

#Collatz Conjecture
    #This program will take in an input integer
    #or generate a random int
    #from 1 to 10,000
    #Choose random int with input value of -1

#---------------------------------------------------------------------
#INPUT
Test_Num = input('Enter your input value: ')

if int(Test_Num) == -1:                         #Checks for random value generation
    Test_Num = random.randint(1,10000)          #Generate random number
    print('Random Number Chosen: ', Test_Num)
else:
    print('Chosen Number: ',Test_Num)           #Prints the number that has been input
#---------------------------------------------------------------------
#COLLATZFUNC FUNCTION DEFINITION
Test1 = False
Test2 = False
Test3 = True
waitTime = .2                                   #Amount of time to wait before executing next operation

def CollatzFunc(input):
    temp1= int(input)
    num_operations = 0                          #counter for the total number of Operations
    num_even = 0                                #To keep track of even numbers
    num_other = 0                               #To keep track of Odds

    if Test2:                                   #Test if the program gets to here
        print('BEFORE THE FOR LOOP')

    while temp1 != 1.0:                         #Base case to drop out of the loop

        if Test2:                               #Test if the program gets to here
            print('INSIDE THE FOR LOOP')

        if temp1 % 2 == 0:                      #If the value is even
            temp1 = temp1/2
            num_operations += 1
            num_even += 1
            print(int(temp1))
            if(Test1):
                print('Divide by 2\n')
                print('Current Number of Operations: ',num_operations)

            time.sleep(waitTime)
        else:                                   #The Number is not even
            temp1 = ((temp1 * 3) + 1)           #Multiply by 3 and add 1
            num_operations += 1                 #increment Counters
            num_other += 1
            print(int(temp1))
            if(Test1):
                print('Multiply by 3, add 1\n')
                print('Current Number of Operations: ',num_operations)
            time.sleep(waitTime)                #make the program wait so we can watch it execute

    #Outside of the while loop
    print('Starting Number: ',Test_Num)
    print('Total Number of Operations: ',num_operations)
    print('Number of Even Ops: ', num_even)
    print('number of Other Ops: ', num_other)
#---------------------------------------------------------------------

#Function Call
CollatzFunc(Test_Num)
