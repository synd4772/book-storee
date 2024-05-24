from __future__ import annotations

"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books = list()


    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        if isinstance(book, Book):
            if book.rating >= self.rating:
                for book_object in self.books:
                    if book_object.author == book.author and book_object.title == book.title:
                        return False
                return True
        return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):

            self.books.append(book)
        else:
            return False


    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if isinstance(book, Book) and book in self.books:
            return True
        return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.remove(book)
        else:
            return False
        

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        
        return self.books

    @staticmethod
    def sort_by(instances, by:str, cheapest:bool):
        return_list = []
        max_var = 0
        min_var = None
        for instance in instances:
            if by == "price":
                if cheapest:
                    if min_var is None:
                        min_var = instance.price
                        return_list.append(instance)
                    elif min_var < instance.price:
                        min_var = instance.price
                        return_list.insert(0, instance)
                    else:
                        return_list.append(instance)
                else:
                    if instance.price > max_var:
                        return_list.insert(0, instance)
                        max_var = instance.price
                    else:
                        return_list.append(instance)
            elif by == "popular":
                if cheapest:
                    if min_var is None:
                        min_var = instance.popular
                        return_list.append(instance)
                    elif min_var < instance.popular:
                        min_var = instance.popular
                        return_list.insert(0, instance)
                    else:
                        return_list.append(instance)
                else:
                    if instance.rating > max_var:
                        return_list.insert(0, instance)
                        max_var = instance.rating
                    else:
                        return_list.append(instance)
        return return_list


    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return self.sort_by(self.books, by="price", cheapest=True)



    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        return self.sort_by(self.books, by="popular", cheapest=False)

#__init__(self, title: str, author: str, price: float, rating: float)
b1 = Book(title="Lupen", author="John Doe", price=55.99, rating=0.6)
b2 = Book(title="Lupen 2", author="John Doe", price=23.99, rating=0.4)


#__init__(self, name: str, rating: float)

s1 = Store("Prismo", 0.2)

s1.add_book(b1)
s1.add_book(b2)
print("ALL")
all_books = s1.get_all_books()
for book_object in all_books:
    
    print(book_object.title, 123)

print("ALL\n")

print("PRICE")
all_books_by_price = s1.get_books_by_price()
for book_price in all_books_by_price:
    
    print(book_price.title)

print("PRICE\n")

print("POPULAR")
all_book_by_popular = s1.get_most_popular_book()
for book_popular in all_book_by_popular:
    print(book_popular.title)

print("POPULAR\n")

print("DELETING")
s1.remove_book(b1)
for book_object in all_books:
    print(book_object.title)
print("DELETING")