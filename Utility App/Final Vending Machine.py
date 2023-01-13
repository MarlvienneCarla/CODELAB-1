#In this final assessment in Programming Fundamentals, I'll be making a program simulating vending machine
#I add this at first so that I can bold texts later.
bold = "\33[1m"
normal = "\33[m"
#These are the products/items that I put in my vending machine.The Dictionary.
items_in_stock = [
    {
        "item_id": 0,
        "item_name": (f"{bold}Milky Way{normal}"),
        'item_price': 6,
    },
    {
        "item_id": 1,
        "item_name": "Hot Chocolate",
        'item_price': 2,
    },
    {
        "item_id": 2,
        "item_name": "Coke",
        'item_price': 5,
    },
    {
        "item_id": 3,
        "item_name": "Coffee",
        'item_price': 2,
    },
    {
        "item_id": 4,
        "item_name": "Bueno",
        'item_price': 6,
    },
    {
        "item_id": 5,
        "item_name": "Water",
        'item_price': 2,
    },
]


the_item = []

receipt = """
\t\tPRODUCT -- PRICE
"""

sum = 0

run = True

print(f"------------{bold}Python Automat{normal}------------\n\n")
print("----------The Items In Stock Are----------\n\n")

for i in items_in_stock:
    print(f"Item: {i['item_name']} --- Price: {i['item_price']} --- Item ID: {i['item_id']}")


def machine(items_in_stock, run, the_item):
    while run:

        buy_item = int(input("\n\nEnter the item code of the product you want to buy: "))

        if buy_item < len(items_in_stock):
            the_item.append(items_in_stock[buy_item])
        else:
            print("THE PRODUCT ID IS WRONG!")

        more_items = str(input("Press any key to add more items and press q to quit: "))

        if more_items == "q":
            run = False

    rec_bool = int(input(("1. Print the receipt? 2. Only print the total sum: ")))
    if rec_bool == 1:
        print(create_receipt(the_item, receipt))
    elif rec_bool == 2:
        print(sum(the_item))
    else:
        print("INVALID ENTRY")


def sum(the_item):
    sum = 0
    for i in the_item:
        sum += i["item_price"]
    return sum

def create_receipt(the_item, receipt):
    for i in the_item:
        receipt += f"""
        \t{i["item_name"]} -- {i['item_price']}
        """
    receipt += f"""
        \tTotal --- {sum(the_item)}
        
        """
    return receipt
if __name__ == "__main__":
    machine(items_in_stock, run, the_item)  
#Here, I defined a variable for the ultimate cost and a place for the user to enter the payment information.
total = sum(the_item)
totalmoney = 0

#Additionally, I have a list that I can add to all the products the consumer will purchase to later display it.
itemsbought = []

#It instructs the user to enter payment in order to acquire the ordered things.
print("\nTo purchase, please insert money.\n")

# These three lines tell the user of the acceptable coins and bills as well as the minimum amount needed to make a purchase, which is 5 dhs.
print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
print("All coins are accepted.\n")
print(f"The minimum amount is {bold}AED 5{normal}")
    
money = (float(input("Please insert here: ")))
totalmoney += money #It will be included in the totalmoney variable.

#This while loop handles the variable below.
while totalmoney < total:
    #The following is printed first, and the user is prompted to enter more cash.
    print(f"Almost there! Just {bold}AED {total - totalmoney}{normal} left.")
    money = (float(input("\nPlease insert here: ")))
    totalmoney += money
    
    if totalmoney >= total:
        #The text below will be written when the sum of all the user-inputted money is more than or equal to the bill;
        print(f"\nGreat! You inserted a total of {bold}AED {totalmoney}{normal}.")
        break
    
    #and when the money inserted is invalid, this else phrase is what happens.   
    else:
        #For the user's convenience, I made the program ask them to enter their payment information once again.
        print(f"\n{bold}Invalid bill/s or coin/s.{normal}")
        print("Please try again.\n")
            
        print(f"The available bills are {bold}5{normal}, {bold}10{normal}, {bold}20{normal}, and {bold}50{normal}")
        print("All coins are accepted.\n")
        print(f"The minimum amount is {bold}AED 5{normal}")
            
        money = (float(input("\nPlease insert here: ")))
        totalmoney += money
      #I also entered the same loop from before.
        while totalmoney <= total:
            print(f"Almost there! Just AED {total - totalmoney} left.")
            money = (float(input("\nPlease insert here: ")))
            totalmoney += money
#Final part of the program
change = totalmoney - total #I created a formula to determine the change first.
if change <= 0: #Now, the user won't get any change if change is 0.
    print("You have no change.\n") #The user will instead see this message.
    print("Thank you!\n")

#If not, the user will see the following message.
else:
    print(f"Your change is {bold}AED {change}{normal}\n") #The overall change will be displayed.
    print("Thank you!\n")