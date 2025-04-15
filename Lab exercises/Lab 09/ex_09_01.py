# Write a program that divides two numbers and prints the output
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is zero to avoid division by zero
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is: {result}")

""" Output:

Enter the first number: 5
Enter the second number: 2
The result of dividing 5.0 by 2.0 is: 2.5

"""