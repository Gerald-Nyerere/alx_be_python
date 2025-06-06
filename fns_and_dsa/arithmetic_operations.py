def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "devide":
        if num2 == 0:
            return "Error cannot devide by zero"
        return num1 / num2
    else: 
        return "invalid operation"

