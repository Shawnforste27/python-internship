from library_system.library import Library

def main():
    lib = Library()

    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Save & Exit")

        choice = input("Choose: ")

        if choice == "1":
            lib.add_book(
                input("Title: "),
                input("Author: "),
                input("ISBN: ")
            )

        elif choice == "2":
            lib.register_member(
                input("Name: "),
                input("Member ID: ")
            )

        elif choice == "3":
            lib.borrow_book(
                input("ISBN: "),
                input("Member ID: ")
            )

        elif choice == "4":
            lib.return_book(
                input("ISBN: "),
                input("Member ID: ")
            )

        elif choice == "5":
            lib.search_books(input("Search title: "))

        elif choice == "6":
            lib.save_data()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

main()
