# John Varela,
# this code is a receipt for a coffee and muffin shop where the coffee is $5
# each and the muffins are $4 each with a 6% tax

# this is the main function to store my code 
def main():
    # predetermined variables for my code that are known from the start
    TAX_RATE = 0.06
    MUFFIN_PRICE = 4
    COFFEE_PRICE = 5
    COOKIE_PRICE = 2
    BAGEL_PRICE = 3
    # here i am asking for the quantity of items bought
    print("***************************************")
    print("My Coffee and Muffin shop")
    coffee_quantity = askQuantity("Number of coffees bought? ")
    muffin_quantity = askQuantity("Number of muffins bought? ")
    cookie_quantity = askQuantity("Number of cookies bought? ")
    bagel_quantity = askQuantity("Number of bagels bought? ")
    print("***************************************")
    # variables to do calculations for how many of each items were purchased 
    # and how much they cost
    muffin_total = muffin_quantity*MUFFIN_PRICE
    coffee_total = coffee_quantity*COFFEE_PRICE
    cookie_total = cookie_quantity*COOKIE_PRICE
    bagel_total = bagel_quantity*BAGEL_PRICE

    subtotal = coffee_total+muffin_total+bagel_total+cookie_total
    tax = subtotal*TAX_RATE
    total = subtotal+tax
    # here i am printing the actual receipt 
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(coffee_quantity, "Coffee at $5 each:", "$" + str(coffee_total))
    print(muffin_quantity, "Muffins at $4 each:", "$" + str(muffin_total))
    print(cookie_quantity, "cookies at $2 each:", "$" + str(cookie_total))
    print(bagel_quantity, "bagels at $3 each:", "$" + str(bagel_total))
    print("6% tax:", "$" + str(round(tax,2)))
    print("---------")
    print("total:", "$" + str(round(total,2)))
    print("Thanks for comming to my coffee and")
    print("muffin shop, we hope to see you again!")
    print("***************************************")
# function for getting a number from the user given a prompt
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
