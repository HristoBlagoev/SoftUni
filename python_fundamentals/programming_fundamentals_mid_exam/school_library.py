array_of_books = input().split('&')
command = input().split(" | ")

while command[0] != 'Done':
    action = command[0]

    if action == 'Add Book':
        book = command[1]
        if book not in array_of_books:
            array_of_books.insert(0, book)
    elif action == 'Take Book':
        book = command[1]
        if book in array_of_books:
            array_of_books.remove(book)
    elif action == 'Swap Books':
        book1, book2 = command[1], command[2]
        if book1 in array_of_books and book2 in array_of_books:
            i = array_of_books.index(book1)
            x = array_of_books.index(book2)
            array_of_books[i], array_of_books[x] = array_of_books[x], array_of_books[i]
    elif action == 'Insert Book':
        book = command[1]
        if book not in array_of_books:
            array_of_books.append(book)
    elif action == 'Check Book':
        index = int(command[1])
        if 0 <= index < len(array_of_books):
            print(array_of_books[index])

    command = input().split(" | ")

print(*array_of_books, sep=', ')