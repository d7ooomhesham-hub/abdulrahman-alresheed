from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Student, Address, Publisher, Author, Gallery
from django.db.models import Q, Count, Avg, Max, Min, Sum
from django.utils import timezone
from datetime import datetime
from .forms import BookForm, StudentForm, GalleryForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# --- 1. الدوال الأساسية ---
def index(request): 
    return render(request, 'bookmodule/index.html')

def list_books(request):
    all_books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': all_books})

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html', {'bookId': bookId})

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

# --- 2. Lab 12: نظام المستخدمين والرسائل (Tasks 1, 2, 4, 5) ---

def register_user(request): #
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!') #
            return redirect('books:login')
    else:
        form = UserCreationForm()
    return render(request, 'bookmodule/users/register.html', {'form': form})

def login_user(request): #
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successfully!') #
            return redirect('books:index')
        else:
            messages.error(request, 'Error: Invalid credentials.') #
    else:
        form = AuthenticationForm()
    return render(request, 'bookmodule/users/login.html', {'form': form})

def logout_user(request): #
    logout(request)
    return redirect('books:login')

# --- 3. Lab 11: الطلاب والصور (Tasks 1, 2, 3) ---

@login_required(login_url='/books/users/login') #
def add_student(request): #
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('books:index')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11_add_student.html', {'form': form})

@login_required(login_url='/books/users/login') #
def add_to_gallery(request): #
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('books:index')
    else:
        form = GalleryForm()
    return render(request, 'bookmodule/lab11_gallery.html', {'form': form})

# --- 4. Lab 10: CRUD Operations (Part 1 & 2) ---

@login_required(login_url='/books/users/login') #
def lab10_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_listbooks.html', {'books': books})

def lab10_addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        Book.objects.create(title=title, price=price, quantity=quantity, rating=rating, pubdate=timezone.now())
        return redirect('books:lab10_listbooks')
    return render(request, 'bookmodule/lab10_addbook.html')

def lab10_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.rating = request.POST.get('rating')
        book.save()
        return redirect('books:lab10_listbooks')
    return render(request, 'bookmodule/lab10_editbook.html', {'book': book})

def lab10_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:lab10_listbooks')

def lab10_part2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_part2_listbooks.html', {'books': books})

def lab10_part2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pubdate = timezone.now()
            book.save()
            return redirect('books:lab10_part2_listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_part2_addbook.html', {'form': form})

def lab10_part2_editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:lab10_part2_listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_part2_editbook.html', {'form': form})

def lab10_part2_deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books:lab10_part2_listbooks')

# --- 5. Lab 9: الإحصائيات (Tasks 1 to 6) ---

def lab9_task1(request):
    total_q = Book.objects.aggregate(total=Sum('quantity'))['total'] or 1
    books = Book.objects.all()
    for b in books: b.availability_percentage = (b.quantity / total_q) * 100
    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})

def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(avg_price=Avg('book__price'), min_price=Min('book__price'), max_price=Max('book__price'))
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})

def lab9_task5(request):
    publishers = Publisher.objects.filter(book__rating__gte=4).annotate(high_rated_count=Count('book')).distinct()
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})

def lab9_task6(request):
    publishers = Publisher.objects.filter(book__price__gt=50, book__quantity__gte=1, book__quantity__lt=5).annotate(filtered_count=Count('book'))
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})

def add_lab9_data(request):
    p1, _ = Publisher.objects.get_or_create(name="O'Reilly Media", location="USA")
    p2, _ = Publisher.objects.get_or_create(name="Packt Publishing", location="UK")
    Book.objects.get_or_create(title="Django Advanced", price=120.0, quantity=10, pubdate=timezone.make_aware(datetime(2024, 1, 1)), rating=5, publisher=p1)
    Book.objects.get_or_create