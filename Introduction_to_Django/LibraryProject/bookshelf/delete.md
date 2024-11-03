# Delete Operation for Book Model

### Command:
```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="1984")
book_to_delete.delete()
Verification Command:
python
Copy code
Book.objects.all()

Expected Output:
<QuerySet []>