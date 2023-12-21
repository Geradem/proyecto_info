from django.urls import path

#Import views
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_post, name='home_posts'),
    # path('categorias', views.categorias_post, name='categorias_posts'),
    
    #Posteos
    path('posteos/', views.post_realizado, name= 'post_realizado'),

    #post detail
    path('post_detail/<int:post_id>', views.post_detail, name= 'post_detail'),

    #urls comentarios
    path("comentario", views.comentar_posteo, name='comentar'),

    path("Borrar/<int:pk>", views.Borrar_Comentario.as_view(), name="borrar_comentario"),

    path("Modificar/<int:pk>", views.Modificar_Comentario.as_view(), name="modificar_comentario")
]
