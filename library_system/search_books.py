# search_books.py
from config import sb

def search_books(column, keyword):
    response = sb.table("books").select("*").ilike(column, f"%{keyword}%").execute()
    return response.data

if __name__ == "__main__":
    column = input("Search by (title/author/category): ").strip().lower()
    keyword = input("Enter keyword: ").strip()
    books = search_books(column, keyword)
    for book in books:
        print(book)
