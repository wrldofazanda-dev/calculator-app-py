# get first number
first_number = input("Please enter the first number: ")
# get the second number
second_number = input("Please enter the second number:")
# get the operation
operation = input("Please enter the operation (ADD, SUB, MUL, DIV):")
# check which operation was entered
if operation == "ADD":
    # add the number
    result = int(first_number) + int(second_number)
elif operation == "SUB":
    # subtract the number
    result = int(first_number) - int(second_number)
elif operation == "MUL":
    # subtract the number
    result = int(first_number) * int(second_number)
elif operation == "DIV":
    # subtract the number
    result = int(first_number) / int(second_number)
# return the result to the user
print("The result is: ", str(result))