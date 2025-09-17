# borrow_book.py
from config import sb
from datetime import datetime

def borrow_book(member_id, book_id):
    book = sb.table("books").select("*").eq("book_id", book_id).single().execute().data
    if not book or book["stock"] < 1:
        print("Book not available.")
        return
    # Decrease stock
    sb.table("books").update({"stock": book["stock"] - 1}).eq("book_id", book_id).execute()
    # Insert borrow record
    record = {"member_id": member_id, "book_id": book_id}
    sb.table("borrow_records").insert(record).execute()
    print("Book borrowed.")

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    book_id = int(input("Enter book ID: ").strip())
    borrow_book(member_id, book_id)
