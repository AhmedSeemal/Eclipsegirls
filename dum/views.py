from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def home(request):
    book_list = Book.objects.all()
    """lis = list()
    for items in book_list:
        lis.append(items.book_name)    
    return HttpResponse('<br>'.join(lis)) """
    
    return render(request, 'index.html',{'books': book_list})    