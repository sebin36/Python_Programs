import library

def main():
    lib = []
    while True:
        b1 = library.Library(lib)
        print('\nMenu')
        print('1.Add Book')
        print('2.Remove Book')
        print('3.List Books')
        opt = int(input('Enter Choice: '))
        if opt == 1:
            book = input('Enter Book Title: ')
            b1.add_book(book)
        elif opt == 2:
            book = input('Enter Book to Delete: ')
            b1.remove_book(book)
        elif opt == 3:
            print(b1.list_books())
        else:
            print('Done')
            break      

main()
        


