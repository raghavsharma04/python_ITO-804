# Write a Python function called divide_numbers that takes in two numbers as arguments, numerator, and denominator, and performs the division operation. However, the function should handle the following exceptions:
# If the numerator or denominator is not a valid number (i.e., not an integer or float), it should raise a ValueError with the message "Invalid number(s) provided."
# If the denominator is zero, it should raise a ZeroDivisionError with the message "Cannot divide by zero."
# If any other unexpected error occurs during the division, it should raise a generic Exception with the message "An error occurred during division."
# Your task is to implement the divide_numbers function according to the specifications above and include appropriate exception handling
def divide_numbers(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        raise ValueError("Invalid number(s) provided.")

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except Exception:
        raise Exception("An error occurred during division.")
