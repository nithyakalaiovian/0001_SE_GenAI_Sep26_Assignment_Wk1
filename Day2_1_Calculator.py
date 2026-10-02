# Chat gpt prompt - Write a simple Python calculator that supports addition, subtraction, multiplication, and division. Include error handling for invalid number input, invalid operators, and division by zero. In each except block, capture the exception as e and print the message using an f-string, such as print(f"Input error: {e}"). Show the complete code."and"
# Simple Calculator 
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Choose an operation (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator. Choose +, -, *, or /.")

    print(f"Result: {result}")

except ValueError as e:
    print(f"Input error: {e}")
except ZeroDivisionError as e:
    print(f"Math error: {e}")