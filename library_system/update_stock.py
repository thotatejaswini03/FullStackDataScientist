# update_stock.py
from config import sb

def update_stock(book_id, new_stock):
    response = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return response.data

if __name__ == "__main__":
    book_id = int(input("Enter book ID: ").strip())
    new_stock = int(input("Enter new stock count: ").strip())
    result = update_stock(book_id, new_stock)
    print("Updated book:", result)
