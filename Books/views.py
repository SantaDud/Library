from django.shortcuts import render
from .models import Book as m_Book
from Users.models import User as m_User
from random import randint


def index(request):
    numberOfBooks = m_Book.objects.count()
    if (numberOfBooks):
        first = m_Book.objects.first().pk
        bookIds = []
        for i in range(3):
            temp = randint(first, numberOfBooks + first - 1)
            while(temp in bookIds):
                temp = randint(first, numberOfBooks + first - 1)
            bookIds.append(temp)
        return render(request, 'Books/index.html', {
            "books": m_Book.objects.all(),
            "rBook1": m_Book.objects.get(pk = int(bookIds[1])),
            "rBook2": m_Book.objects.get(pk = int(bookIds[0])),
            "rBook3": m_Book.objects.get(pk = int(bookIds[2])),
        })
    else:
        return render(request, "Books/index.html")

def book(request, book_id, user_id):
    if user_id == 0:
        return render(request, 'Books/book.html', {
            "book": m_Book.objects.get(pk = book_id),
        })
    else:
        user = m_User.objects.get(pk = user_id)
        user_favorites = user.favorites.all()
        user_issued = user.issuedBooks.all()
        return render(request, 'Books/book.html', {
            "book": m_Book.objects.get(pk = book_id),
            "user_favorites": user_favorites,
            "user_issued": user_issued
        })

def search(request):
    searchText = request.GET['searchText']
    return render(request, 'Books/search.html', {
        "books": m_Book.objects.filter(title__icontains = searchText)
    })
