# Generated by Django 4.2.6 on 2023-10-18 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='titulo')),
                ('conteudo', django_ckeditor_5.fields.CKEditor5Field(verbose_name='conteudo')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]