# John Varela,
# this code is a receipt for a coffee and muffin shop where the coffee is $5
# each and the muffins are $4 each with a 6% tax

# predetermined variables for my code that are known from the start
TAX_RATE = 0.06
MUFFIN_PRICE = 4
COFFEE_PRICE = 5
COOKIE_PRICE = 2
BAGEL_PRICE = 3
# here i am asking for the quantity of items bought
print("***************************************")
print("My Coffee and Muffin shop")
coffee_quantity = int(input("Number of coffees bought? "))
muffin_quantity = int(input("Number of muffins bought? "))
cookie_quantity = int(input("Number of cookies bought? "))
bagel_quantity = int(input("Number of bagels bought? "))
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
print(coffee_quantity, "Coffee at $5 each:", "$" ,(coffee_total))
print(muffin_quantity, "Muffins at $4 each:", "$" ,(muffin_total))
print(cookie_quantity, "cookies at $2 each:", "$" ,(cookie_total))
print(bagel_quantity, "bagels at $3 each:", "$" ,(bagel_total))
print("6% tax:", "$",(tax))
print("---------")
print("total:", "$", (total))
print("Thanks for comming to my coffee and")
print("muffin shop, we hope to see you again!")
print("***************************************")
