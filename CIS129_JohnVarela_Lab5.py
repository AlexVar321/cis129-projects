# John Alex Varela
# 10/15/2024
# code for grocery store to track the number of bottles collected for the week.

# main method
def main():

    # Lab 5 The Bottle Return Program

    # Step 1: Declare variables as stated in psudo code in document
    totalBottles = 0
    counter = 1
    todayBottles = 0
    totalPayout = 0
    keepGoing = "y"

    # Step 2: Loop to run program again  
    while keepGoing == "y":

        # code to set value of variables
        NBR_OF_DAYS = 7
        PAYOUT_PER_BOTTLE = 0.10
        counter = 0
        totalBottles = 0

        # Loop for data of each day and calculate payout for amount of bottles
        while counter < NBR_OF_DAYS:
            
            # getting input from user and calculating total bottles
            todayBottles = int(input(
                "Enter number of bottles returned for day #"
                  + str(counter + 1) + ": "))
            totalBottles = totalBottles + todayBottles
            counter += 1

        # printing desired output and calculating payout
        print()
        totalPayout = totalBottles * PAYOUT_PER_BOTTLE
        print("The total Number of bottles collected is", totalBottles)
        print(f"The total payout is $ {totalPayout:.2f}")
        print()

        # asking user if they want to repeat
        print("Do you want to enter another week's worth of data?")
        keepGoing = input("(Enter y or n): ")
main()