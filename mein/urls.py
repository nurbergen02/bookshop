from django.urls import path

from .views import index, book_list

urlpatterns = [
    path('', index),
    path('listing/', book_list),
]