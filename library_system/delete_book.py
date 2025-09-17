# delete_book.py
from config import sb

def delete_book(book_id):
    borrow = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute().data
    if borrow:
        print("Cannot delete book that is currently borrowed.")
        return
    response = sb.table("books").delete().eq("book_id", book_id).execute()
    return response.data

if __name__ == "__main__":
    book_id = int(input("Enter book ID to delete: ").strip())
    result = delete_book(book_id)
    print("Deleted book:", result)
