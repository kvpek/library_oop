import csv

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"
        

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
            self.books.append(book)
            print(f"Book '{book.title}' by {book.author} added to library.")
    def show_books(self):
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")
    def borrow_book(self, title):
        found = False
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip() and book.is_borrowed == False:
                book.is_borrowed = True
                found = True
                print("Task completed. You borrow this book. Please return it in 30 days from today. Thank you!")
                break
        if not found:
            print("Your book is not available or you insert something wrongly. Try again.")
    def return_book(self, title):
        found = False
        for book in self.books:        
            if book.title.lower().strip() == title.lower().strip() and book.is_borrowed == True:
                book.is_borrowed = False
                found = True
                print("Task completed. You have returned your book. Thank you!")
                break
        if not found:
            print("There is something wrong... Try again!")        
    def save_to_file(self, filename="library.csv"):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "is_borrowed"])
            for book in self.books:
                writer.writerow([book.title, book.author, book.is_borrowed])
    def load_from_file(self, filename='library.csv'):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title = row[0]
                author = row[1]
                is_borrowed = (row[2] == "True")
                
                book = Book(title, author, is_borrowed)
                self.books.append(book)
    def add_book_x(self):
        title = input("Title: ")
        author = input("Author: ")
        self.add_book(Book(title, author))
        self.save_to_file()
                
                
# library = Library()

# books = [
#     Book("Harry Potter i Kamień Filozoficzny", "J.K. Rowling"),
#     Book("Hobbit", "J.R.R. Tolkien"),
#     Book("Władca Pierścieni", "J.R.R. Tolkien"),
#     Book("Mały Książę", "Antoine de Saint-Exupéry"),
#     Book("Zbrodnia i kara", "Fiodor Dostojewski"),
#     Book("Lalka", "Bolesław Prus"),
#     Book("Opowieść wigilijna", "Charles Dickens"),
#     Book("Duma i uprzedzenie", "Jane Austen"),
#     Book("Mistrz i Małgorzata", "Michaił Bułhakow"),
#     Book("1984", "George Orwell")]
# for b in books:
#     library.add_book(b)
# library.save_to_file()

library = Library()
library.load_from_file()
library.show_books()

while True:
    q = int(input("1. Borrow book. \n2. Return a book. \n3. Show books. \n4. Add new book to the library. \n10. End the process. \nChoose what action do you want to make: "))
    
    if q == 1:
        title = input("Book title to borrow: ")
        library.borrow_book(title)
        library.save_to_file()
        
    elif q == 2:
        title = input("Book title to return: ")
        library.return_book(title)
        library.save_to_file()
    elif q == 3:
        library.show_books()
        
    elif q == 4:
        library.add_book_x()
        
    elif q == 10:
        library.save_to_file()
        break
