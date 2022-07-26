from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from app.models import Book

# create book view
class create_book(CreateView):
    model = Book
    fields = ['title', 'author', 'description']
    success_url = "/"


# list books view
class list_books(ListView):
    model = Book


# detail book view
class detail_book(DetailView):
    model = Book


# update book view
class update_book(UpdateView):
    model = Book
    fields = ['title', 'author', 'description']
    success_url = '/list_books/'


# delete book view
class delete_book(DeleteView):
    model = Book
    success_url = '/list_books/'
