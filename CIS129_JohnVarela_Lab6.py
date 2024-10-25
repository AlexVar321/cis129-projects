'''
    script: CIS129_JohnVarela_lab6.py
    action: a. reads in positive integers from the user
            b. calculates packs of hotdogs and buns needed
            c. displays result
    author: John Alex Varela
    date:   10/24/2024
'''

# imports math built in function
import math

def main():
    '''
    Main method to get how many hotdog packs and buns needed for the cookout
    and leftovers

    action: declares variables
            calculates hotdog packs and buns needed
            calculates leftover hotdogs and buns
            displays values
    input:  none
    output: Hotdogs left
            buns left
            hotdog packs needed
            bun packs needed
    return: none
    '''

    # Local variables and constants
    totalHotDogs = getTotalHotDogs()
    totalBuns = totalHotDogs
    DOGS = 10
    BUNS = 8

    # Calculations for hotdog packs and buns as well as leftovers
    minDogs = math.ceil(totalHotDogs / DOGS)
    minBuns = math.ceil(totalBuns / BUNS)
    dogsLeft = (DOGS * minDogs) - totalHotDogs
    bunsLeft = (BUNS * minBuns) - totalBuns
    
    # Display output here
    print("Hotdogs left:", dogsLeft)
    print("Buns left:", bunsLeft)
    print("Minimum hotdog packs needed:", minDogs)
    print("Minimum Bun packs needed:", minBuns)


def getTotalHotDogs():
    '''
    Function to get how many hotdogs are needed for the cookout
    
    action: prompts user to input amount of people are attending
            prompts user to input amount of hotdogs each person is eating
            prompts user to input positive number if a negative number is input
    input:  amount of people who are attending
            amount of hotdogs each person is eating
    output: none
    return: total number of hotdogs
    '''


    # While loop to ensure we get a positive number
    total = -1
    while total < 0:

        # Input from user to get amount of people and hotdogs per person
        people = int(input("How many people are attending? "))
        hotDogs = int(input("How many hotdogs is each person having? "))

        # Number of hotdogs needed
        total = people * hotDogs

        # If statement to prompt user to enter a number above zero then return total
        if total < 0:
            print("Please enter a number above 0")
    return (total)
# Calling main function
main()
