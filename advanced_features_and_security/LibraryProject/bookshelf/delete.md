# Delete Operation for Book Model

### Command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
Verification Command:
Book.objects.all()

Expected Output:
<QuerySet []>