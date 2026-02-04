from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    context = {
        'form': BookForm(),
        'category': Category.objects.all(),
        'books' : Book.objects.all(),
        'category_form':CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'soldbooks': Book.objects.filter(status="sold").count(),
        'rentedbooks': Book.objects.filter(status="rental").count(),
        'availablebooks': Book.objects.filter(status="available").count(),
    }

    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'category': Category.objects.all(),
        'books' : Book.objects.all()
    }
    return render(request, 'pages/books.html', context)

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()

    return render(request, 'pages/index.html', {'category_form': form})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()

    return render(request, 'pages/index.html', {'form': form})



def update(request, id):
        
    book = Book.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(request.POST ,request.FILES ,instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
        'book' : book
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('index')

    return render(request, "pages/delete.html", {'book': book})