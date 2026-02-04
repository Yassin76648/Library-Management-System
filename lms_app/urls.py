from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('books', views.books, name="books"),
    path('addbook', views.add_book, name="add_book"),
    path('add_category', views.add_category, name="add_category"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
