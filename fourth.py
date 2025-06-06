op = str(input("Would you like to + - / * % : ")).lower()

if op == "+":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print(f"Your total is: {total}")

elif op == "-":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 - num2
    print(f"Your total is: {total}")

elif op == "*":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 * num2
    print(f"Your total is: {total}")

elif op == "/":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        total = num1 / num2
        print(f"Your total is: {total}")
    else:
        print("Error: Cannot divide by zero.")

elif op == "%":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        total = num1 % num2
        print(f"Your total is: {total}")
    else:
        print("Error: Cannot take modulo by zero.")

else:
    print("Invalid input")
    print("Please enter a valid input")
