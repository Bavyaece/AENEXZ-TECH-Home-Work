def add_book(catalog, book_id, title, author, year):
    # value stored as tuple -> immutable book details
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist.")
        return
    if book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
        return
    borrowed_books.append(book_id)
    print(f"Book ID {book_id} borrowed successfully.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


def register_member(members, member_id):
    if member_id in members:
        # silently ignore duplicates
        return
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("Available Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  ID {book_id}: {title} by {author} ({year})")


def main():
    catalog = {}            # dict: book_id -> (title, author, year)
    borrowed_books = []     # list: keeps order of borrowed book ids
    members = set()         # set: unique member ids

    # Add 4 books
    add_book(catalog, 1, "The Alchemist", "Paulo Coelho", 1988)
    add_book(catalog, 2, "Atomic Habits", "James Clear", 2018)
    add_book(catalog, 3, "Deep Work", "Cal Newport", 2016)
    add_book(catalog, 4, "Clean Code", "Robert C. Martin", 2008)

    # Register 3 members, try adding one twice
    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M001")  # duplicate, ignored
    print("Registered Members:", members)

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    # Return 1 book
    return_book(borrowed_books, 1)

    # Show available books
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()
