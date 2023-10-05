maths_operation = input("Enter Maths Operation (x, +, - or / : ) ")
first_number_string: str = input("Enter first number: ")
first_number = int(first_number_string)

second_number_string: str = input("Enter second number: ")
second_number = int(second_number_string)


if maths_operation == '+':
    print (first_number + second_number)
elif maths_operation == '-':
    print (first_number - second_number)
elif maths_operation == 'x':
    print (first_number * second_number)
elif maths_operation == '/':
    print (first_number / second_number)
