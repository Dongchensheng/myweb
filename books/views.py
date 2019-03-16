from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here. student list
# def table(request):
#     students = {'Jack': [22, 'boy','Programmer'],
#                 'Alen': [27, 'boy', 'Designer'],
#                 'Una': [23, 'girl', 'Tester'],
#                 'Brant': [23, 'girl', 'Tester'],
#                 'David':  [23, 'boy', 'Tester']}
#     return render(request, 'table.html', {'student_list': students})

from books.models import *

def table(request):
    books = Book.objects.all()
    paginator = Paginator(books, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'table.html', {'pages': contacts})

def upload(request):
    files = File.objects.all()
    return render(request, 'upload.html', {'file_list': files})

def upload_save(request):
    files = File.objects.all()
    filename = request.POST.get('filename','')
    fileing = request.FILES.get('fileing','')
    if filename == '' or fileing == '':
        error = 'File and description cannot be empty!'
        return render(request, 'upload.html', {'error':error, 'file_list': files})
    else:
        upload = File()
        upload.filename = filename
        upload.fileway = fileing
        upload.save()
        return render(request,'upload.html', {'upload_success':'upload success!', 'file_list': files})