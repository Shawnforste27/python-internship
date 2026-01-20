import json
import os
from library_system.book import Book
from library_system.member import Member

BOOK_FILE = "data/books.json"
MEMBER_FILE = "data/members.json"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print("Book already exists.")
            return
        self.books[isbn] = Book(title, author, isbn)

    def register_member(self, name, member_id):
        if member_id in self.members:
            print("Member already exists.")
            return
        self.members[member_id] = Member(name, member_id)

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books or member_id not in self.members:
            print("Book or member not found.")
            return

        book = self.books[isbn]
        member = self.members[member_id]

        if not book.borrow(member_id):
            print("Book not available.")
            return

        if not member.borrow_book(isbn):
            print("Borrow limit reached.")
            book.return_book()
            return

        print("Book borrowed successfully.")

    def return_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            self.books[isbn].return_book()
            self.members[member_id].return_book(isbn)
            print("Book returned.")

    def search_books(self, keyword):
        for book in self.books.values():
            if keyword.lower() in book.title.lower():
                status = "Available" if book.available else "Borrowed"
                print(book.title, "-", status)

    def save_data(self):
        with open(BOOK_FILE, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open(MEMBER_FILE, "w") as f:
            json.dump({k: v.__dict__ for k, v in self.members.items()}, f, indent=4)

    def load_data(self):
        if os.path.exists(BOOK_FILE):
            with open(BOOK_FILE, "r") as f:
                data = json.load(f)
                for isbn, info in data.items():
                    self.books[isbn] = Book.from_dict(info)

        if os.path.exists(MEMBER_FILE):
            with open(MEMBER_FILE, "r") as f:
                data = json.load(f)
                for mid, info in data.items():
                    member = Member(info["name"], mid)
                    member.borrowed_books = info["borrowed_books"]
                    self.members[mid] = member
