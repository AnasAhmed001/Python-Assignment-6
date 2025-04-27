class Book:
    total_books = 0  # Class variable to track total number of books
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    def get_info(self):
        return f"'{self.title}' by {self.author}"
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books


# Initial count
print(f"Initial total books: {Book.get_total_books()}")

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
print(f"After adding '{book1.title}', total books: {Book.get_total_books()}")

book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(f"After adding '{book2.title}', total books: {Book.get_total_books()}")

# Create multiple books at once
books = [
    Book("1984", "George Orwell"),
    Book("The Hobbit", "J.R.R. Tolkien"),
    Book("Pride and Prejudice", "Jane Austen")
]
print(f"After adding 3 more books, total books: {Book.get_total_books()}")

# Manually increment (though typically this would happen automatically)
Book.increment_book_count()
print(f"After manually incrementing, total books: {Book.get_total_books()}")
