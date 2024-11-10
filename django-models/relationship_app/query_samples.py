from relationship_app.models import Book, Librarian, Library,Author

def get_book_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Author.books.all()
        return books
    except Author.DoesNotExist:
        return None

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        books = Library.libraries.all()
        return books
    except Library.DoesNotExist:
        return None

def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)           # Fetch the library by name
        librarian = Librarian.objects.get(library=library)         # Get the librarian for this library
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None
