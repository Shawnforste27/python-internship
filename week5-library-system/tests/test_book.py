from library_system.book import Book

b = Book("Test Book", "Author", "123")
assert b.available == True
print("Book test passed")
