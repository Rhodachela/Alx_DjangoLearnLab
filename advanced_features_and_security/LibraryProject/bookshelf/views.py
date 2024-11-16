from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.db.models import Q
from .forms import BookSearchForm

# Create your views here.
# Permission checks are applied using @permission_required to restrict access.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')

# Use Django ORM to prevent SQL injection and ensure safe handling of user inputs
# Example: Using Q objects for complex lookups instead of raw SQL
books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.raw(f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'")
    return render(request, 'bookshelf/book_list.html', {'books': books})

# bookshelf/views.py
def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books})

# bookshelf/views.py

def search_books(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['q']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
