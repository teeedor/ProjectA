# FIZZBUZZ.py
#This program is the common programming problem FIZZ BUZZ
#you must print out the first 100 numbers and every time the number is
#divisible by 3, print FIZZ, and for those divisible by 5 print BUZZ
#Obviously combine them when both statements are true

#Loop through and print all numbers 1 to 100
for i in range(1,101):
    #Check to see if Both conditions are satisfied first
    if i%3 ==0 and i%5 == 0:
        print("FIZZBUZZ")
    else:
        if i%3 == 0:
            #Write FIZZ
            print("FIZZ")
        if i%5 == 0:
            #Write BUZZ
            print("BUZZ")
        else:
            print(i)
