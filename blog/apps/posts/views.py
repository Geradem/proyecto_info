#import get_object
from django.shortcuts import render, get_object_or_404
#importar la clase Post del Models(BD)
from .models import Post



# Create your views here.

def home_post(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')

def post_realizado(request):
    posteos = Post.objects.all() # Selec * from post
    return render(request, 'posts/post.html', {'posteos':posteos})

def post_detail(request, post_id):
    #busca el post y si no encuentra err 404
    post =get_object_or_404(Post, pk=post_id)
    ctx = {"post": post}
    return render(request, 'posts/post_detail.html', ctx )
