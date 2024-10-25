# John Alex Varela
# 10/24/2024
# Code for calculating hotdog packs and bun packs needed for hotdog cookout


import math

# Main method to process data
def main():

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

# Function to get the total number of hotdogs needed at the cookout
def getTotalHotDogs():

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
