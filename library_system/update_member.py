# update_member.py
from config import sb

def update_member(member_id, new_email):
    response = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    return response.data

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    new_email = input("Enter new email: ").strip()
    result = update_member(member_id, new_email)
    print("Updated member:", result)
