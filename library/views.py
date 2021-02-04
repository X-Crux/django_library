from django.shortcuts import render
from .models import Recording


def library_list(request):
    return render(request, 'library/library_list.html', {})


def give_out_book(request):
    return render(request, 'library/give_out_book.html', {})


def get_post(request):
    try:
        recording = Recording(reader=request.POST['name'], author=request.POST['author'], title=request.POST['title'])
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
    title_value = request.POST['title']
    result = Recording.objects.filter(title__icontains=title_value)
    return render(request, 'library/search_result.html', {'result': result})


def clean_bd(request):
    all_bd = Recording.objects.all()
    if all_bd:
        Recording.objects.all().delete()
        status = True
    else:
        status = False
    return render(request, 'library/clean_bd.html', {'status': status})
