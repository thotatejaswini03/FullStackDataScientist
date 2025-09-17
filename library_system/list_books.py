# list_books.py
from config import sb

def list_books():
    response = sb.table("books").select("*").execute()
    return response.data

if __name__ == "__main__":
    books = list_books()
    for book in books:
        print(book)
