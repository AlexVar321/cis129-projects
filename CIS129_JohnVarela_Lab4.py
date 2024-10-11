# Module 4 Lab-4
# John Alex Varela
# 10/10/2024
# program calculates store profits and bonuses to give the store and employees

# the main function
def main():

# declare local variables
    monthlySales = 0 # monthly sales amount
    storeAmount = 0 # store bonus amount
    empAmount = 0 # employee bonus amount
    salesIncrease = 0 # percent of sales increase

# call to getSales
    monthlySales = getSales("Enter the monthly sales ")

# call to getIncrease
    salesIncrease = getIncrease("enter the percent of sales increase: ")

# call to calcStoreBonus
    storeAmount = calcStoreBonus(monthlySales)

# call to calcEmpBonus
    empAmount = calcEmpBonus(salesIncrease)

# call to printBonus    
    printBonus(storeAmount,empAmount)

# This function prints the bonus information
def printBonus(storeAmount,empAmount):
    print("the store bonus is $", storeAmount)
    print("the employee bonus is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible!")

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return (empAmount)

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
       storeAmount = 5000
    elif monthlySales >= 90000:
       storeAmount = 4000
    elif monthlySales >= 80000:
       storeAmount = 3000
    else: storeAmount = 0 
    return(storeAmount)

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease/100
    return (salesIncrease)

# This function gets the monthly sales
def getSales(prompt):
 monthlySales = float(input(prompt))
 return monthlySales


# calls main
main()
    