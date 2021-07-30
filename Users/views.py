from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User as m_User
from .forms import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data.get("first_name")}')
            return redirect('index')
    else:
        form = User()
    return render(request, 'Users/signup.html', {'form': form })

def favorites(request, user_name):
    user = m_User.objects.get(username=user_name)
    books = user.favorites.all()
    return render(request, 'Users/favorites.html', {'books': books})