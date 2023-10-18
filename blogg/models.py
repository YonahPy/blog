from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    conteudo = CKEditor5Field('conteudo', config_name='extends')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField('data', auto_now_add=True)
    slug = models.SlugField('slug')
