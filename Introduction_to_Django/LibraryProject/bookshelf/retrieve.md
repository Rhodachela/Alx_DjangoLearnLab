# Retrieve Operation for Book Model

### Command:
```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")

Expected Output:
<Book: 1984 by George Orwell (1949)>