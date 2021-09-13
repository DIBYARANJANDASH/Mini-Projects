class Library:
    def __init__(self,books, aname):
        self.Books = books
        self.Name = aname
        self.lended = []

    def display_book(self):
        print("Name of all the books present are : \n")
        print("....................")
        for i in self.Books:
            print(i)
        return "...................."

    def add_book(self):
        new = input("Enter the name of the book you want to add/return: ")
        self.Books.append(new)
        return "\nBook added to library..."

    def lend_book(self):

        lend = input("Enter the name of the book you want to borrow: ")
        len_time = input("Enter the duration you want to keep it: ")
        flag = 0
        for j in self.Books:
            if lend == j:
                flag = 1

        if flag == 1:
                print("Book is available so you can borrow it for {} duration".format(len_time))
                self.lended.append(lend)
                self.Books.remove(lend)
        else:
            print("Book is already lended to someone")


print(".......WELCOME TO DIBYA'S LIBRARY.......")
name = input("Enter your name: ")
Dibya = Library(["Programming with C", "Harry Potter", "Java", "Sherlock Homes"], name)
while True:
    print("\n1. Display books\n2. Add book\n3. Borrow a Book\n4. Return a book\n5. Exit the library")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print(Dibya.display_book())
    elif choice == 2:
        print(Dibya.add_book())
    elif choice == 3:
        Dibya.lend_book()
    elif choice == 4:
        print(Dibya.add_book())
    else:
        exit(0)


