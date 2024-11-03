# Retrieve Operation for Book Model

### Command:
```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="Sample Book")
retrieved_book

Expected Output:
<Book: Sample Book by Author Name (2024)>