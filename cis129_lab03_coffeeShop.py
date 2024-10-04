# John Varela,
# this code is a receipt for a coffee and muffin shop where the coffee is $5 each and the muffins are $4 each with a 6% tax

# this is the main function to store my code 
def main():
    # these are my predetermined variables for my code that are known from the start
    taxrate = 0.06
    muffinprice = 4
    coffeeprice = 5
    flag = True
    # here i have 2 while loops to get my inputted variables and check to make sure i am getting a number inputted from the user
    print("My Coffee and Muffin shop")
    while flag:
        getcoffees = input("number of coffees bought? ")
        if getcoffees.isdigit():
            print(getcoffees)
            flag = False
        else: print("please enter the number of coffees purchased.")
    flag = True
    while flag:
        getmuffins = input("number of muffins bought? ")
        if getmuffins.isdigit():
            print(getmuffins)
            flag = False
        else: print("please enter the number of muffins purchased.")
    # here i have more variables to do calculations for how many muffins and coffees were purchased and how much they cost
    Purchasedmuffins = int(getmuffins)*muffinprice
    purchasedcoffees = int(getcoffees)*coffeeprice
    purchaseditems = purchasedcoffees+Purchasedmuffins
    tax = purchaseditems*taxrate
    total = purchaseditems+tax
    # here i am printing the actual receipt 
    print(getcoffees, "Coffee at $5 each:", purchasedcoffees)
    print(getmuffins, "Muffins at $4 each:", Purchasedmuffins)
    print("6% tax: ", tax)
    print("total: ", total)



if __name__ == "__main__":
    main()
