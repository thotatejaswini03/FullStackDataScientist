import re
def is_strong_password(password):
    if len(password)<8 :
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[@#$%^&+=]',password):
        return False
    return True
password=input("Enter your password: ")
if is_strong_password(password):
    print("Strong password")
else:
    print("Weak password")