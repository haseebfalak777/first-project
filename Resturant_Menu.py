# Creating Menu
menu = {
    "Pizza": 1000,
    "Burger": 500,
    "Salad": 400,
    "Pasta": 350,
    "Coke": 100,
}
# Greet and show returant menu

name = input("Enter your Name : ")
print(f"Welcome 'Mr.{name}' to Our Resturant!")
print("Pizza = Rs1000\nBurger = Rs500\nSalad = Rs400\nPasta = Rs350\nCoke = Rs100")

# Creating a grand total variable to add sum of all ordre items

grand_total = 0

# Taking order from user

item1 = input("Enter the item you want to order : ")

if item1 in menu:
    grand_total += menu[item1]
    print(f"Your order of '{item1}' has been placed.")
else:
    print("Item is not avaible in the menu.")

# if user wants to buy some thing else:

another_order = input("Do you want to order something else: Yes/No ")

if another_order == "Yes":
    item2 = input("Enter the second item you want to order : ")
    if item2 in menu:
        grand_total += menu[item2]
        print(f"Your order of '{item2}' has been placed.")
    else:
        print("Item is not available in the menu.")


# Calculating total amount

print(f"Your Total bill is {grand_total}.")
print(f"Thank You for visiting us! 'Mr.{name}'\nLooking Forward to see you again.")
