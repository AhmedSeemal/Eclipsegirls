from django.shortcuts import render
from blog.models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(title = 'sample')
    return render(request, 'blog/post_list.html', {'posts': posts} )

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

	
