# You are given a list of strings representing names of fruits and a dictionary containing the quantity of each fruit in stock. Write a function called check_inventory that takes two parameters: the list of fruit names and the dictionary of fruit quantities. The function should check if each fruit in the list exists in the inventory dictionary and return a new list of fruits that are in stock.
# Write the code for the check_inventory function and provide an example usage to demonstrate its functionality.use the following as input:
# fruits = ["apple", "banana", "grape", "orange", "kiwi"]
# inventory = {"apple": 5, "banana": 10, "orange": 3}
def check_inventory(fruits, inventory):
    in_stock = []
    for fruit in fruits:
        if fruit in inventory:
            in_stock.append(fruit)
    return in_stock
fruits = ["apple", "banana", "grape", "orange", "kiwi"]
inventory = {"apple": 5, "banana": 10, "orange": 3}

result = check_inventory(fruits, inventory)
print("Fruits in stock:", result)
