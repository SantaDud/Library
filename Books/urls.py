from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='index'),
    path("<int:book_id>/<int:user_id>", views.book, name='book'),
    path("search", views.search, name='search'),
]
