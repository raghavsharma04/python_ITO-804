# You must take following list of dictionaries representing students and their scores in different subjects:
# students = [
# {'name': 'Alice', 'math':85, 'physics':92, 'chemistry':78},
# {'name': 'Bob', 'math':90, 'physics':78, 'chemistry':85},
# {'name': 'David', 'math':92, 'physics':90, 'chemistry':95},
# {'name': 'Charlie', 'math':80, 'physics':88, 'chemistry': 90},]
# Write a lambda function that takes a student dictionary as input and returns their average score across all subjects. Use this lambda function along with the max() function to find the student with the highest average score. Write the code to demonstrate the usage of the lambda function and print the name of the student with the highest average score.
students = [
    {'name': 'Alice', 'math': 85, 'physics': 92, 'chemistry': 78},
    {'name': 'Bob', 'math': 90, 'physics': 78, 'chemistry': 85},
    {'name': 'Charlie', 'math': 80, 'physics': 88, 'chemistry': 90},
    {'name': 'David', 'math': 92, 'physics': 90, 'chemistry': 95}
]

# Lambda function to calculate average score
calculate_average = lambda student: (student['math'] + student['physics'] + student['chemistry']) / 3

# Find the student with the highest average score
highest_average_student = max(students, key=calculate_average)

# Print the name of the student with the highest average score
print("Student with the highest average score:", highest_average_student['name'])
