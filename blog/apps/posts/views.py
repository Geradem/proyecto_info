from django.shortcuts import render

# Create your views here.



def post(request):
    return render(request, 'post.html')

def categorias_post(request):
    return render(request, 'posts/categorias.html')