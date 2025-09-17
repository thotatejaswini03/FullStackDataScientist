# return_book.py
from config import sb
from datetime import datetime

def return_book(member_id, book_id):
    borrow = sb.table("borrow_records")\
        .select("*")\
        .eq("member_id", member_id)\
        .eq("book_id", book_id)\
        .is_("return_date", None)\
        .single().execute().data
    if not borrow:
        print("No active borrow record found.")
        return
    # Update return date
    sb.table("borrow_records")\
        .update({"return_date": datetime.utcnow().isoformat()})\
        .eq("record_id", borrow["record_id"]).execute()
    # Increase stock
    book = sb.table("books").select("*").eq("book_id", book_id).single().execute().data
    sb.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()
    print("Book returned.")

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    book_id = int(input("Enter book ID: ").strip())
    return_book(member_id, book_id)
