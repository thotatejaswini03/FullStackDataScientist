class InsufficentFunds(Exception):
    pass
balance=1000
withdraw_amount=int(input("Enter the amount to withdraw:"))
try:
    if balance<withdraw_amount:
        raise InsufficentFunds("Insufficient funds in your account")
    else:
        balance-=withdraw_amount
        print("Transaction successful. Remaining balance:",balance)
    
except InsufficentFunds as e:
    print(e)