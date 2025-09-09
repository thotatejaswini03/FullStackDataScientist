try:
    units=float(input("Enter the units consumed:"))
    if units<0:
        raise ValueError("Units cannot be negative")
    if units<=100:
        bill=units*5
    elif units<=200:
        bill=100*5+(units-100)*7            
    else:
        bill=100*5+100*7+(units-200)*10
    print("The total bill amount is:",bill)
except ValueError as ve:
    print("Error:", ve) 
finally:
    print("bill process finished")