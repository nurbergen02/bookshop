from django.shortcuts import render
from .models import Genre

def index(request):
    genres = Genre.objects.all()
    return render(request, 'mein/index.html', {'genres': genres})


def book_list(request):
    return render(request, 'mein/book_list.html')