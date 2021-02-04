from django.urls import path
from .import views

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('give_out_book.html', views.give_out_book, name='give_out_book'),
    path("get_post.html", views.get_post, name='get_post'),
    path("reader_list.html", views.reader_list, name='reader_list'),
    path("reader_search.html", views.reader_search, name='reader_search'),
    path("search_result.html", views.search_result, name='search_result'),
    path("clean_bd.html", views.clean_bd, name='clean_bd'),
]
