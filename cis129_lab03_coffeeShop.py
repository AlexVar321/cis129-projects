# John Varela,
# this code is a receipt for a coffee and muffin shop where the coffee is $5 each and the muffins are $4 each with a 6% tax

# this is the main function to store my code 
def main():
    # these are my predetermined variables for my code that are known from the start
    taxrate = 0.06
    muffinprice = 4
    coffeeprice = 5
    cookieprice = 2
    bagelprice = 3
    # here i am asking for the quantity of items bought
    print("***************************************")
    print("My Coffee and Muffin shop")
    getcoffees = askQuantity("Number of coffees bought? ")
    getmuffins = askQuantity("Number of muffins bought? ")
    getcookies = askQuantity("Number of cookies bought? ")
    getbagels = askQuantity("Number of bagels bought? ")
    print("***************************************")
    # here i have more variables to do calculations for how many of each items were purchased and how much they cost
    Purchasedmuffins = getmuffins*muffinprice
    purchasedcoffees = getcoffees*coffeeprice
    purchasedcookies = getcookies*cookieprice
    purchasedbagels = getbagels*bagelprice

    purchaseditems = purchasedcoffees+Purchasedmuffins+purchasedbagels+purchasedcookies
    tax = purchaseditems*taxrate
    total = purchaseditems+tax
    # here i am printing the actual receipt 
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(getcoffees, "Coffee at $5 each:", purchasedcoffees)
    print(getmuffins, "Muffins at $4 each:", Purchasedmuffins)
    print(getcookies, "cookies at $2 each:", purchasedcookies)
    print(getbagels, "bagels at $3 each:", purchasedbagels)
    print("6% tax: ", tax)
    print("total: ", total)
    print("Thanks for comming to my coffee and\nmuffin shop, we hope to see you again!")
    print("***************************************")
# this is my function for getting a number from the user given a prompt
def askQuantity(prompt: str):
        flag = True
        while flag:
            user_input = input(prompt)
            if user_input.isdigit():
                print(user_input)
                flag = False
            else: print("please enter the quantity purchased. ")
        return int(user_input)
if __name__ == "__main__":
    main()
