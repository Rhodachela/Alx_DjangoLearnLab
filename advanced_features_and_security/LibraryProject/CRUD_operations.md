# CRUD Operations for Book Model

## Create
Command:
```python
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
Expected Output: Created instance in the database.

Retrieve
Command: retrieved_book = Book.objects.get(title="1984")
Expected Output:<Book: 1984 by George Orwell (1949)>


Update
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

Expected Output:
<Book: Nineteen Eighty-Four by George Orwell (1949)>

Delete
retrieved_book.delete()
Expected Output:

(1, {'bookshelf.Book': 1})
Confirm deletion:

Book.objects.all()

