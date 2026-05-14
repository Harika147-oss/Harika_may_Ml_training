def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book", book_id, "borrowed successfully")
    else:
        print("Book cannot be borrowed")
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book", book_id, "returned successfully")
    else:
        print("Book not found in borrowed list")
def register_member(members, member_id):
    members.add(member_id) 
def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(book_id, "-", title, ",", author, ",", year)
def main():
    catalog = {}
    borrowed_books = []
    members = set()
    add_book(catalog, 101, "Python Basics", "John", 2020)
    add_book(catalog, 102, "Data Structures", "David", 2019)
    add_book(catalog, 103, "Machine Learning", "Andrew", 2021)
    add_book(catalog, 104, "AI Fundamentals", "James", 2022)
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)
    print("Members:", members)
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 102)
    return_book(borrowed_books, 101)
    show_available(catalog, borrowed_books)
main()
