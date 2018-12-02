# Generated by Django 2.1.3 on 2018-11-29 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('body', models.TextField(blank=True, help_text='Enter the main content of the page')),
                ('image_cover', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Cover')),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageMetadata',
            fields=[
                ('metadata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seo.Metadata')),
            ],
            options={
                'verbose_name': 'page metadata',
                'verbose_name_plural': 'page metadata',
            },
            bases=('seo.metadata',),
        ),
        migrations.AddField(
            model_name='page',
            name='metadata',
            field=models.OneToOneField(blank=True, help_text='Add metadata for page SEO', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.PageMetadata'),
        ),
    ]