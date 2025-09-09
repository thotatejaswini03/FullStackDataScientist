class library:
    def __init__(self,books):
        self.books=books
    def borrow(self,title):
        if self.books.get(title,0)>0:
            self.books[title]-=1
            return f"you borrowed {title}"
        else:
            return f"{title} is not available"
    def return_book(self,title):
        self.books[title]=self.books.get(title,0)+1
        return f"you returned {title}"
    def show_books(self):
        return f"Available books: {self.books}"
    
lib=library({"python":3,"java":2,"c++":1})
print(lib.borrow("python"))
print(lib.return_book("java"))
print(lib.show_books())