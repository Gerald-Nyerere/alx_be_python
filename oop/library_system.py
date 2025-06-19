class Book:
    def  __init__(self, title:str, author:str):
        self.title = title
        self.author = author

    def get_details(self):
        return f'{self.title} by {self.author}'
    
    def __str__(self):
        return self.get_details()
class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)

        self.file_size = file_size

    def get_details(self):
        return f'{super().get_details()} [EBook, {self.file_size}MB]'

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)

        self.page_count = page_count
    
    def get_details(self):
        return f'{super().get_details()} [PrintBook, {self.page_count} pages]'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book) 
    
    def list_books(self, ):
        if not self.books:
             print("No books in the library.")
        else:
            for book in self.books:
                print(book.get_details())
        