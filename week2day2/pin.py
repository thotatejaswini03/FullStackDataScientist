pin="1234"
attempts=3
for i in range(attempts+1):
    input_pin=input("Enter your pin:")
    if(input_pin==pin):
        print("Access granted")
        break
    else:
        attempts-=1
        print("Incorrect pin total attempts left:",attempts)
        if(attempts==0):
            print("Account locked")
            break
else :
    print("access denied")