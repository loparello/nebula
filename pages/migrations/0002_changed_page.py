# Generated by Django 2.1.3 on 2018-12-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='body',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image_cover',
        ),
        migrations.AddField(
            model_name='page',
            name='is_homepage',
            field=models.BooleanField(default=False, help_text='Set page as home page without ambiguity', verbose_name='Home page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(help_text='Set page url and database reference (auto-generated from title)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(help_text='Set title to display in page and in navigation', max_length=200),
        ),
    ]