from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    latest_post_list = Post.objects.order_by('-pubdate')
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'latest_post_list': latest_post_list, 'form': form}
    
    return render(request, 'fanwebsite/index.html', context)
    