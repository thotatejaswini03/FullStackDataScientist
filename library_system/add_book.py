# add_book.py
from config import sb

def add_book(title, author, category, stock):
    data = {"title": title, "author": author, "category": category, "stock": stock}
    response = sb.table("books").insert(data).execute()
    return response.data

if __name__ == "__main__":
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category: ").strip()
    stock = int(input("Enter stock count: ").strip())
    result = add_book(title, author, category, stock)
    print("Book added:", result)
