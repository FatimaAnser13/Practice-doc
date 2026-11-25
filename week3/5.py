# Book 
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Pages must be greater than 0")
        self._pages = value

    def get_info(self):
        return f"Title: {self.title} | Author: {self.author} | Pages: {self.pages}"


# EBook 
class EBook(Book):
    def __init__(self, title, author, pages, file_size_mb):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb

    @property
    def file_size_mb(self):
        return self._file_size_mb

    @file_size_mb.setter
    def file_size_mb(self, value):
        if value <= 0:
            raise ValueError("File Size must be greater than 0")
        self._file_size_mb = value

    def get_info(self):
        return f"{super().get_info()} | Size: {self.file_size_mb}MB"


# AudioBook 
class AudioBook(Book):
    def __init__(self, title, author, pages, duration_hrs):
        super().__init__(title, author, pages)
        self.duration_hrs = duration_hrs

    @property
    def duration_hrs(self):
        return self._duration_hrs

    @duration_hrs.setter
    def duration_hrs(self, value):
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        self._duration_hrs = value

    def get_info(self):
        return f"{super().get_info()} | Duration: {self.duration_hrs}hrs"


books = [
    Book("Clean Code", "Robert Martin", 431),
    EBook("Python Crash Course", "Eric Mathes", 544, 3.2),
    AudioBook("Atomic Habits", "James Clear", 320, 5),
]

for book in books:
    print(book.get_info())



print("\nTest Validation:")

try:
    Book("Bad Book", "Nobody", -5)
except ValueError as err:
    print(err)

try:
    EBook("Bad EBook", "Nobody", 100, 0)
except ValueError as err:
    print(err)


try:
    AudioBook("Bad Audio", "Nobody", 200, -1)
except ValueError as err:
    print(err)


    