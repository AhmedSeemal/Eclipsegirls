from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.
def home(request):
    boards = Board.objects.all()
    """board_names = list()
    for i in boards:
        board_names.append(i.name)     
    response_html = '<br>'.join(board_names)
    return HttpResponse(response_html) """
    return render(request, 'home.html', {'boards': boards})
       
        
        
    