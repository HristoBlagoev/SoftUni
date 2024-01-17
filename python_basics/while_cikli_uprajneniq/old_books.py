book_name = input()
book_counter = 0
book_is_found = False

current_book = input()
while current_book != 'No More Books':
    if current_book == book_name:
        book_is_found = True
        break
    book_counter += 1
    current_book = input()

if book_is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")

