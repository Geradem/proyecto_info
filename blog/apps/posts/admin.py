from django.contrib import admin

# Register your models here.

from .models import Post

# registramos la clase para ver en el panel de administrador 
admin.site.register(Post)