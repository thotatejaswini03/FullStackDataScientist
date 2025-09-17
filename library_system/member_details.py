# member_details.py
from config import sb

def get_member_details(member_id):
    member = sb.table("members").select("*").eq("member_id", member_id).single().execute().data
    borrow = sb.table("borrow_records").select("book_id, borrow_date, return_date").eq("member_id", member_id).execute().data
    return member, borrow

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    member, borrow = get_member_details(member_id)
    print("Member Info:", member)
    print("Borrowed Books:", borrow)
