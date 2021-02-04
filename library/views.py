from django.shortcuts import render
from .models import Recording
import random


def library_list(request):
    return render(request, 'library/library_list.html', {})


def give_out_book(request):
    return render(request, 'library/give_out_book.html', {})


def get_post(request):
    try:
        recording = Recording(
            reader=request.POST['name'],
            author=request.POST['author'],
            title=request.POST['title'].upper()
        )
        recording.save()
        status = True
    except Exception as err:
        status = False
        return render(request, 'library/get_post.html', {'status': status, 'err': err})
    return render(request, 'library/get_post.html', {'status': status})


def reader_list(request):
    all_bd = Recording.objects.all()
    return render(request, 'library/reader_list.html', {'all_bd': all_bd})


def reader_search(request):
    return render(request, 'library/reader_search.html', {})


def search_result(request):
    title_value = request.POST['title'].upper()
    result = Recording.objects.filter(title__contains=title_value)
    return render(request, 'library/search_result.html', {'result': result})


def clean_bd(request):
    all_bd = Recording.objects.all()
    if all_bd:
        Recording.objects.all().delete()
        status = True
    else:
        status = False
    return render(request, 'library/clean_bd.html', {'status': status})


def generate_db(request):
    try:
        readers = _generate_readers()
        books = _generate_books()

        for i in range(1, 5000):  # сделать 5000 записей в БД
            reader = random.choice(readers)
            title, author = random.choice(books)
            recording = Recording(reader=reader, author=author, title=title.upper())
            recording.save()
        status = True
    except Exception as err:
        status = False
        return render(request, 'library/generate_db.html', {'status': status, 'err': err})
    return render(request, 'library/generate_db.html', {'status': status})


def _generate_books():
    books = []
    with open('library/book_unite.csv', mode='r', encoding='utf8') as file_books:
        for i in file_books:
            item = i[:-1].split('|')
            books.append((item[0], item[1]))
    return books


def _generate_readers():
    readers = []
    file_names = open('library/names_unite.csv', mode='r', encoding='utf8')
    file_surnames = open('library/surname_list.csv', mode='r', encoding='utf8')
    list_names = list(file_names)
    list_surnames = list(file_surnames)
    for i in range(1, 1000):  # сделать 1000 рамдомных читателей
        readers.append(random.choice(list_names)[:-1] + ' ' + random.choice(list_surnames)[:-1])
    file_names.close()
    file_surnames.close()
    return readers
