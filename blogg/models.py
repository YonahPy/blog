from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    conteudo = CKEditor5Field('conteudo', config_name='extends')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField('data', auto_now_add=True)
    slug = models.SlugField('slug', unique=True)
    resumo = CKEditor5Field('resumo', config_name='extends')
    imagem_resumo = models.ImageField('imagem_resumo', upload_to='imagens/' )