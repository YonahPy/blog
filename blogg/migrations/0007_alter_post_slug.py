# Generated by Django 4.2.6 on 2023-10-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0006_alter_post_imagem_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]