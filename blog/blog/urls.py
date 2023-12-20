from django.contrib import admin
from django.urls import path, include

#Import staticos/media
from django.conf.urls.static import static
from django.conf import settings

#mport loginview y logoutview
from django.contrib.auth.views import LoginView, LogoutView

#Import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto),
    path('acerca_de/', views.acerca_de),
    # path('categorias/', views.categorias),
    
    #urls de la aplicacion posts
    path('posts/', include('apps.posts.urls')),
    
    #urls para el login y logout
    path("login/", LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path("usuarios/", include("apps.usuarios.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)