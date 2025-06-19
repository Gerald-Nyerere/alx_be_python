class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self):
        return f'Book: {self.title} by {self.author}'

    def __str__(self):
        return self.get_details()


class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f'EBook: {self.title} by {self.author}, File Size: {self.file_size}KB'


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f'PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}'
