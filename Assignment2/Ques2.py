# You are working on a program that involves mapping functions to perform various operations on data. You decide to use a dictionary to store the mapping of function names to their corresponding functions.
# a) Create a dictionary called function map with the following key-value pairs:
# Key: 'add', Value: A function that takes two numbers as input and returns their sum.
# Key: 'subtract', Value: A function that takes two numbers as input and returns their difference.
# Key: 'multiply', Value: A function that takes two numbers as input and returns their product.
# Key: 'divide', Value: A function that takes two numbers as input and returns their division.
# b) Write a program that asks the user to enter two numbers and an operation (add, subtract, multiply, or divide). Use the function_map dictionary to retrieve the appropriate function based on the user's operation choice and perform the operation on the entered numbers. Print the result.

# Solution 1: Create the function map dictionary
function_map = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y
}
# Step 2: Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

# Step 3: Perform the operation using function_map
if operation in function_map:
    result = function_map[operation](num1, num2)
    print("Result:", result)
else:
    print("Invalid operation!")
