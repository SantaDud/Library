from . import views
from django.urls import path
from django.contrib.auth.views import (
    LoginView as auth_login, 
    LogoutView as auth_logout,
    PasswordChangeDoneView, 
    PasswordChangeView,
    )
from django.urls import reverse_lazy

urlpatterns =[
    path('signup', views.signup, name='signup'),
    path(
        'passwordchange', 
        PasswordChangeView.as_view(
            template_name = 'Users/passwordchange.html', 
            success_url = reverse_lazy('PCdone')
        ), 
        name = 'passwordchange'
    ),
    path(
        'changesuccess',
        PasswordChangeDoneView.as_view(template_name = 'Users/PCdone.html'),
        name = 'PCdone'
    ),
    path('<str:user_name>/favorites', views.favorites, name='favorites'),
    path("<str:user_name>/<int:book_id>/added", views.addToFav, name='addToFav'),
    path('<str:user_name>/<int:book_id>/removed', views.remFromFav, name='remFromFav'),
    path("<str:user_name>/issued", views.issuedBooks, name='issuedBooks'),
    path("<int:book_id>/<str:user_name>/added", views.addToIssued, name='addToIssued'),
    path('<str:user_name>/<int:book_id>', views.remFromIssued, name='remFromIssued'),
    ]