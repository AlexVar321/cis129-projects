'''
    script: CIS129_JohnVarela_lab7.py
    action: a. reads in positive integers from the user
            b. calculates number of seats purchased within seat limit
            c. calculates price of seats purchased each
            d. displays a subtotal for each purchase
            e. displays total revenue from purchases
    author: John Alex Varela
    date:   11/06/2024
'''

def main():
    '''
    Main function makes loop to run the code for each 'section' of the theater

    action: prompts user to input positive number
            uses number input to calculate price per section and the total
            prints the totals per section and total price
    input: integer from user for each section
    output: total price per section and total price
    return: none
    '''
    #constants
    SECTION_NAMES = ["A", "B", "C"]
    SECTION_PRICES = [20, 15, 10]
    SECTION_SEATS = [300, 500, 200]

    #welcome message and spacing
    print("Welcom to the CIS129 Theater!")
    print()

    #local variables
    i = 0
    total = 0

    #while loop to process data input by user
    while i < len(SECTION_NAMES):
        
        #local variables to pull data from constants(lists)
        sectionName = SECTION_NAMES[i]
        sectionPrice = SECTION_PRICES[i]
        seatMax = SECTION_SEATS[i]

        #print statement to inform user of price and seats available in section
        print(f"Section {SECTION_NAMES[i]}: ${SECTION_PRICES[i]} per seat", 
              f"{SECTION_SEATS[i]} seats available.")
        
        #getting input from user 
        seatsBought = getSeats("How many seats would you like in section",
                                sectionName, seatMax)
        
        #calculations for subtotal and total
        subTotal = seatsBought * sectionPrice
        total += subTotal

        #printing the subtotal and the running total of each section
        print(f"Subtotal = ${subTotal}")
        print(f"Running total = ${total}")
        print()

        #increment increase
        i += 1

    #printing the final total
    print()
    print(f"Total = ${total}")
    
    
        

def getSeats(msg, section, seatMax):
    '''
    Uses professors getInteger() function to get an integer
    then confirms that the integer is within the range of the seats available

    action: gets integer from user
            checks if integer is greater than or equal to 0
            checks if integer is less than or equal to the SECTION_SEAT maximum
            returns integer
    input: integer from user
    output: prompts user to enter a valid integer if input integer is invalid
    return: integer
    '''

    #gets integer from getInteger() function
    integer = getInteger(msg, section)

    #checks if integer meets conditions
    if integer <= seatMax and integer >= 0:

        #returns valid integer
        return integer
    
    #loops user until they enter a valid integer
    else:
        print(f'Please enter a number between 0 and {seatMax}.')
        return getSeats(msg, section, seatMax)


def getInteger(msg, section):
    '''
    (Professors code) gets integer from the user and checks if it is an integer

    action: gets integer from user
            checks if input is a string
            prompts user to enter a valid input if string was input
    input: integer from user
    output: prompt for user to enter an integer
    return: integer
    '''

    #gets input from user
    myInteger = input(msg + " " + section + ": ")

    #checks and returns user input as an integer
    try:
        return int(myInteger) 
    
    #loops user until they enter a valid integer
    except ValueError:
        print(f'{myInteger} is not a valid integer. Please try again.')
        return getInteger(msg, section)
    
    





main()