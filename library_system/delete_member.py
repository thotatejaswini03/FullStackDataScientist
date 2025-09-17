# delete_member.py
from config import sb

def delete_member(member_id):
    borrow = sb.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute().data
    if borrow:
        print("Cannot delete member with active borrow records.")
        return
    response = sb.table("members").delete().eq("member_id", member_id).execute()
    return response.data

if __name__ == "__main__":
    member_id = int(input("Enter member ID to delete: ").strip())
    result = delete_member(member_id)
    print("Deleted member:", result)
