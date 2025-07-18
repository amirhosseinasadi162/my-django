import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {"title": self.title, "author": self.author}


class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, book):
        self.books.append(book.to_dict())
        self.save_books()
        print(f"✅ کتاب '{book.title}' اضافه شد.")

    def list_books(self):
        if not self.books:
            print("هیچ کتابی یافت نشد.")
            return
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book['title']} by {book['author']}")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book['title'].lower()]
        if found_books:
            for book in found_books:
                print(f"✅ پیدا شد: {book['title']} by {book['author']}")
        else:
            print("کتاب مورد نظر پیدا نشد.")

    def delete_book(self, title):
        initial_count = len(self.books)
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]
        if len(self.books) < initial_count:
            self.save_books()
            print(f"✅ کتاب '{title}' حذف شد.")
        else:
            print("کتاب مورد نظر برای حذف پیدا نشد.")
