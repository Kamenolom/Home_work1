number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
operation = input("Enter operation: +,-,*,/ is:")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 !=0:
        result = number1 / number2
    else:
        result  = "Enter correct number not '0'"
print("Your result is:" ,result)



