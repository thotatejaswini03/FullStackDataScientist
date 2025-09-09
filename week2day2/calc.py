def calc(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b==0:
            return "Error: Division by zero"
        return a/b
    else:
        return "Invalid operation"
print(calc(10,5,'+'))


    