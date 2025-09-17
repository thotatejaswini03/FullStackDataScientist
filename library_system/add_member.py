
from config import sb

def add_member(name, email):
    data = {"name": name, "email": email}
    response = sb.table("members").insert(data).execute()
    return response.data

if __name__ == "__main__":
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    result = add_member(name, email)
    print("Member added:", result)
