from django.urls import path
from app.views import create_book, list_books, detail_book, update_book, delete_book

urlpatterns = [
    path('', create_book.as_view()),
    path('list_books/', list_books.as_view()),
    path('list_books/<pk>/', detail_book.as_view()),
    path('list_books/<pk>/update', update_book.as_view()),
    path('list_books/<pk>/delete', delete_book.as_view()),
]
