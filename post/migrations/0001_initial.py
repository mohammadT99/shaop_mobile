# Generated by Django 4.0.8 on 2022-12-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.CharField(max_length=12)),
                ('masege', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='image')),
                ('desc', models.TextField()),
                ('publish', models.CharField(max_length=50)),
                ('drct', models.CharField(choices=[('p', 'publish'), ('d', 'drsft')], max_length=50)),
            ],
        ),
    ]
