from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User as m_User
from Books.models import Book as m_Book
from .forms import User
from random import randint

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            messages.success(request, f'Account created for {form.cleaned_data.get("first_name")}')
            return redirect('index')
    else:
        form = User()
    return render(request, 'Users/signup.html', {'form': form })

def favorites(request, user_name):
    user = m_User.objects.get(username=user_name)
    print(user.pk)
    books = user.favorites.all()
    return render(request, 'Users/favorites.html', {'books': books})

def addToFav(request, user_name, book_id):
    user = m_User.objects.get(username = user_name)
    book = m_Book.objects.get(pk = book_id)
    user.favorites.add(book)
    messages.success(request, f'{book.title} was added to your favorites successfully.')    
    return redirect('book', book_id, user.pk)

def remFromFav(request, user_name, book_id):
    user = m_User.objects.get(username = user_name)
    book = m_Book.objects.get(pk = book_id)
    user.favorites.remove(book)
    messages.success(request, f'{book.title} was removed from your favorites successfully.')
    return redirect('book', book_id, user.pk)

def issuedBooks(request, user_name):
    user = m_User.objects.get(username=user_name)
    books = user.issuedBooks.all()
    return render(request, 'Users/issuedBooks.html', {'books': books})

def addToIssued(request, user_name, book_id):
    book = m_Book.objects.get(pk = book_id)
    user = m_User.objects.get(username = user_name)
    if book.isIssued:
        messages.warning(request, f'{book.title} is issued to another person.')
        return redirect('book', book_id, user.pk)
    else:
        book.isIssued = True
        book.issuedTo = user
        book.save()
        messages.success(request, f'You can get the book "{book.title}" from counter no. {randint(1, 5)}')
        return redirect('book', book_id, user.pk)

def remFromIssued(request, user_name, book_id):
    book = m_Book.objects.get(pk = book_id)
    user = m_User.objects.get(username = user_name)
    issueDate_m = book.dateIssued.month
    issueDate_d = book.dateIssued.day - 14
    book.save()
    returnDate_m = book.dateReturned.month
    returnDate_d = book.dateReturned.day
    months = (issueDate_m - returnDate_m) * 30
    days = issueDate_d - returnDate_d
    fineMultiple = months + days
    if fineMultiple < 0:
        fine = 0
    else:
        fine = 10 * fineMultiple
    book.isIssued = False
    book.issuedTo = None
    book.dateIssued = None
    book.dateReturned = None
    book.save()
    if fine == 0:
        messages.success(request, f'Book returned successfully.')
        return redirect('issuedBooks', user.username)
    else:
        user.fine = user.fine + fine
        user.save()
        messages.warning(request, f'You returned the book {fineMultiple} days late. {fine} added to current fine amount.')
        return redirect('book', book_id, user.pk)