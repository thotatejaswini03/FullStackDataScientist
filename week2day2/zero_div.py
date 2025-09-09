try:
    a=int(input("Enter the numerator:"))
    b=int(input("Enter the denominator:"))
    result=a/b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("The result is:",result)