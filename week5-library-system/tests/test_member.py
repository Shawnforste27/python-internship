from library_system.member import Member

m = Member("John", "M1")
assert m.borrow_book("123") == True
print("Member test passed")
