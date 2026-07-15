while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = (input("Enter the operation +, -, *, / :"))
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Enter correct number, not 0!")
    print(result)
    answer = input("Do you want to continue?Enter: 'y' or 'n' :")
    if answer == 'y':
        continue
    else:
        break








