from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dairy_Entry(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.PROTECT, default=None)

    # python manage.py makemigrations
    # python manage.py migrate

    def __str__(self):
        return self.titulo
    
    def snippet(self):
        return self.cuerpo[:50] + "..."
